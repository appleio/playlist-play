from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms

playlist = []

class NewFormPlaylist(forms.Form):
    playlist = forms.CharField(label="Playlist Name")

def index(request):
    return render(request, "home/index.html", {
        "playlist": playlist
    })

def add(request):
    if request.method == "POST":
        form = NewFormPlaylist(request.POST)
        if form.is_valid():
            playlist.append(form.cleaned_data["playlist"])
            return HttpResponseRedirect("/")
        else:
            return render(request, "home/index.html",{
                "playlist" : form
            })

    return render(request, "home/add.html",{
        "playlist" : NewFormPlaylist()
    })

def remove(request):
    return render(request, "home/remove.html" , {
        "playlists": playlist
    })