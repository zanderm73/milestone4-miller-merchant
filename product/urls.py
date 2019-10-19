from django.conf.urls import url, include
from .views import all_products, all_publishers, all_authors, each_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^author/', all_authors, name='author'),
    url(r'^publisher/', all_publishers, name='publisher'),
    url(r'^eachproduct/', each_product, name='eachproduct'),

]