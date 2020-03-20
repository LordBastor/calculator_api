from django.test import TestCase

from rest_framework.test import APIClient


class EvaluateExpressionTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_simple_addition_response(self):
        response = self.client.post(
            "/api/v1/evaluate_expression", {"expression": "2 + 2"}, format="json"
        )

        data = response.data

        self.assertEquals(response.status_code, 200)
        self.assertTrue("result" in data)
        self.assertEquals(data["result"], 4.0)

    def test_view_server_error(self):
        response = self.client.post(
            "/api/v1/evaluate_expression",
            {"expression": "Whoa this is invalid"},
            format="json",
        )

        data = response.data

        self.assertEquals(response.status_code, 400)
        self.assertTrue("validation_error" in data)
