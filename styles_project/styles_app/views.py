from django.shortcuts import render

def home(request):
    return render(request, 'styles_app/home.html')

def about(request):
    return render(request, 'styles_app/about.html')    
