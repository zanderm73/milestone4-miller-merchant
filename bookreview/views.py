from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .models import BookReview, UserVote
from .forms import UserCommentForm
from django.db import IntegrityError

# Create your views here.
def review_landing(request):
    reviewlanding = BookReview.objects.all()
    return render(request, "landingbookreview.html", {"reviewlanding": reviewlanding})


def each_book_review(request):
    bookreview = BookReview.objects.all()
    return render(request, "bookreview.html", {"bookreview": bookreview})


@login_required()
def view_votes(request):
    viewvote = UserVote.objects.all()
    bookreview = BookReview.objects.all()
    return render(request, "viewvotes.html", {"viewvote": viewvote, "bookreview": bookreview})

@login_required()
def book_vote(request):
    comment_form = UserCommentForm(request.POST or None)
    bookreview = BookReview.objects.all()
    if comment_form.is_valid():
        bookvote = comment_form.save(commit=False)
        bookvote.loggeduser = request.user
        try:
            bookvote.save()
            messages.success(request, "You have voted")
        except IntegrityError:
            messages.error(request, "You have already voted this month")
    return render(request, "bookvote.html", {"comment_form": comment_form, "bookreview": bookreview})
