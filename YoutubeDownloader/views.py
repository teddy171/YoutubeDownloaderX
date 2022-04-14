from django.shortcuts import render

def index(request):
    """The home page for YoutubeDownload."""
    return render(request, 'YoutubeDownloader/index.html')
