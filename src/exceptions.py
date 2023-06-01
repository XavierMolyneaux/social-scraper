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
    

class ApiError(Exception):
    """
    Errors related to api requests.
    """

    @classmethod
    def hunter_error(self, domain):
        """
        There was an issue making a request to Hunter.io for a given domain.
        """
        return f"Error when making request to Hunter with domain: {domain}"
    
    @classmethod
    def twitter_error(self):
        """
        There was an issue making a request to Twitter for a given account.
        """
        return f""