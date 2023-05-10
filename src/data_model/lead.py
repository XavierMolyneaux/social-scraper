"""
Module used parse response data from Hunter. Hunter returns lists of emails for a given company
domain.
"""
from dataclasses import dataclass
from src.exceptions import LeadError


@dataclass
class HunterLead:
    """
    Class to house data and functions of a lead returned by the Hunter API. 
    A lead is defined as CEO, CXO, CTO, etc of a company.
    """

    @classmethod
    def _validate_data(self, data):
        """
        Data validation for the object. Confirm lead's name is present and email is deliverable.
        """
        if data.name is None:
            raise LeadError.unknown_name(data)
        elif data.deliverable is not "valid":
            raise LeadError.email_undeliverable(data)

    def __init__(self, data) -> None:
        """
        Initialize object (lead) with data fetched from Hunter.
        Args:
            data (dict): Data from Hunter API
        """
        self._validate_data(data)
        self.__dict__ = data
    
    def __repr__(self) -> str:
        """
        Class representation.
        Returns:
            str: _description_
        """
        return f"{self.__class__.__name__}({self.__dict__})"