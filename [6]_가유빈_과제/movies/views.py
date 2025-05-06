from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from reviews.models import Review
from .models import Bookmark

# Create your views here.

# def movies(request):
#     return render(request, 'about.html')

#북마크
@login_required
def toggle_bookmark(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    bookmark, created = Bookmark.objects.get_or_create(user=request.user, review=review)
    if not created: #북마크 토글
        bookmark.delete()
    return redirect(request.META.get('HTTP_REFERER', 'review_list'))#보던 페이지로 이동

# 나의 북마크 리뷰
# @login_required
def my_bookmarks(request):
    # 현재 로그인된 사용자가 북마크한 리뷰들만 가져오기
    bookmarks = Bookmark.objects.filter(user=request.user).select_related('review')
    return render(request, 'about.html', {'bookmarks': bookmarks})
