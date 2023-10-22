import requests
from datetime import datetime

class NvdApiUtility:
    BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

    @staticmethod
    def extract_cve_data(api_key, start_index):
        base_url = "https://services.nvd.nist.gov/rest/json/cves/2.0"

        params = {
            "startIndex": start_index,  # Start from the beginning
            "resultsPerPage": 1000,  # Get only one result for testing
        }

        headers = {
            "Content-Type": "application/json",
            "x-api-key": api_key
        }

        try:
            response = requests.get(base_url, params=params, headers=headers)

            # Check if the request was successful
            response.raise_for_status()
            print(response.json())

            # Return the JSON data
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        return None
