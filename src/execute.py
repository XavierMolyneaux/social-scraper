"""
Execute the scraper.
"""
from dotenv import load_dotenv
from src.api.hunter_search import HunterSearch
from src.api.twitter_scrape import TwitterScrape

load_dotenv() # load env variables from .env file. Each module will load its respected variables.
twitter_handle = ""

# Social Media Filtering
ts = TwitterScrape(twitter_handle)


# Hunter Data Handling
hs = HunterSearch(domain=)
hunter_data = hs.domain_search()
data = hs.create_list_from_leads(hunter_data) # send this data to spreadsheet creation