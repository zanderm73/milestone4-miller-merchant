from django.db import models
from product.models import Product

# Create your models here.

# model that allows the user to input their data during the order process when at checkout
class Order(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=40, blank=False)
    delivery_address = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=40, blank=False)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


# model that brings together the customers data, products they have selected and quantity added to cart
# to allow the user to progress to the payment page
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.name, self.product.price)