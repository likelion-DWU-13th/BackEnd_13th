from django.shortcuts import render, redirect, get_object_or_404 
from home.models import Post
from home.forms import PostModelForm

# Create your views here.
def blogHome(request):
    return render(request, "blog-home.html")

#게시글 목록 조회
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, "blog-home.html", {"posts" : posts})

#게시글 상세페이지 조회
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post":post})

#게시글 수정
def post_update(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:   #GET이면
        form = PostModelForm(instance=post)
        return render(request, 'form_create.html', {'form':form, 'id':id})

#게시글 삭제
def post_delete(request, id):
    post = Post.objects.get(pk=id)
    post.delete()
    return redirect('post_list')