from django.shortcuts import render, redirect
from .forms import PostModelForm

def home(request):
    return render(request, 'index.html') 

def recommend(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostModelForm()
    return render(request, 'form_pick.html', {'form': form})
