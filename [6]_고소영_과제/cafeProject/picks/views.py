from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostPickModelForm, CommentForm
from .models import PostPick, PickComment
from django.core.paginator import Paginator

# Create your views here.
def pick(request):
    return render(request, "pick.html")

#pick 게시물 쓰기
def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostPickModelForm(request.POST, request.FILES)
        if form.is_valid():
            # form.save()
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('picks')
    else:
        form = PostPickModelForm()
    return render(request, 'form_create_pick.html', {'form':form})

#pick 게시글 목록 조회
def pick_list(request):
    picks = PostPick.objects.all().order_by('-created_at')
    my_paginator = Paginator(picks, 4)
    page_num = request.GET.get('page')
    picks = my_paginator.get_page(page_num)
    return render(request, "pick_list.html", {"picks":picks})

#pick 상세 페이지 조회
def pick_detail(request, id):
    pick = get_object_or_404(PostPick, pk=id)
    comment_form = CommentForm()
    context = {
        'pick' : pick,
        'comment_form': comment_form
    }
    return render(request, "pick_detail.html", context)

#pick 게시글 수정
def pick_update(request, id):
    pick = get_object_or_404(PostPick, pk=id)

    if request.method == 'POST' or request.method == 'FILES':
        form = PostPickModelForm(request.POST, request.FILES, instance=pick)
        if form.is_valid():
            form.save()
            return redirect('pick_list')
    else:
        form = PostPickModelForm(instance=pick)
        return render(request, 'form_create_pick.html', {'form':form, 'id':id})

#pick 게시글 삭제
def pick_delete(request, id):
    pick = PostPick.objects.get(pk=id)
    pick.delete()
    return redirect('pick_list')


# 댓글 쓰기
def create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(PostPick, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('pick_detail', id)

#댓글 수정
def update_comment(request, pick_id, com_id):
    comment = PickComment.objects.get(id=com_id)

    if request.method == 'POST':
        updated_form = CommentForm(request.POST, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('pick_detail', pick_id)
    else:
        comment_form = CommentForm(instance=comment)
        context = {'comment_form' : comment_form}
        return render(request, 'comment_update.html', context)


#댓글 삭제
def delete_comment(request, pick_id, com_id):
    comment = PickComment.objects.get(id=com_id)
    comment.delete()
    return redirect('pick_detail', pick_id)

#좋아요
def pick_like(request, id):
    pick = get_object_or_404(PostPick, pk=id)
    if request.user in pick.likes.all():
        pick.likes.remove(request.user)
    else:
        pick.likes.add(request.user)
    return redirect('pick_detail', id=id)