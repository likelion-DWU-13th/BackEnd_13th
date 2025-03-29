from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostPickModelForm
from .models import PostPick

# Create your views here.
def pick(request):
    return render(request, "pick.html")

#pick 게시물 쓰기
def create(request):
    if request.method == 'POST':
        form = PostPickModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('picks')
    else:
        form = PostPickModelForm()
    return render(request, 'form_create_pick.html', {'form':form})

#pick 게시글 목록 조회
def pick_list(request):
    picks = PostPick.objects.all().order_by('-created_at')
    return render(request, "pick_list.html", {"picks":picks})

#pick 상세 페이지 조회
def pick_detail(request, id):
    pick = get_object_or_404(PostPick, pk=id)
    return render(request, "pick_detail.html", {"pick":pick})

#pick 게시글 수정
def pick_update(request, id):
    pick = get_object_or_404(PostPick, pk=id)

    if request.method == 'POST':
        form = PostPickModelForm(request.POST, instance=pick)
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
