from django.shortcuts import render, redirect
from .forms import PostSkipModelForm

# Create your views here.
def skip(request):
    return render(request, "skip.html")

def create(request):
    if request.method == 'POST':
        form = PostSkipModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('skips')
    else:
        form = PostSkipModelForm()
    return render(request, 'form_create_skip.html', {'form': form})