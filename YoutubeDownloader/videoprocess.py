from __future__ import unicode_literals
from concurrent import futures
import youtube_dl
import os
import json

from .autoMail import send_email
def send_video(filename, email):
    with open(filename,'rb') as f:
        content = f.read()
    proress = str(int.from_bytes(content, byteorder='big', signed=False))
    while True:
        try:
            send_email(filename.split('/')[-1], proress, email)
        except:
            pass
        else:
            print("Already send the mail.")
            os.remove(filename)
def download_video(content, location, email):
    ydl_opts = {"writeinfojson": True, "outtmpl":f"data/{location}/%(title)s.%(ext)s"}
    while True:
        try:
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download(content)
        except:
            pass
        else:
            break
    files = os.listdir(f"data/{location}/")
    info_files = []
    video_names = []
    for file in files:
        element = file.split('.')
        if(element[-1] == 'json' and element[-2] == "info"):
            info_files.append(file)
    for info_file in info_files:
        with open(f"data/{location}/{info_file}") as f:
            info = json.load(f)
            video_name = info["_filename"]
            video_names.append(video_name)
            with open(video_name, 'rb') as video:  
                n = 0
                file_names = []
                while True:
                    block = video.read(1048576)
                    if not block:
                        break
                    with open(f"{video_name}.{n}",'xb') as f:
                        f.write(block)
                        file_names.append(f"{video_name}.{n}")
                    n+=1
                with futures.ProcessPoolExecutor() as executor:
                    res = executor.map(send_video, file_names, email)
            os.remove(video_name)
        os.remove(f"data/{location}/{info_file}")    

    return video_names


     
                    
