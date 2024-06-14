from django.shortcuts import render

from django.shortcuts import render

def home(request):
    return render(request, 'templates_app/home.html')

def about(request):
    return render(request, 'templates_app/about.html')
