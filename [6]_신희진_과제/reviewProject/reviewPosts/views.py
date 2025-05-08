from django.shortcuts import render
from reviews.models import Post

def reviewPost(request):
    return render(request, "review_list.html")

def review_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "review_list.html", {"posts":posts})