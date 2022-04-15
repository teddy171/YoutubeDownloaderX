from django.urls import path

from . import views

app_name = 'YoutubeDownloader'
urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    path('task/', views.task, name='task'),
    path('new_task/', views.new_task, name='new_task'),
    path('download_task/', views.download_task, name='download_task')
]