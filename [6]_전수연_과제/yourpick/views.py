from django.shortcuts import render, redirect, get_object_or_404
from home.models import Post, Comment
from home.forms import PostModelForm, CommentForm
from django.core.paginator import Paginator

# def yourPick(request):
#     return render(request, 'yourpick.html')

def yourpick_list(request):
    yourPicks = Post.objects.all().order_by('-created_at')
    pgn = Paginator(yourPicks, 5)
    page_num = request.GET.get('page')
    page_yourPicks = pgn.get_page(page_num)
    return render(request, "yourpick.html", {"yourPicks": page_yourPicks})

def yourpick_detail(request, yourpick_id):
    yourPick = get_object_or_404(Post, pk=yourpick_id)
    comment_form = CommentForm()
    context = {
        'yourPick': yourPick,
        'comment_form': comment_form
    }
    return render(request, "yourpick_detail.html", context)

def yourpick_update(request, id):
    yourpick = get_object_or_404(Post, pk=id)

    if request.method =='POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=yourpick)
        if form.is_valid():
            
            form.save()
            return redirect('yourpick_detail', yourpick_id = id)
    else:
        form = PostModelForm(instance=yourpick)
        return render(request, 'form_pick.html', {'form':form, 'id':id})

def yourpick_delete(request, id):
    yourpick = Post.objects.get(pk=id)
    yourpick.delete()
    return redirect('yourpick_list')

def comment_create(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Post, pk=id)
        finished_form.author = request.user
        finished_form.save()
    return redirect('yourpick_detail', id)

def comment_update(request, yourpick_id, com_id):
    comment = Comment.objects.get(id = com_id)

    if request.method == "POST":
        update_form = CommentForm(request.POST, instance=comment)
        if update_form.is_valid():
            update_form.save()
            return redirect('yourpick_detail', yourpick_id)
    else:
        comment_form = CommentForm(instance=comment)
        context = {'comment_form': comment_form}
        return render(request, 'comment_update.html', context)

def comment_delete(request, yourpick_id, com_id):
    comment = Comment.objects.get(id = com_id)
    comment.delete()
    return redirect('yourpick_detail', yourpick_id)