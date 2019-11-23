from django import forms
from .models import BookReview, UserVote


class UserCommentForm(forms.ModelForm):

    class Meta:
        model = UserVote
        fields = ('book', 'comment')

