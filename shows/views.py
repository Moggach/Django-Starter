from django.shortcuts import render

from .models import Shows

def shows(request):
    return render(request, 'shows/shows.html')

