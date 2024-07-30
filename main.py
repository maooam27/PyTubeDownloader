from tkinter import *

root = Tk()
root.title("PyTube Downloader - Lite")
root.geometry("500x300")
root.resizable(False, False)


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

gather_info = Button(url_zone, text="Gather Info")
gather_info.pack(side=LEFT, padx=10)

if __name__ == '__main__':
    root.mainloop()
