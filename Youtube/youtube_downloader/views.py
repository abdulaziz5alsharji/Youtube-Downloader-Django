from django.shortcuts import render
from pytube import YouTube
from django.http import HttpResponseRedirect
# Create your views here.

def download(request):
    if request.method == "POST":
        youtube_url = request.POST.get("url")
        quality = request.POST.get("quality")
        if youtube_url is not None and quality is not None:
            youtube = YouTube(youtube_url)
            download_link = ""
            if quality == "high":
                download_link = youtube.streams.get_highest_resolution().url
            else:
                download_link = youtube.streams.get_lowest_resolution().url
            return HttpResponseRedirect(download_link)
        else:
            return render(request, "youtube_downloader/download.html", context={

            })
    return render(request, "youtube_downloader/download.html", context={

    })