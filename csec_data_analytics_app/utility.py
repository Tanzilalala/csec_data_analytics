from datetime import datetime, timedelta
import requests
class NvdApiUtility:
    BASE_URL = "https://services.nvd.nist.gov/rest/json/cves/1.0"

    @staticmethod
    def extract_cve_data(api_key, start_index):
        base_url = "https://services.nvd.nist.gov/rest/json/cves/1.0"

        # Set the start date to January 1, 2021
        # start_date = "2021-01-01"

        # Calculate the end date, 120 days later
        # start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
        # end_datetime = start_datetime + timedelta(days=120)
        # end_date = end_datetime.strftime("%Y-%m-%d")

        params = {
            # "pubStartDate": start_date,
            # "pubEndDate": end_date,
            "resultsPerPage": 1000  # Get only one result for testing
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