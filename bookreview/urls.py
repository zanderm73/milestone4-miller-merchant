from django.conf.urls import url, include
from .views import each_book_review, book_vote, view_votes, review_landing

urlpatterns = [
    url(r'^$', review_landing, name='reviewlanding'),
    url(r'^review/', each_book_review, name='eachbookreview'),
    url(r'^vote/', book_vote, name='bookvote'),
    url(r'^score/', view_votes, name='viewvotes'),

]
