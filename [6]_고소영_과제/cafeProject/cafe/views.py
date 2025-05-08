from django.shortcuts import render
from picks.models import PostPick
from skips.models import PostSkip

# Create your views here.
def home(request):
    return render(request, "index.html")

def liked_posts(request):
    user = request.user
    liked_picks = PostPick.objects.filter(likes=user)
    liked_skips = PostSkip.objects.filter(likes=user)

    return render(request, 'liked_posts.html', {'liked_picks':liked_picks, 'liked_skips': liked_skips})