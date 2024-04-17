import os

import requests
from dotenv import load_dotenv
import json

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_user_id: str, mock: bool = False):
    """Scrape information from LinkedIn profiles,
       Manually scrape the information from the LinkedIn Profile User."""

    data = {}

    if mock:
        # Load the data from the JSON file
        with open('data.json', 'r') as file:
            data = json.load(file)
    else:
        url = "https://api.scrapingdog.com/linkedin/"

        params = {
            "api_key": os.getenv("SCRAPEDOG_API_KEY"),
            "type": "profile",
            "linkId": linkedin_profile_user_id
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
        else:
            print(f"Request failed with status code: {response.status_code}")

    print(data)

    return data


if __name__ == "__main__":
    print(scrape_linkedin_profile(linkedin_profile_user_id="https://www.linkedin.com/in/tylerreedai"))
