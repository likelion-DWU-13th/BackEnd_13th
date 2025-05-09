from django.shortcuts import render, redirect
from .forms import letterModelForm

def home(request):
    return render(request, "index.html")

def create(request):
    if request.method == 'POST' or request.method == 'FILES':  # POST 요청만 처리
        form = letterModelForm(request.POST, request.FILES)  # 파일 포함된 요청 처리
        if form.is_valid():
            unfinished_form = form.save(commit=False)
            unfinished_form.author = request.user
            unfinished_form.save()
            return redirect('home')  # 성공 시 홈 페이지로 리디렉션
    else:
        form = letterModelForm()  # GET 요청 시 빈 폼 생성
    return render(request, 'form_create.html', {'form': form})
