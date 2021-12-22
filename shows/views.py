from django.shortcuts import render

from .models import Shows

def shows(request):
    shows = Shows.objects.all()
    context = {
      'shows': shows
    }
    return render(request, 'shows/shows.html', context )

