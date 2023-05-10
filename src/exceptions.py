"""
Error Handling.
"""

class LeadError(Exception):
    """
    Errors related to lead data
    """

    @classmethod
    def unknown_name(self, data):
        """
        Name missing from lead data.
        """
        return f"Unknown name in lead instance: {data}"
    
    @classmethod
    def email_undeliverable(self, data):
        """
        Lead email is undeliverable.
        """
        return f"Lead email is undeliverable for lead instance: {data}"