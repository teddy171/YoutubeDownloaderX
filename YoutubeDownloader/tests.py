from django.test import TestCase
import youtube_dl
# Create your tests here.
from videodownloader import VideoDownloader

a = VideoDownloader("unity")
try:
    a.download_video()
except youtube_dl.utils.DownloadError:
    print("NA")
    print(a.content)
