from django.shortcuts import render, redirect, get_object_or_404 
from .forms import MusicModelForm
from music.models import Music, Comment
from music.forms import MusicModelForm, CommentForm
from django.core.paginator import Paginator


# Create your views here.
def music(request):
    form = MusicModelForm()  # 빈 폼 생성
    return render(request, "music.html", {"form": form})  # 폼을 전달

def create(request):
    if request.method == 'POST' or request.method == 'FILES': 
        form = MusicModelForm(request.POST, request.FILES)   # 입력된 데이터를 form에 저장
        if form.is_valid():  # 폼이 유효한지 검사
            #form.save()  # DB에 저장
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('home')  # 홈으로 리다이렉트
    else:
        form = MusicModelForm()  # GET 요청일 경우 빈 폼을 전달
    return render(request, 'music.html', {'form': form})

#게시글 목록 조회
def music_list(request):
    musics = Music.objects.all().order_by('-created_at')
    my_paginator = Paginator(musics, 5)
    page_num = request.GET.get('page')
    musics = my_paginator.get_page(page_num)
    return render(request, "music_list.html", {"musics" : musics})

#게시글 상세페이지 조회
def music_detail(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    comment_form = CommentForm()
    context = {
        'music': music,#'post': post,
        'comment_form': comment_form
    }
    return render(request, 'music_detail.html', context)

#게시글 수정
def music_update(request, id):
    music = get_object_or_404(Music, pk=id)

    if request.method == 'POST' or request.method == 'FILES':
        form = MusicModelForm(request.POST, request.FILES, instance=music)
        if form.is_valid():
            form.save()
            return redirect('music_list')
    else:   #GET이면
        form = MusicModelForm(instance=music)
        return render(request, 'music.html', {'form':form, 'id':id})
    
#게시글 삭제
def music_delete(request, id):
    music = Music.objects.get(pk=id)
    music.delete()
    return redirect('music_list')

def create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Music, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('music_detail', id)

def update_comment(request, music_id, com_id):
    comment = Comment.objects.get(id=com_id)
    
    if request.method == "POST": # 사용자가 수정 후 POST 요청을 보냈을 때
        updated_form = CommentForm(request.POST, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('music_detail', music_id)
    else: # GET 요청일 때
        comment_form = CommentForm(instance=comment)
        context = {'comment_form' : comment_form}
        return render(request, 'comment_update.html', context)
    
def delete_comment(request, music_id, com_id):
    comment = Comment.objects.get(id=com_id)
    comment.delete()
    return redirect('music_detail', music_id)