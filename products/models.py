from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    thermal_value = models.DecimalField(max_digits=4, decimal_places=2, default='0.22')
    product_type = models.CharField(max_length=125, default='')
    thickness = models.DecimalField(max_digits=4, decimal_places=1, default='12.5')
    m2_coverage = models.DecimalField(max_digits=4, decimal_places=2, default='10.64')
    recomended_for = models.CharField(max_length=100, default='')



    def __str__(self):
        return self.name