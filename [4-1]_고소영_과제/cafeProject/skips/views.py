from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostSkipModelForm
from .models import PostSkip

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

def skip_list(request):
    skips = PostSkip.objects.all().order_by('-created_at')
    return render(request, "skip_list.html", {"skips":skips})

def skip_detail(request, id):
    skip = get_object_or_404(PostSkip, pk=id)
    return render(request, "skip_detail.html", {"skip": skip})

def skip_update(request, id):
    skip = get_object_or_404(PostSkip, pk=id)

    if request.method == 'POST':
        form = PostSkipModelForm(request.POST, instance=skip)
        if form.is_valid():
            form.save()
            return redirect('skip_list')
    else:
        form = PostSkipModelForm(instance=skip)
        return render(request, "form_create_skip.html", {"form":form, "id":id})

def skip_delete(request, id):
    skip = PostSkip.objects.get(pk=id)
    skip.delete()
    return redirect('skip_list')