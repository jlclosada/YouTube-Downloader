from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox


def download():
    link = videos.get()
    video = YouTube(link)
    download = video.streams.get_highest_resolution()
    download.download(output_path="D:\Descargas")


def popup():
    MessageBox.showinfo("About me", "Software Engineer, Spain.")


root = Tk()
root.config(bd=15)
root.title("YouTube downloader")

imagen = PhotoImage(file="logo.png")
foto = Label(root, image=imagen, bd=0)
foto.grid(row=0, column=0)

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)


menubar.add_cascade(label="Sobre este programa", menu=helpmenu)
helpmenu.add_cascade(label="Información del autor", command=popup)

menubar.add_cascade(label="Salir", command=root.destroy)

instructions = Label(root, text="Bienvenido al YouTube downloader de Joss")
instructions.config(font=("Courier", 23, "bold"))
instructions.grid(row=0, column=1)

videos = Entry(root, width=90)
videos.grid(row=1, column=1)

boton = Button(root, text="Download", command=download)
boton.grid(row=2, column=1)

root.mainloop()


label = "Hola"
