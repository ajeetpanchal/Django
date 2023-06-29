from django.db import models


class Product(models.Model):
    """
    Represents a product.

    Fields:
    - name (CharField): The name of the product. Max length: 255 characters.
    - price (DecimalField): The price of the product. Max digits: 10, Decimal places: 2.
    - quantity (PositiveIntegerField): The quantity of the product.
    """

    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
