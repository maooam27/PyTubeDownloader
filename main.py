from requests import get
from tkinter import *
from PIL import Image, ImageTk
import pytube

root = Tk()
root.title("PyTube Downloader - Lite")
root.geometry("500x300")
root.resizable(False, False)


def gather():
    print("Gathering information")
    url = url_entry.get()
    yt = pytube.YouTube(url)
    title_label.config(text=yt.title)
    author_label.config(text=yt.author)

    thumbnail_url = yt.thumbnail_url
    img = Image.open(thumbnail_url)
    resize_image = img.resize((50, 30))
    img = ImageTk.PhotoImage(resize_image)
    thumbnail.config(image=img)
    thumbnail.image = img


# Title

title = Label(root, text="PyTube Downloader", font=("Arial", 20))
title.pack(pady=10)


# Url zone

url_zone = Frame(root)
url_zone.pack(pady=10)

url_label = Label(url_zone, text="Enter URL: ")
url_label.pack(side=LEFT, padx=10)

url_entry = Entry(url_zone, width=30)
url_entry.pack(side=LEFT)

gather_info = Button(url_zone, text="Gather Info", command=gather)
gather_info.pack(side=LEFT, padx=10)

info_zone = Frame(root)
info_zone.pack(pady=10, fill=X)

img = Image.open("placeholder.png")
resize_image = img.resize((50, 30))
img = ImageTk.PhotoImage(resize_image)

thumbnail = Label(info_zone, text="Thumbnail", image=img)
thumbnail.image = img
thumbnail.pack(side=LEFT, padx=15)

title_label = Label(info_zone, text="Title")
title_label.pack(side=LEFT, padx=15)

author_label = Label(info_zone, text="Author")
author_label.pack(side=BOTTOM, padx=15)

download_button = Button(root, text="Download")
download_button.pack(pady=10)


if __name__ == '__main__':
    root.mainloop()
