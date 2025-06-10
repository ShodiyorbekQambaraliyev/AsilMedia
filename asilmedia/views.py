from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def videoPage(request):
    return render(request, 'video_page.html')