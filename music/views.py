from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from.models import Album


def index(request):
    all_album = Album.objects.all()
    html = ''
    for album in all_album:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="' + url + '">' + album.album_title + '</a><br>'
    return HttpResponse("<h1>This is the music app homepage</h1>")


def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

