from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html')

def stats(request):
    return render(request, 'stats.html')