from django.shortcuts import render, redirect
from .forms import ContactModelForm

def home(request):
	return render(request, "index.html")

def submitContact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactModelForm()
    
    return render(request, 'contact.html', {'form':form } )



