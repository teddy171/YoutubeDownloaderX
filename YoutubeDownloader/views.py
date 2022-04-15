from importlib.resources import contents
from importlib.util import resolve_name
from django.shortcuts import render, redirect
import youtube_dl
from django.http import HttpResponse
import datetime


from .videoprocess import download_video
from .models import Task
from .forms import TaskForm

def index(request):
    """The home page for YoutubeDownloadX."""
    return render(request, 'YoutubeDownloader/index.html')
def task(request):
    """Show a single task"""
    task = Task.objects.all()
    context = {'task': task}
    return render(request, 'YoutubeDownloader/task.html', context)
def new_task(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TaskForm()
    else:
        # POST data submitted; process data.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('YoutubeDownloader:task')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'YoutubeDownloader/new_task.html', context)
def download_task(request):
    task = Task.objects.first()
    download_video([str(task)])
    return render(request, 'YoutubeDownloader/download_video.html')