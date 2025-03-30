from django.shortcuts import render, redirect, get_object_or_404 
from ins.models import Page
from ins.forms import PageModelForm

# Create your views here.
def resume(request):
    return render(request, "resume.html")

def feedback_list(request):
    feedbacks = Page.objects.all().order_by('-created_at')
    return render(request, "feedback_list.html", {"feedbacks" : feedbacks})

def feedback_detail(request, page_id):
    page = get_object_or_404(Page, pk=page_id)
    return render(request, "feedback_detail.html", {"page" : page})

def feedback_update(request, id):
    page = get_object_or_404(Page, pk=id)

    if request.method == 'POST':
        form = PageModelForm(request.POST, instance=page)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:   
        form = PageModelForm(instance=page)
        return render(request, 'form_create.html', {'form':form, 'id':id})
    
def feedback_delete(request, id):
    page = Page.objects.get(pk=id)
    page.delete()
    return redirect('feedback_list')