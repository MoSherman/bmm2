from django.shortcuts import render

from .models import Room

def index(request):
    return render(request, 'template.html')

def museum(request):
    count = Room.objects.all().count()
    context = {
        'count': count,
    }
    return render(request, 'museum.html', context)
