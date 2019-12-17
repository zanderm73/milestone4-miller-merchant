from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BookReview(models.Model):
    bookname = models.CharField(max_length=100, default='')
    bookimage = models.ImageField(upload_to='images', default='')
    bookauthor = models.CharField(max_length=100, default='')
    bookpublisher = models.CharField(max_length=100, default='')
    bookreview = models.CharField(max_length=1000, default='')
    authorscomments = models.CharField(max_length=1000, default='')
    active = models.CharField(max_length=5, default='no')
    bookofthemonth = models.CharField(max_length=5, default='no')
    vote = models.IntegerField(default=0)
    
    def __str__(self):
        return self.bookname



class UserVote(models.Model):
    loggeduser = models.ForeignKey(User)
    book = models.ForeignKey(BookReview)
    comment = models.CharField(max_length=100, default='')
    dateposted = models.DateTimeField(auto_now_add=True)


    class Meta:
        unique_together = ('loggeduser', 'book')

    def __str__(self):
        return self.book.bookname