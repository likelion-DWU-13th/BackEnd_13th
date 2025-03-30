from django.shortcuts import render

def myPick(request):
    return render(request, 'mypick.html')
