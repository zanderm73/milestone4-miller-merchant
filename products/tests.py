from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTests(TestCase):
    """
    test that we'll run against our product model

    """

    def test_str(self):
        test_name = Product(name='knauf')
        self.assertEqual(str(test_name), 'knauf')