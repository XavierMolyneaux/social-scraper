"""
Module used parse response data from Hunter. Hunter returns lists of emails for a given company
domain.
"""
from dataclasses import dataclass, field
from src.exceptions import LeadError


@dataclass(frozen=True, order=True)
class HunterLead:
    """
    Class to house data and functions of a lead returned by the Hunter API. 
    A lead is defined as CEO, CXO, CTO, etc of a company.
    """
    name: str
    email: str
    deliverable: str
    position: str = ""
    phone_number: str = ""
    email_type: str = ""
    company: str = ""
    department: str = ""
    domain: str = ""
    state: str = ""
    city: str = ""
    

    @classmethod
    def _validate_data(cls, data) -> None:
        """
        Data validation for the object. Confirm lead's name is present and email is deliverable.
        """
        if data.name is None:
            raise LeadError.unknown_name(data)
        elif data.deliverable is not "valid":
            raise LeadError.email_undeliverable(data)
        

@dataclass(frozen=True)
class LeadList:
    """
    Class to house data for a list of HunterLead
    """
    leads: list[HunterLead] = field(default_factory=list)