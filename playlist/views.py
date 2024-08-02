from django.shortcuts import render, redirect
from .models import Bublik


def playlist(request):
    playlist = Bublik.objects.all()
    return render(request, "playlist/playlist.html", {"videos":playlist})

def sosiski(request):
    if request.method == "POST":
        video_title = request.POST["title"]
        video_embed = request.POST["embed"]
        video_description = request.POST["description"]
        Bublik.objects.create(
            title=video_title,
            embed=video_embed,
            description=video_description,
        )
        return redirect ('playlist')
    return render(request, "playlist/sosiski.html")
