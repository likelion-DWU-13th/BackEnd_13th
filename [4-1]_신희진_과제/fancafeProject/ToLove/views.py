from django.shortcuts import render, redirect,  get_object_or_404
from cafeMain.models import Post
from cafeMain.forms import PostModelForm

def toL(request):
    return render(request, "ToL.html")

def toL_list(request):
    letters = Post.objects.all().order_by('-created_at')
    return render(request, "toL_list.html", {"letters" : letters})

def toL_detail(request, letter_id):
    letter = get_object_or_404(Post, pk = letter_id)
    return render(request, "toL_detail.html", {"letter" : letter})

def toL_update(request, id):
    letter = get_object_or_404(Post, pk = id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance = letter)
        if form.is_valid():
            form.save()
            return redirect('toL_list')
    else:
        form = PostModelForm(instance = letter)
        return render(request, 'form_create.html', {'form' : form, 'id' : id})
    
def toL_delete(request, id):
    letter = Post.objects.get(pk = id)
    letter.delete()
    return redirect('toL_list')