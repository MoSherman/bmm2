from django.shortcuts import render

def index(request):
    return render(request, 'template.html')

def museum(request):
    return render(request, 'museum.html')
