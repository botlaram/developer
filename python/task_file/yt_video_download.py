from tkinter import *
from pytube import YouTube

# def Download(link):
#     youtubeObject = YouTube(link)
#     youtubeObject = youtubeObject.streams.get_highest_resolution()
#     try:
#         youtubeObject.download()
#     except:
#         print("An error has occurred")
#     print("Download is completed successfully")


# link = input("Enter the YouTube video URL: ")
# Download(link)


############### using tkinter #############

##Create Display Window
root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("youtube video downloader")

# Tk() used to initialize tkinter to create display window
# geometry() used to set the window’s width and height
# resizable(0,0) set the fix size of window
# title() used to give the title of window


Label(root,text = 'Youtube Video Downloader', font ='arial 20 bold').pack()
# Label() widget use to display text that users can’t able to modify.
# root is the name of the window
# text which we display the title of the label
# font in which our text is written
# pack organized widget in block

##Create Field to Enter Link
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

# link is a string type variable that stores the youtube video link that the user enters.
# Entry() widget is used when we want to create an input text field.
# width sets the width of entry widget
# textvariable used to retrieve the value of current text variable to the entry widget
# place() use to place the widget at a specific position

## Create Function to Start Downloading
def Downloader():     
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

# Button() widget used to display button on the window.
# 
# text which we display on the label
# font in which the text is written
# bg sets the background color
# command is used to call the function
# root.mainloop() is a method that executes when we want to run the program.


root.mainloop()

