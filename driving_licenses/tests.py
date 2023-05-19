from rest_framework.test import APITestCase
from . import models
from users.models import User

class TestExplanations(APITestCase):

    NAME = "Explanation Test"
    DESCRIPTION = "Explanation Des Test"
    URL = "http://localhost:8000/api/v1/driving_licenses/explanations/"

    def setUp(self):
        models.Explanation.objects.create(
            name = self.NAME,
            description = self.DESCRIPTION,
                    )

    def test_all_explanations(self):

        response = self.client.get(self.URL)
        data = response.json()

        self.assertEqual(response.status_code, 200, "Status code isn't 200.")

        self.assertIsInstance(data, list,)
        self.assertEqual(len(data), 1,)
        self.assertEqual(data[0]["name"], self.NAME,)
        self.assertEqual(data[0]["description"], self.DESCRIPTION,)

    def test_create_explanation(self):

        new_explanation_name = "New Explanation"
        new_explanation_description = "New Explanation Desc."

        response = self.client.post(self.URL, data={"name": new_explanation_name, "description": new_explanation_description,},
        )
        data = response.json()
    
        self.assertEqual(response.status_code, 200, "Not 200 status code",)

        self.assertEqual(data["name"], new_explanation_name,)
        self.assertEqual(data["description"], new_explanation_description,)

        response = self.client.post(self.URL)
        self.assertEqual(response.status_code, 200)
        self.assertIn("name", data)

class TestExplanation(APITestCase):

    NAME = "Test Explanation"
    DESC = "Test Explanation Dsc"

    def setUp(self):
        models.Explanation.objects.create(
            name=self.NAME,
            description=self.DESC,
        )

    def test_explanation_not_found(self):
        response = self.client.get("http://localhost:8000/api/v1/driving_licenses/explanations/2")

        self.assertEqual(response.status_code, 404)

    def test_get_explanation(self):

        response = self.client.get("http://localhost:8000/api/v1/driving_licenses/explanations/1")

        self.assertEqual(response.status_code, 200)

        data = response.json()

        self.assertEqual(data["name"], self.NAME,)
        self.assertEqual(data["description"],self.DESC,)

    def test_put_explanation(self):
        
        revised_explanation_name = "Revised Explanation"
        revised_explanation_description = "Revised Explanation Desc."

        response = self.client.put("http://localhost:8000/api/v1/driving_licenses/explanations/1", data={"name": revised_explanation_name, "description": revised_explanation_description,},
        )
        data = response.json()
    
        self.assertEqual(response.status_code, 200, "Not 200 status code",)

        self.assertEqual(data["name"], revised_explanation_name,)
        self.assertEqual(data["description"], revised_explanation_description,)

        response = self.client.put("http://localhost:8000/api/v1/driving_licenses/explanations/1")
        self.assertEqual(response.status_code, 200)

    def test_delete_explanation(self):
        response = self.client.delete("http://localhost:8000/api/v1/driving_licenses/explanations/1")
        self.assertEqual(response.status_code, 204)

class TestDriving_licenses(APITestCase):
    def setUp(self):
        user = User.objects.create(
        username = "test",
        )
        user.set_password("123")
        user.save()
        self.user = user
            
    def test_create_driving_license(self):

        response = self.client.post("http://localhost:8000/api/v1/driving_licenses/")

        self.assertEqual(response.status_code, 403)

        self.client.force_login(
            self.user,
        )

        response = self.client.post("http://localhost:8000/api/v1/driving_licenses/")

        print(response)
        print(response.json())