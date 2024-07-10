import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytLink = link.get()
        yt = YouTube(ytLink,on_progress_callback=on_progress)
        print(yt.title)
        
        for stream in yt.streams.filter(progressive=True):
            print("resolution: " + stream.resolution)
            print("fps: " + str(stream.fps))
            print("----------------------")

        
        video = yt.streams.get_highest_resolution()
        
        title.configure(text=(yt.title + "\nDownload is started"),text_color = "white")
        finishLabel.configure(text="")
        video.download()
    
        print("Download complete")
        finishLabel.configure(text="Download complete")
    except:
        print("Youtube link in invalid")
        finishLabel.configure(text="Download Error!", text_color="Red")


def on_progress(stream,chunk,bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining   
    percect_completed = (bytes_downloaded/total_size) * 100
    per = str(int(percect_completed))
    pPercent.configure(text=per+"%")
    pPercent.update()
    
    # update progress bar
    progressBar.set(float(percect_completed)/100)
    
# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720X480")
app.title("YouTube downloader")

# adding UI elements
title = customtkinter.CTkLabel(app,text="Insert a youtube link")
title.pack(padx=10,pady=5)

# link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width = 350,height=40,textvariable=url_var)
link.pack(padx=20,pady=10)

# finished downloading
finishLabel = customtkinter.CTkLabel(app,text ="")
finishLabel.pack()

# progress bar
pPercent =customtkinter.CTkLabel(app,text="0%")
pPercent.pack() 

progressBar = customtkinter.CTkProgressBar(app,width=400)
progressBar.set(0)
progressBar.pack(padx=10,pady=10)

# Doenload Button
download = customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(pady=10)

# run app
app.mainloop()