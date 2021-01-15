from tkinter import *
from tkinter import ttk

# __init__(level=NOTSET)

root=Tk()
root.title("Music Player")

mainframe = ttk.Frame(root, width=100,height=100)
mainframe.grid(column=0,row=0,columnspan=2)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


my_image=PhotoImage(file="image.gif")
image_label=ttk.Label(mainframe,image=my_image)
image_label.grid(row=0,column=0,columnspan=2)


l = ttk.Label(mainframe, background="green",  width=20, text="empty")
l.grid(column=1,row=1,columnspan=2)
 

def print_selection(v):
    l.config(text="you have selected " + v)

s = ttk.Scale(mainframe,from_=0, to=10, length=200, orient=HORIZONTAL, command=print_selection)
s.grid(column=1,row=1,columnspan=2)

buttom1=ttk.Button(mainframe)
buttom2=ttk.Button(mainframe)
buttom3=ttk.Button(mainframe)

music_word=ttk.Entry(mainframe)
language=StringVar()
English=ttk.Radiobutton(mainframe,text="English",variable=language,value="English")
Chinese=ttk.Radiobutton(mainframe,text="Chinese",variable=language,value="Chinese")




root.mainloop()
