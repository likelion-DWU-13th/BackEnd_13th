from django.shortcuts import render, redirect, get_object_or_404
from .forms import NoteModelForm, CommentModelFrom
from .models import Note, Comment
from django.core.paginator import Paginator
from django.contrib.auth.models import User

#게시글 작성
def create(request):
    if request.method == 'POST' or request.method == 'FILES': 
        form = NoteModelForm(request.POST, request.FILES)
        if form.is_valid():
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('list') 
    else:
        form = NoteModelForm()
    return render(request, 'create.html', {'form':form})

# 게시글 목록 보기
def list(request):
    notes = Note.objects.all().order_by('-created_at')
    my_pagenator = Paginator(notes, 5)
    page_num = request.GET.get('page')
    notes = my_pagenator.get_page(page_num)
    return render(request, "list.html", {'notes': notes})

# 게시글 자세히 보기 
def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    comment_form = CommentModelFrom()
    context = {
        'note':note,
        'comment_form':comment_form
    }
    return render(request, "detail.html", context)

# 게시글 수정하기
def update(request, id):
    note = get_object_or_404(Note, pk=id)
    if request.method == 'POST' or request.method == 'FILES':
        form = NoteModelForm(request.POST, request.FILES, instance=note)
        if form.is_valid():
            form.save()
            return redirect('detail', id) #id=note.id 수정
    else:
        form = NoteModelForm(instance=note)
    return render(request, 'create.html', {'form':form, 'id':id})

# 게시글 삭제하기
def delete(request, id):
    note = get_object_or_404(Note, pk=id)
    note.delete()
    return redirect('list')

#댓글 작성하기 
def comment_create(request, id):
    filled_form = CommentModelFrom(request.POST, request.FILES)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.note = get_object_or_404(Note, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('detail', id)

#댓글 수정하기
def comment_update(request, note_id, com_id):
    comment = Comment.objects.get(id=com_id)

    if request.method == 'POST':
        updated_form = CommentModelFrom(request.POST, request.FILES, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('detail', note_id)
    else:
        comment_form = CommentModelFrom(instance=comment)
        context={'comment_form':comment_form}
        return render(request, 'comment_update.html', context)

#댓글 삭제하기
def comment_delete(request, note_id, com_id):
    comment = Comment.objects.get(id=com_id)
    comment.delete()
    return redirect('detail', note_id)

# 게시글 추천 누르기
def note_likes(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, pk=note_id)
        if note.like_users.filter(pk=request.user.pk).exists():
            note.like_users.remove(request.user)
        else:
            note.like_users.add(request.user)
        return redirect('detail', note_id)
    return redirect('accounts:login')

# 댓글 추천 누르기
def comment_likes(request, com_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=com_id)
        if comment.like_users.filter(pk=request.user.pk).exists():
            comment.like_users.remove(request.user)
        else:
            comment.like_users.add(request.user)
        return redirect('detail', note_id=comment.note.id)
    return redirect('accounts:login')

# 게시글 스크랩 하기
def scraps(request, note_id):
    if request.user.is_authenticated:
        note = get_object_or_404(Note, pk=note_id)
        if note.scrap_users.filter(pk=request.user.pk).exists():
            note.scrap_users.remove(request.user)
        else:
            note.scrap_users.add(request.user)
        return redirect('detail', note_id)
    return redirect('accounts:login')