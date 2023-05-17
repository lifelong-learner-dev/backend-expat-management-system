from rest_framework.test import APITestCase

class TestExplanations(APITestCase):
    def test_all_explanations(self):

        response = self.client.get("http://localhost:8000/api/v1/driving_licenses/explanations/")
        print(response.status_code)
        print(response.content)
