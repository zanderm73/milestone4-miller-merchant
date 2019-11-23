from django.contrib import admin
from .models import BookReview, UserVote

# Register your models here.
admin.site.register(BookReview)
admin.site.register(UserVote)