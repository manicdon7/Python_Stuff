import os
from pytube import YouTube, exceptions
from time import time
from tkinter import *
from customtkinter import *

set_appearance_mode("System")
set_default_color_theme("blue")
for i in os.listdir(os.getcwd()):
    if i  == "youtube_downloads":
        break
    
else:
    os.mkdir("youtube_downloads")
        
def download_video(entry_field):
    try:
        start_time = time()
        download_location = "youtube_downloads/"
        YouTube(entry_field).streams.first().download(download_location)
        end_time = time()
        
        popup = CTk()
        popup.title = ("Downlader status")
        popup.resizable(False,False)
        popup.geometry("200x100")
        popup.columnconfigure(0,weight=1)
        popup.rowconfigure((0,1),weight=1)
        msg = StringVar()
        msg.set(f"Download successful!\n Total time taken {round(end_time-start_time,3)}seconds")
        label = CTkLabel(popup, text=msg.get())
        label.grid(row=0, column=0)
        button = CTkButton(popup, text="OK", command=popup.destroy)
        button.grid(row=1,column=0)
        popup.mainloop()
    except exceptions.RegexMatchError:
        error = CTk()
        error.title("Error")
        error.resizable(False,False)
        error.geometry("300x100")
        error.rowconfigure((0,1),weight=1)
        error.columnconfigure(0,weight=1)
        error_label = CTkLabel(error,text="Please enter a valid youtube link")
        error_label.grid(row=0,column=1)
        button = CTkButton(error,text="OK",command=error.destroy)
        button.grid(row=1,column=0)
        error.mainloop()
        
master = CTk()
master.title("Youtube Downloader")
master.grid_rowconfigure((0,1),weight=1)
master.grid_columnconfigure((0,1),weight=1)
master.geometry("300x150")
master.resizable(False,False)
CTkLabel(master,text="Enter a Youtube Link to Download:").grid(row=0,column=0)
entry = CTkEntry(master)
entry.grid(row=0,column=1)
CTkButton(master, text="Download",command=lambda *args: download_video(entry.get())).grid(row=1,column=0,columnspan=2)
master.mainloop()


