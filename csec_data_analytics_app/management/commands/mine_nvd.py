from django.core.management.base import BaseCommand
from csec_data_analytics_app.models import Vulnerability
from csec_data_analytics_app.utility import NvdApiUtility
from datetime import datetime


class Command(BaseCommand):

    help = 'Mine NVD for CVE data and store in MongoDB'

    def handle(self, *args, **kwargs):
        api_key = 'd25283de-955f-4bff-b596-2dc898eb9162'
        items = 20000
        start_index = 0
        # Extract CVE data
        while start_index < items:
            cve_data = NvdApiUtility.extract_cve_data(api_key, start_index)

            if cve_data and 'vulnerabilities' in cve_data:
                vulnerabilities = cve_data['vulnerabilities']

                for cve_item in vulnerabilities:
                    # Extract relevant information and save to the database
                    Vulnerability.objects.create(
                        cve_id=cve_item['cve']['id'],
                        description=cve_item['cve']['descriptions'][0]['value'],
                        cpe_configurations=cve_item['configurations'][0]['nodes'] if cve_item.get('configurations') else [],
                        cwes=[entry['cwe']['ID'] for entry in
                              cve_item.get('cve', {}).get('problemtype', {}).get('problemtype_data', [])],
                        cisa_exploitability_metric=cve_item.get('impact', {}).get('cvss', {}).get('exploitabilityScore',
                                                                                                  None),
                        cvss=cve_item.get('impact', {}).get('cvss', {}).get('baseScore', None),
                        published_date=datetime.strptime(cve_item['cve']['published'], "%Y-%m-%dT%H:%M:%S.%f"),
                        last_modified_date=datetime.strptime(cve_item['cve']['lastModified'], "%Y-%m-%dT%H:%M:%S.%f")
                    )
            else:
                print("No vulnerabilities found in the response.")

            start_index = start_index + 1000
