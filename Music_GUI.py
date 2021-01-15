from tkinter import *
from tkinter import filedialog, font, messagebox, ttk

class Music:
    def windowInit(self):
        self.root=Tk()
        self.root.title("Music Player")
        self.root.geometry("600x540+200+20")
        self.root.resizable(True,True) #control window size
        
        #font
        highlightFont = font.Font(family="Helvetica", name="appHighlightFont", size=12, weight="bold")
        lightFont=font.Font(family="Helvetica", name="applightFont", size=10, weight="normal")
         #image
        image=PhotoImage(file="image.gif")
        image_label=ttk.Label(self.root,image=image)
        image_label.grid(row=0,column=1,columnspan=2)
        
        label1=ttk.Label(self.root,text="Playing",font=highlightFont)
        label1.grid(row=1,column=1,columnspan=2)
        self.playing=StringVar(self.root,value="null")
        label2=ttk.Label(self.root,text="",textvariable=self.playing,wraplength=200,font=highlightFont,background="white")
        label2.grid(row=2,column=1,columnspan=2,ipadx=60)
        label3=ttk.Label(self.root,text="Play List",font=highlightFont)
        label3.grid(row=3,column=1,columnspan=2)
        label4=ttk.Label(self.root,text="There is no music file in Play List, please add",font=lightFont)
        label4.grid(row=4,column=1,columnspan=2,padx=10,pady=5)
       
        self.box=ttk.Entry(self.root,show=None)
        self.box.grid(row=5,column=1,ipadx=60)

        self.buttomInit()
        self.menuInit()
        self.root.mainloop()
    
    def windowClose(self):
        self.root.destroy()
    
    def buttomInit(self):
        #add
        self.bAdd=ttk.Button(self.root,text="Add",width=7)
        self.bAdd.grid(row=0, column=0, padx=10, pady=5)
        self.bAdd["state"]="normal"
        
        #play
        self.flag=StringVar(self.root,value="Play")
        self.bPlay=ttk.Button(self.root,textvariable=self.flag,width=7)
        self.bPlay.grid(row=1,column=0,padx=10, pady=5)
        self.bPlay["state"]="disable"
        
        #stop
        self.bStop=ttk.Button(self.root,text="Stop",width=7)
        self.bStop.grid(row=2,column=0,padx=10, pady=5)
        self.bStop["state"]="disable"
        
        #next
        self.bNext=ttk.Button(self.root,text="Next",width=7)
        self.bNext.grid(row=3,column=0,padx=10, pady=5)
        self.bNext["state"]="disable"

        #Last
        self.bLast=ttk.Button(self.root,text="Last",width=7)
        self.bLast.grid(row=4,column=0,padx=10, pady=5)
        self.bLast["state"]="disable"

        #volume adjust
        scale=ttk.Scale(self.root,orient=HORIZONTAL,from_=0,to=100,length=200)
        scale.grid(row=5,column=0,padx=10, pady=5)
        
        #path
        self.bPath=ttk.Button(self.root,text="Add path",width=10)
        self.bPath.grid(row=5,column=2,padx=10, pady=5)
        self.bPath["state"]="normal"

    def menuInit(self):
        my_menu=Menu(self.root)
        
        file_menu=Menu(my_menu,tearoff=0)
        file_menu.add_command(label="Open File")
        file_menu.add_command(label="Open Folder")
        file_menu.add_command(label="Clear Play List")
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.windowClose)

        action_menu=Menu(my_menu,tearoff=0)
        action_menu.add_command(label="Pause/Continue")
        action_menu.add_command(label="Stop")
        action_menu.add_command(label="Next")
        action_menu.add_command(label="Last")
        

        my_menu.add_cascade(label="File",menu=file_menu)
        my_menu.add_cascade(label="Control",menu=action_menu)
        my_menu.add_cascade(label="About",command=self.About)
        
        self.root.config(menu=my_menu)
    
    def About(self):
        print(messagebox.showinfo(title="message",\
            message="Author:何沛霖\nStudentID:1809853U-I011-0078"))

music=Music()
music.windowInit()
