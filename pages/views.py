from django.shortcuts import render

shows = [
    {'id': 1, 'name': 'Seinfeld'},
    {'id': 2, 'name': 'The Simpsons'},
    {'id': 3, 'name': 'The Thick of It'},
    {'id': 4, 'name': 'Succession'},
]

# Create your views here.
def index(request):
    return render (request, 'pages/index.html', {'shows': shows})

def about(request):
    return render(request, 'pages/about.html')