from django.shortcuts import render, get_object_or_404

from .models import Show

def shows(request):
    shows = Show.objects.all()
    context = {
      'shows': shows
    }
    return render(request, 'shows/shows.html', context )


def show(request, show_id):
  show = get_object_or_404(Show, pk=show_id)
  context = {
    'show': show
  }
  return render(request, 'shows/show.html', context)
