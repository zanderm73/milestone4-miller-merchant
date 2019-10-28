from django.db import models

# Create your models here.
class Publisher(models.Model):
    names = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=100, default='')
    country = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.names


class Author(models.Model):
    name = models.CharField(max_length=100, default='name')
    author_bio = models.CharField(max_length=1000, default='author-bio')
    author_image = models.ImageField(upload_to='images', default='')
    nationality = models.CharField(max_length=100, default='nationality')
    date_of_birth = models.DateField(default='1990-08-08')

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100, default='')
    product_decription = models.CharField(max_length=1000, default='description')
    image = models.ImageField(upload_to='images', default='')
    authors = models.ForeignKey(Author)
    publisher = models.ForeignKey(Publisher)
    date_published = models.DateField(default='1990-08-08')
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=100, default='')
    average_reading_time = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title
