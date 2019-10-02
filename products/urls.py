from django.conf.urls import url, include
from .views import all_products, mineralwool, plasterboard, pir, thermallaminate

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^mineralwool/', mineralwool, name='mineralwool'),
    url(r'^plasterboard/', plasterboard, name='plasterboard'),
    url(r'^pir/', pir, name='pir'),
    url(r'^thermallaminate/', thermallaminate, name='thermallaminate'),
]