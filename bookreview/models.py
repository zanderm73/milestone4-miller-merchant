from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# model that allows book information to be stored on the database by the site admin
class BookReview(models.Model):
    booknamereview = models.CharField(max_length=100, default='')
    bookimage = models.ImageField(upload_to='images', default='')
    bookauthor = models.CharField(max_length=100, default='')
    bookpublisher = models.CharField(max_length=100, default='')
    bookreview = models.CharField(max_length=10000, default='')
    authorscomments = models.CharField(max_length=1000, default='')
    bookofthemonth = models.CharField(max_length=5, default='no')
    monthwinner = models.CharField(max_length=20, default='none')
    
    def __str__(self):
        return self.booknamereview

# model that allows book information to be stored on the database to be used on the voting competition 
class BookChoice(models.Model):
    booknamechoice = models.CharField(max_length=100, default='')
    bookchoiceimage = models.ImageField(upload_to='images', default='')
    bookchoiceauthor = models.CharField(max_length=100, default='')
    bookchoicepublisher = models.CharField(max_length=100, default='')
    authorschoicecomments = models.CharField(max_length=1000, default='')
    vote = models.IntegerField(default=0)
    
    def __str__(self):
        return self.booknamechoice


# model that allows users comments and choice to be stored in the database
class UserVote(models.Model):
    loggeduser = models.ForeignKey(User)
    book = models.ForeignKey(BookChoice)
    comment = models.CharField(max_length=100, default='')
    dateposted = models.DateTimeField(auto_now_add=True)

    # ensures a user can only vote for their preffered choice once
    class Meta:
        unique_together = ('loggeduser', 'book')

    def __str__(self):
        return self.book.booknamechoice