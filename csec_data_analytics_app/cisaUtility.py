import requests
from csec_data_analytics_app.models import CisaVulnerability

class CisaApiUtility:
    @staticmethod
    def fetch_cve_data():
        url = "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json"

        try:
            response = requests.get(url)

            # Check if the request was successful
            response.raise_for_status()

            # Return the JSON data
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
        except Exception as err:
            print(f"An error occurred: {err}")

        return None

    @staticmethod
    def update_exploitability_metric(cve_data):
        # Assuming cve_data['vulnerabilities'] is a list of CVE records
        for cve_record in cve_data['vulnerabilities']:
            cve_id = cve_record['cveID']
            # Check if this CVE has known exploited vulnerabilities
            if cve_record['knownRansomwareCampaignUse'] == "Known":
                # Update the exploitability metric (for example, adding a new field 'exploitabilityMetric')
                cve_record['exploitabilityMetric'] = "HIGH"
        return cve_data
