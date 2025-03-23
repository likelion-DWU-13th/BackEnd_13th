from django.shortcuts import render

def stores(request):
    return render(request, 'store.html')
