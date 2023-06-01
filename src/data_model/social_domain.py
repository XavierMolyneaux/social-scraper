"""
Module used to parse standardized data from a social media API repsonse.
"""
from dataclasses import dataclass

@dataclass
class SocialMediaUser:
    """
    Class to standardize what a social media user should look like. A user is defined as a company, 
    typically will be the company's social media account.
    """
    name: str
    domain: str
    description: str
    external_id: str  # User defined screen name, handle or alias
    source: str = "Twitter"  # TODO: Remove this default once other social platforms are supported.
    country: str = "US"  # TODO: A piece of data we will want to validate.