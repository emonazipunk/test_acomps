import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestOrgUnit(BaseCase):

    def setup(self):
        self.base_url = 'https://demo.u-system.tech/api/v1/org-units'
        self.company_name = 'lapka'

    def test_get_all_org_units(self):
        session = requests.Session()
        session.verify = False  # отключает проверку сертификата

        response = session.get(self.base_url)
        Assertions.assert_status_code(response, 403)
        print(response.content.decode('utf-8'))
