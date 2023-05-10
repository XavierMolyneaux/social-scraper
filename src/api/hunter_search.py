"""
Module used to make requests to Hunter given a company domain.

ref: https://hunter.io/api/domain-search
Note: In our case the domain will come from the search/filtering made on twitter. - 5/9/2023
"""

class HunterSearch:
    """
    Hunter API function.
    """

    def __init__(self):
        """
        A lead returned from a Hunter response should contain the following data:
            name (str): _description_
            email (str): _description_
            phone_number (str or None): _description_
            email_type (str or None): _description_
            deliverable (str): _description_
            position (str or None): _description_
            seniority (str or None): _description_
            department (str or None): _description_
        """
        pass