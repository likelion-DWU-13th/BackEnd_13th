from django.shortcuts import render, redirect
from .forms import MusicModelForm

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