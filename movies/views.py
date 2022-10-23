from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 5,
            'title': 'Super Man',
            'year': 2000
        },
        {
            'id': 6,
            'title': 'Spider Man',
            'year': 1999
        },
        {
            'id': 7,
            'title': 'Black Panther',
            'year': 1990
        }
    ]
    }

def movies(request):
    return render(request, 'movies/movies.html', data)

def home(request):
    return HttpResponse("Homepage!")