from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from notes.models import Note

#회원가입
def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['repeat']:
            new_user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            print("가입에 성공했습니다")
            return redirect('home')
    else: 
        return render(request, "signup.html")

#로그인
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['password']
        user = authenticate(request, username=username, password=pwd)
        if user is not None:
            auth_login(request,user)
            print("로그인 성공")
            return redirect('home')
        else:
            error_message = "아이디 또는 비밀번호가 잘못 되었습니다."
            return render(request, 'login.html', {'error_message':error_message})
    else:
        return render(request, 'login.html')

#로그아웃
def logout(request):
    auth_logout(request)
    print("로그아웃 성공")
    return redirect('home')

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def my_scraps(request):
    user = request.user
    scraped_notes = Note.objects.filter(scrap_users=user).order_by('-created_at')
    return render(request, 'list.html', {'notes': scraped_notes})