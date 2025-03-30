from django.shortcuts import render
from cafeMain.models import Post

def toL(request):
    return render(request, "ToL.html")

def toL_list(request):
    letters = Post.objects.all().order_by('-created_at')
    return render(request, "toL_list.html", {"letters" : letters})