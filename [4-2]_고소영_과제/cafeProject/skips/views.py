from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostSkipModelForm, CommentForm
from .models import PostSkip, Comment
from django.core.paginator import Paginator

# Create your views here.
def skip(request):
    return render(request, "skip.html")

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostSkipModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('skips')
    else:
        form = PostSkipModelForm()
    return render(request, 'form_create_skip.html', {'form': form})

def skip_list(request):
    skips = PostSkip.objects.all().order_by('-created_at')
    my_paginator = Paginator(skips, 4)
    page_num = request.GET.get('page')
    skips = my_paginator.get_page(page_num)
    return render(request, "skip_list.html", {"skips":skips})

def skip_detail(request, id):
    skip = get_object_or_404(PostSkip, pk=id)
    comment_form = CommentForm()
    context = {
        'skip': skip,
        'comment_form': comment_form
    }
    return render(request, "skip_detail.html", context)

def skip_update(request, id):
    skip = get_object_or_404(PostSkip, pk=id)

    if request.method == 'POST' or request.method == 'FILES':
        form = PostSkipModelForm(request.POST, request.FILES, instance=skip)
        if form.is_valid():
            form.save()
            return redirect('skip_list')
    else:
        form = PostSkipModelForm(instance=skip)
        return render(request, "form_create_skip.html", {"form":form, "id":id})

def skip_delete(request, id):
    skip = PostSkip.objects.get(pk=id)
    skip.delete()
    return redirect('skip_list')


def skip_create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(PostSkip, pk=id)
        finished_form.save()
    return redirect('skip_detail', id)

def skip_update_comment(request, skip_id, com_id):
    comment = Comment.objects.get(id=com_id)
    
    if request.method == "POST":
        updated_form = CommentForm(request.POST, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('skip_detail', skip_id)
    else:
        comment_form = CommentForm(instance=comment)
        context = {'comment_form' : comment_form}
        return render(request, 'skip_comment_update.html', context)
    
def skip_delete_comment(request, skip_id, com_id):
    comment = Comment.objects.get(id=com_id)
    comment.delete()
    return redirect('skip_detail', skip_id)