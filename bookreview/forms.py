from django import forms
from .models import BookReview, UserVote

# form to allow users to select book and comment on their choice
class UserCommentForm(forms.ModelForm):

    class Meta:
        model = UserVote
        fields = ('book', 'comment')

