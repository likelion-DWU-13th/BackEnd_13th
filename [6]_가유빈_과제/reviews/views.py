from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewModelForm, CommentForm
from .models import Review, Comment
from movies.models import Bookmark
from django.core.paginator import Paginator

#리뷰 목록 조회
def reviews(request):
    reviews = Review.objects.all().order_by('-created_at')
    my_paginator = Paginator(reviews, 5)
    page_num = request.GET.get('page')
    reviews = my_paginator.get_page(page_num)

    if request.user.is_authenticated:
        bookmarked_ids = Bookmark.objects.filter(user=request.user).values_list('review_id', flat=True)
        for review in reviews:
            review.is_bookmarked = review.id in bookmarked_ids
    else:
        for review in reviews:
            review.is_bookmarked = False
            
    return render(request, 'products.html', {'reviews': reviews})

#리뷰 생성
def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = ReviewModelForm(request.POST, request.FILES)
        if form.is_valid():
            #form.save()
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('reviews')
    else:
        form = ReviewModelForm()
    return render(request, 'form_create.html', {'form': form})

#리뷰 상세
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    comment_form = CommentForm()
    context = {
        'review': review,
        'comment_form': comment_form
    }
    return render(request, 'review_detail.html', context)

#리뷰 수정
def review_update(request, id):
    review = get_object_or_404(Review, pk=id)

    if request.method == 'POST' or request.method == 'FILES':
        form = ReviewModelForm(request.POST, request.FILES, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', review_id=review.id)
    else:
        form = ReviewModelForm(instance=review)
        return render(request, 'form_create.html', {'form':form, 'id':id})

#리뷰 삭제
def review_delete(request, id):
    review = Review.objects.get(pk=id)
    review.delete()
    return redirect('reviews')

#댓글 생성
def create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Review, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('review_detail', id)

#댓글 수정
def update_comment(request, review_id, com_id):
    comment = Comment.objects.get(id=com_id)

    if request.method == 'POST':
        updated_form = CommentForm(request.POST, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('review_detail', review_id)
    else:
        comment_form = CommentForm(instance=comment)
        context = {'comment_form': comment_form}
        return render(request, 'comment_update.html', context)

#댓글 삭제
def delete_comment(request, review_id, com_id):
    comment = Comment.objects.get(id=com_id)
    comment.delete()
    return redirect('review_detail', review_id)

#좋아요
def likes(request, review_id):
    if request.user.is_authenticated: #로그인한 유저인지 확인
        review = get_object_or_404(Review, pk=review_id)

        if review.like_users.filter(pk=request.user.pk).exists(): #좋아요 했는지 확인
            review.like_users.remove(request.user) #했으면 삭제
        else:
            review.like_users.add(request.user) #아니면 추가
        return redirect('review_detail', review_id)
    return redirect('accounts:login')