import os
import requests
from dotenv import load_dotenv


class LinkedInProfileScraper:
    def __init__(self, linkedin_url: str, mock: bool = False) -> dict:
        load_dotenv()
        self._api_endpoint = "https://api.scrapin.io/enrichment/profile"
        self._api_key = os.getenv("SCRAPER_API_KEY")
        self._mock_url = os.getenv("MOCK_URL")
        self._linkedin_url = linkedin_url
        self._mock = mock

    def scrape_linkedin_profile(self) -> str:
        """
        Scrapes a LinkedIn profile for the given person's name.
        This function is a placeholder and should be implemented with actual scraping logic.
        """
        # Placeholder URL for LinkedIn profile scraping
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        try:
            if self._mock == False:
                print(f"Scraping LinkedIn profile for URL: {self._linkedin_url}")
                params = {
                    "linkedin_url": self._linkedin_url,
                    "api_key": self._api_key,  # Ensure you have set this in your .env file
                }

                response = requests.get(
                    api_endpoint,
                    params=params,
                    timeout=10,  # Set a timeout for the request
                )
                print(f"Response status code: {response.status_code}")
                if response.status_code == 200:
                    print("Profile scraped successfully.")
                    print(response.json())
                    return response.json()
                # elif response.status_code == 404 or response.status_code == 401:
                #   return "To fetch the LinkedIn profile, please provide a proper API Key. The API Key must be set in the .env file and must be from paid plan."
            elif self._mock == True:
                response = requests.get(self._mock_url, timeout=10)  # Use the mock URL

                print(f"Response status code: {response.status_code}")
                print("Profile scraped successfully.")
                print(response.json())
                return response.json()

        except Exception as e:
            print(f"Error scraping LinkedIn profile: {e}")
            return None
