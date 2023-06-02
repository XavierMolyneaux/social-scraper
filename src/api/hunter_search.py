"""
Module used to make requests to Hunter given a company domain.

ref: https://hunter.io/api/domain-search
Note: In our case the domain will come from the search/filtering made on twitter. - 5/9/2023
"""
import os
import json
import requests
from src.data_model.lead import HunterLead
from src.exceptions import ApiError, LeadError

class HunterSearch:
    """
    Hunter API function.
    """

    def __init__(self, domain):
        """   
        Set API key, company domain and list of acceptable employee positions.            
        """
        self._api_key = os.getenv("HUNTER_API_KEY")
        self.domain = domain
        # Create acceptable employee positions list 
        f = open("src/data/employee_positions.json")
        data = json.load(f)
        self.decision_makers = data["positions"]
        f.close()

    def domain_search(self):
        """
        For the given domain, make a request to Hunter's domain search.

        Args:
            domain (str): A company's we domain.
        """
        url = f"https://api.hunter.io/v2/domain-search?domain={self.domain}&api_key={self._api_key}"
        request = request.get(url)
        if request.status_code == 200:
            request_data = request.json()
            return request_data["data"]
        else:
           raise ApiError.hunter_error(self.domain)

    def create_lead(self, lead_data, company, state, city) -> HunterLead:
        """
        Take the email data from the hunter request and create a lead.

        Args:
            lead_data (dict): A single lead from Hunter's response data.
        Returns:
            HunterLead: A single lead.
        """
        if lead_data["position"] in self.decision_makers:
            return HunterLead(
                name = f"{lead_data['first_name']} {lead_data['last_name']}",
                email = lead_data["value"],
                deliverable = lead_data["verification"]["status"],
                position = lead_data["position"],
                phone_number = lead_data["phone_number"],
                email_type = lead_data["type"],
                company = company,
                department = lead_data["department"],
                domain = self.domain,
                state = state,
                city = city
            )
        else:
            raise LeadError.irrelevant_lead(lead_data)

    def create_list_from_leads(self, data) -> list[HunterLead]:
        """
        Create a list of leads using instances of HunterLead.
        Returns: 
            list[HunterLead]: The list will be passed to the spreadsheet setup module.
        """
        email_data = data["emails"]
        company = data["organization"]
        country = data["country"] if data["country"] else "US"
        state = data["state"]
        city = data["city"]
        if country == "US":
            for lead in email_data:
                yield self.create_lead(lead, company, country, state, city)
        else:
            raise LeadError.irrelevant_domain(self.domain)