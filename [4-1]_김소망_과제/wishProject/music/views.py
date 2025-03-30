from django.shortcuts import render, redirect, get_object_or_404 
from .forms import MusicModelForm
from music.models import Music
from music.forms import MusicModelForm

# Create your views here.
def music(request):
    form = MusicModelForm()  # 빈 폼 생성
    return render(request, "music.html", {"form": form})  # 폼을 전달

def create(request):
    if request.method == 'POST':
        form = MusicModelForm(request.POST)  # 입력된 데이터를 form에 저장
        if form.is_valid():  # 폼이 유효한지 검사
            form.save()  # DB에 저장
            return redirect('home')  # 홈으로 리다이렉트
    else:
        form = MusicModelForm()  # GET 요청일 경우 빈 폼을 전달
    return render(request, 'music.html', {'form': form})

#게시글 목록 조회
def music_list(request):
    musics = Music.objects.all().order_by('-created_at')
    return render(request, "music_list.html", {"musics" : musics})

#게시글 상세페이지 조회
def music_detail(request, music_id):
    music = get_object_or_404(Music, pk=music_id)
    return render(request, "music_detail.html", {"music":music})

#게시글 수정
def music_update(request, id):
    music = get_object_or_404(Music, pk=id)

    if request.method == 'POST':
        form = MusicModelForm(request.POST, instance=music)
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