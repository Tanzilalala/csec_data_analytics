from django.core.management.base import BaseCommand
from csec_data_analytics_app.models import CisaVulnerability
from csec_data_analytics_app.cisaUtility import CisaApiUtility
from datetime import datetime

class Command(BaseCommand):

    help = "mine CISA data"
    def handle(self, *args, **kwargs):

        cve_data = CisaApiUtility.fetch_cve_data()

        if cve_data:
            # Update the exploitability metric
            updated_cve_data = CisaApiUtility.update_exploitability_metric(cve_data)
            if updated_cve_data and 'vulnerabilities' in updated_cve_data:
                vulnerabilities = updated_cve_data['vulnerabilities']

                for cve_item in vulnerabilities:
                    # Extract relevant information and save to the database
                    CisaVulnerability.objects.create(
                        cve_id=cve_item['cveID'],  # Update to match the JSON structure
                        description=cve_item['shortDescription'],  # Update to match the JSON structure
                        cpe_configurations=cve_item.get('configurations', {}).get('nodes', []),
                        # Update to match the JSON structure
                        cwes=[entry['cwe']['ID'] for entry in
                              cve_item.get('cve', {}).get('problemtype', {}).get('problemtype_data', [])],
                        cisa_exploitability_metric="HIGH" if cve_item[
                                                                 'knownRansomwareCampaignUse'] == "Known" else None,
                        # Added condition based on knownRansomwareCampaignUse
                        cvss=None,  # You may need to fetch this data from elsewhere in the JSON
                        published_date=datetime.strptime(cve_item['dateAdded'], "%Y-%m-%d"),
                        # Update to match the JSON structure
                        last_modified_date=None  # You may need to fetch this data from elsewhere in the JSON
                    )

            else:
                print("No vulnerabilities found in the response.")

            # Now 'updated_cve_data' contains the CVE records with the correct metric for exploitability
        else:
            print("Failed to fetch CVE data from the provided URL.")
