from django.conf.urls import url, include
from .views import book_review, book_vote, view_votes

urlpatterns = [
    url(r'^$', book_review, name='bookreview'),
    url(r'^vote/', book_vote, name='bookvote'),
    url(r'^score/', view_votes, name='viewvotes'),

]
