from playground.models import Product
from django.db import connection
from django.test import Client, TestCase


class PlayGround(TestCase):
    """
    Test cases for the PlayGround functionality.

    This class defines test cases to ensure the proper functioning of the PlayGround features.
    """

    def setUp(self):
        """
        Set up the required data and client for the test cases.

        This method is called before each test case execution to set up the necessary data
        and the client for making HTTP requests.
        """
        self.product1 = Product.objects.create(name="hellomoto", price=10.4, quantity=3)
        self.product2 = Product.objects.create(name="Nokia", price=111.1, quantity=4)
        self.client = Client()

    def raise_exception(self):
        """
        Helper method to raise an exception.

        This method raises an exception for simulating negative scenarios in the test cases.
        """
        raise Exception("Test exception")

    def test_show_product_form(self):
        """
        Test the behavior of the "show_product_form" view.

        This test case verifies that the "show_product_form" view returns the expected response
        with the correct template and context when accessed successfully.
        """
        response = self.client.get("/show-product-form")
        self.assertEqual(response.status_code, 200)
        expected_queryset = Product.objects.filter(
            id__in=[self.product1.id, self.product2.id]
        )
        actual_queryset = response.context["products"]
        self.assertQuerysetEqual(actual_queryset, expected_queryset, ordered=False)
        self.assertTemplateUsed(response, "show_product_form.html")

    def test_show_product_form_negative(self):
        """
        Test the negative scenario for the "show_product_form" view.

        This test case simulates an exception being raised when retrieving the products
        and verifies that the error page is rendered with the expected message.
        """
        response = self.client.get("/show-product-form")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "error.html")
        self.assertEqual(response.context["message"], "Exception occur: Test exception")
