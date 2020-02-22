from django.contrib import admin
from .models import BookReview, BookChoice, UserVote

# Register your models here.
admin.site.register(BookReview)
admin.site.register(BookChoice)
admin.site.register(UserVote)