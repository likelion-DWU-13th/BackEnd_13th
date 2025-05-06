from django.shortcuts import render, redirect, get_object_or_404 
from ins.models import Page, Comment
from ins.forms import PageModelForm, CommentForm
from django.core.paginator import Paginator

# Create your views here.
def resume(request):
    return render(request, "resume.html")

def feedback_list(request):
    feedbacks = Page.objects.all().order_by('-created_at')
    my_paginator = Paginator(feedbacks, 5)
    page_num = request.GET.get('page')
    feedbacks = my_paginator.get_page(page_num)
    return render(request, "feedback_list.html", {"feedbacks" : feedbacks})

def feedback_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    like = Like.objects.filter(title=page.title).first()  # 또는 다른 조건으로 연결된 Like 객체 찾기
    if like is None:
        like = Like.objects.create(user=request.user, title=page.title, content="")  # 예시로 Like 객체 생성
    comment_form = CommentForm()
    context = {
        'page': page,
        'comment_form': comment_form,
        'like': like,  # Like 객체를 전달
    }
    return render(request, "feedback_detail.html", context)

def feedback_update(request, id):
    page = get_object_or_404(Page, pk=id)

    if request.method == 'POST' or request.method == 'FILES':
        form = PageModelForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:   
        form = PageModelForm(instance=page)
        return render(request, 'form_create.html', {'form':form, 'id':id})
    
def feedback_delete(request, id):
    page = Page.objects.get(pk=id)
    page.delete()
    return redirect('feedback_list')

def create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Page, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('feedback_detail', id)

def update_comment(request, page_id, com_id):
    comment = Comment.objects.get(id=com_id)
    
    if request.method == "POST": 
        updated_form = CommentForm(request.POST, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('feedback_detail', page_id)
    else:
        comment_form = CommentForm(instance=comment)
        context = {'comment_form' : comment_form}
        return render(request, 'comment_update.html', context)
    
def delete_comment(request, page_id, com_id):
    comment = Comment.objects.get(id=com_id)
    comment.delete()
    return redirect('feedback_detail', page_id)

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import Like

@login_required
def like_toggle(request, like_id):
    like = get_object_or_404(Like, id=like_id)
    user = request.user

    if user in like.like_users.all():
        like.like_users.remove(user)
    else:
        like.like_users.add(user)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))