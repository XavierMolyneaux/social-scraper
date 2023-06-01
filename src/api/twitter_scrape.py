"""
Module used to filter through the followers of a given twitter account. Each follower's
description/bio will be evaluated against a list of keywords to determine if it is a 
qualified company.

ref: https://docs.tweepy.org/en/stable/client.html & https://docs.tweepy.org/en/stable/getting_started.html
"""
import os
import json

from src.data_model.social_domain import SocialMediaUser

class TwitterScrape:
    """
    Class used to scrape twitter data.
    """

    def __init__(self, handle) -> None:
        self._api_key = os.getenv("TWITTER_API_KEY")
        self.handle = handle
        self.domain_list = list()
        # create accepted keywords list.
        f = open("src/data/accepted_keywords.json")
        data = json.load(f)
        self.accepted_keywords = data["keywords"]
        f.close()
        # create blacklisted keywords list.
        f2 = open("src/data/blacklisted_keywords.json")
        data = json.load(f2)
        self.blacklist_keywords = data["keywords"]
        f2.close()

    def twitter_search(self):
        """
        Function used to filter through an account followers and gather relevant data.
        """
        pass

    def parse_account_data(self, account):
        """
        Method to extract domains and any other required account data from Twitter's response.
        """
        return SocialMediaUser(
            name="",
            domain="",
            description="",
            external_id="",
            source="Twitter",
            country="US"
        )
    
    def relevant_account(self, data):
        """
        Method to determine if the account is relevant based on it's bio/description. The account must contain a keyword
        within the the accepted keywords list and none in the blacklisted keywords list.
        """
        pass

    def create_domain_list(self, followers):
        """
        Method to add relevant domains to our list. 
        """ 
        for account in followers:
            data = self.parse_account_data(account)
            if self.relevant_account:
                self.domain_list.append(data["url"])
        return self.domain_list
