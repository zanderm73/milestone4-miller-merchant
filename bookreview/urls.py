from django.conf.urls import url, include
from .views import review_landing, current_book_review, book_vote, view_votes, review_list, prev_book_review

urlpatterns = [
    url(r'^$', review_landing, name='reviewlanding'),
    url(r'^review/', current_book_review, name='currentbookreview'),
    url(r'^vote/', book_vote, name='bookvote'),
    url(r'^score/', view_votes, name='viewvotes'),
    url(r'^reviewlist/', review_list, name='reviewlist'),
    url(r'^previousreview(?P<pk>\d+)/$', prev_book_review, name='previousreview'),
]
