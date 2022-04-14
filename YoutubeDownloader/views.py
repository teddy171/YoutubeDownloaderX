from importlib.util import resolve_name
from django.shortcuts import render, redirect

from .models import Task
from .forms import TaskForm

def index(request):
    """The home page for YoutubeDownloadX."""
    return render(request, 'YoutubeDownloader/index.html')
def task(request):
    """Show a single task"""
    task = Task.objects.last
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
            Task.objects.all().delete()
            form.save()
            return redirect('YoutubeDownloader:task')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'YoutubeDownloader/new_task.html', context)