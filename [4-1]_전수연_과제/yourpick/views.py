from django.shortcuts import render, redirect, get_object_or_404
from home.models import Post
from home.forms import PostModelForm

# def yourPick(request):
#     return render(request, 'yourpick.html')

def yourpick_list(request):
    yourPicks = Post.objects.all().order_by('-created_at')
    return render(request, "yourpick.html", {"yourPicks": yourPicks})

def yourpick_detail(request, yourpick_id):
    yourPick = get_object_or_404(Post, pk=yourpick_id)
    return render(request, "yourpick_detail.html", {"yourPick": yourPick})

def yourpick_update(request, id):
    yourpick = get_object_or_404(Post, pk=id)

    if request.method =='POST':
        form = PostModelForm(request.POST, instance=yourpick)
        if form.is_valid():
            form.save()
            return redirect('yourpick_detail', yourpick_id = id)
    else:
        form = PostModelForm(instance=yourpick)
        return render(request, 'form_pick.html', {'form':form, 'id':id})

def yourpick_delete(request, id):
    yourpick = Post.objects.get(pk=id)
    yourpick.delete()
    return redirect('yourpick_list')