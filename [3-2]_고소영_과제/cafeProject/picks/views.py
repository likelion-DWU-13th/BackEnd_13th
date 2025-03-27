from django.shortcuts import render, redirect
from .forms import PostPickModelForm

# Create your views here.
def pick(request):
    return render(request, "pick.html")

def create(request):
    if request.method == 'POST':
        form = PostPickModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('picks')
    else:
        form = PostPickModelForm()
    return render(request, 'form_create_pick.html', {'form':form})