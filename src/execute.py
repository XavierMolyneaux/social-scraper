"""
Execute the scraper.
"""
from dotenv import load_dotenv
from src.api.hunter_search import HunterSearch
from src.api.twitter_scrape import TwitterScrape

load_dotenv() # load env variables from .env file. Each module will load its respected variables.
twitter_handle = ""
leads = list()

# Social Media Filtering
ts = TwitterScrape(twitter_handle)
twitter_followers = ts.twitter_search()
domains = ts.create_domain_list(twitter_followers)



# Hunter Data Handling
for domain in domains:
    hs = HunterSearch(domain=domain)
    hunter_data = hs.domain_search()
    hunter_leads = hs.create_list_from_leads(hunter_data) # send this data to spreadsheet creation
    leads.append(hunter_leads)


# for company in leads:
#     for employee in company:
#       # upload employee to spreadsheet