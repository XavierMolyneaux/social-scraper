"""
Module used to filter through the followers of a given twitter account. Each follower's
description/bio will be evaluated against a list of keywords to determine if it is a 
qualified company.

ref: https://docs.tweepy.org/en/stable/client.html & https://docs.tweepy.org/en/stable/getting_started.html
"""
import os
import json
import tweepy

from src.data_model.social_domain import SocialMediaUser

class TwitterScrape:
    """
    Class used to scrape twitter data.
    """

    def __init__(self, handle) -> None:
        """
        Authenticate Twitter client and establish keyword filters.
        ref: https://docs.tweepy.org/en/stable/authentication.html
        """
        self.client = tweepy.Client(consumer_key=os.getenv("TWITTER_CONSUMER_KEY"),
                                    consumer_secret=os.getenv("TWITTER_CONSUMER_SECRET"), 
                                    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
                                    access_token_secret=os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
                                    )
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
        Function used to gather follower data.
        """
        # get userID of given handle
        user = self.client.get_user(username=self.handle)
        user_id = user["data"]["id"]
        # use userID to fetch followers
        followers = self.client.get_users_followers(id=user_id, user_fields=["description", "location", "username", "url"])
        return followers


    def parse_account_data(self, account):
        """
        Method to extract domains and any other required account data from Twitter's response.
        """
        return SocialMediaUser(
            name=account["username"],
            domain=account["url"],
            description=account["description"],
            external_id=self.handle,
            source="Twitter",
            country="US"
        )
    
    def relevant_account(self, data):
        """
        Method to determine if the account is relevant based on it's bio/description. The account must contain a keyword
        within the the accepted keywords list and none in the blacklisted keywords list.
        """
        accepted_keyword_found = False
        for word in data["description"]:
            if word in self.blacklist_keywords:
                return False
            if word in self.accepted_keywords:
                accepted_keyword_found = True
        return accepted_keyword_found
        
    def create_domain_list(self, followers):
        """
        Method to add relevant domains to our list. 
        """ 
        for account in followers["data"]:
            data = self.parse_account_data(account)
            if self.relevant_account(data):
                self.domain_list.append(data["url"])
        return self.domain_list
