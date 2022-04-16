import os
from importlib.resources import contents
from importlib.util import resolve_name
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


from .videoprocess import download_video
from .models import Task
from .forms import TaskForm

@login_required
def index(request):
    """The home page for YoutubeDownloadX."""
    return render(request, 'YoutubeDownloader/index.html')

@login_required
def task(request):
    """Show a single task"""
    task = Task.objects.filter(owner=request.user)
    context = {'task': task}
    return render(request, 'YoutubeDownloader/task.html', context)

@login_required
def new_task(request):
    """Add a new topic."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TaskForm()
    else:
        # POST data submitted; process data.
        form = TaskForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.owner = request.user
            new_task.save()
            return redirect('YoutubeDownloader:task')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'YoutubeDownloader/new_task.html', context)

@login_required
def download_task(request):
    tasks = Task.objects.filter(owner=request.user)
    if not os.path.exists(f"data/{request.user}/"):
        os.mkdir(f"data/{request.user}/")
    if len(tasks) == 0:
        return redirect('YoutubeDownloader:task')
    download_video([str(task) for task in tasks], f"{request.user}", Task.objects.first().email)
    tasks.delete()
    return render(request, 'YoutubeDownloader/download_video.html')