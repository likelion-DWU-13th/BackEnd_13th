from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactMessage
from .forms import ContactModelForm

def contact(request):
    form = ContactModelForm()
    return render(request, "contact.html", {'form':form })

# 폼 
def submitContact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactModelForm()
    
    return render(request, 'contact.html', {'form':form } )

# 연락 리스트
def contact_list(request):
    contacts = ContactMessage.objects.all().order_by('-created_at')
    return render(request, "contact_list.html", {"contacts":contacts})

# contact 상세 페이지
def contact_detail(request, id):
    contact = get_object_or_404(ContactMessage, pk=id)
    return render(request, "contact_detail.html", {"contact":contact})

# contact 수정
def contact_edit(request, id):
    contact = get_object_or_404(ContactMessage, pk=id)
    
    if request.method == 'POST':
        form = ContactModelForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()  
            return redirect('contact_list')  
    else:
        form = ContactModelForm(instance=contact)
    
    return render(request, 'contact.html', {'form': form, 'id': id})
    
# contact 삭제
def contact_delete(request, id):
    contact = ContactMessage.objects.get(pk=id)
    contact.delete()
    return redirect('contact_list')