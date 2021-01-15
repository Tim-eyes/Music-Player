# You need python pygame lib
# He Peilin 1809853U-I011-0078
from tkinter import *
#from PIL import Image, ImageTk 
from tkinter import filedialog, font, messagebox, ttk
import os,threading,pygame,time

class Music:
    def __init__(self):
        self.res=[]
        self.num=0
        self.playList=[]
        self.counter=1
        self.isPlaying=False
        
    def windowInit(self):
        self.root=Tk()
        self.root.title("Music Player")
        self.root.geometry("600x540+200+20")
        self.root.resizable(True,True) #control window size
        
        pygame.mixer.init()
        #font
        highlightFont = font.Font(family="Helvetica", name="appHighlightFont", size=12, weight="bold")
        lightFont=font.Font(family="Helvetica", name="applightFont", size=10, weight="normal")
         #image
        image=PhotoImage(file="image.gif")
        image_label=ttk.Label(self.root,image=image)
        image_label.grid(row=0,column=1,columnspan=2)
        
        label1=ttk.Label(self.root,text="Playing",font=highlightFont)
        label1.grid(row=1,column=1,columnspan=2)
        self.playing=StringVar(self.root,value="")
        label2=ttk.Label(self.root,text="",textvariable=self.playing,wraplength=200,font=highlightFont,background="white")
        label2.grid(row=2,column=1,columnspan=2,ipadx=60)
        label3=ttk.Label(self.root,text="Play List",font=highlightFont)
        label3.grid(row=3,column=1,columnspan=2)
        label4=ttk.Label(self.root,text="There is no music file in Play List, please add",font=lightFont)
        label4.grid(row=4,column=1,columnspan=2,padx=10,pady=5)

        self.box=ttk.Entry(self.root,show=None)
        self.box.grid(row=7,column=1,ipadx=60)

        self.root.protocol("WARING",self.windowClose)

        self.buttomInit()
        self.menuInit()
        self.root.mainloop()
    
    def windowClose(self):
        self.isPlaying=FALSE
        pygame.mixer.music.stop()
        pygame.mixer.music.quit()
        self.root.destroy()
    
    def buttomInit(self):
        #add
        self.bAdd=ttk.Button(self.root,text="Add",width=7,command=self.addFolder)
        self.bAdd.grid(row=0, column=0, padx=10, pady=5)
        self.bAdd["state"]="normal"
        
        #play
        self.flag=StringVar(self.root,value="Play")
        self.bPlay=ttk.Button(self.root,textvariable=self.flag,width=7,command=self.playClick)
        self.bPlay.grid(row=1,column=0,padx=10, pady=5)
        self.bPlay["state"]="disable"
        
        #stop
        self.bStop=ttk.Button(self.root,text="Stop",width=7,command=self.stopClick)
        self.bStop.grid(row=2,column=0,padx=10, pady=5)
        self.bStop["state"]="disable"
        
        #next
        self.bNext=ttk.Button(self.root,text="Next",width=7,command=self.nextClick)
        self.bNext.grid(row=3,column=0,padx=10, pady=5)
        self.bNext["state"]="disable"

        #Last
        self.bLast=ttk.Button(self.root,text="Last",width=7,command=self.lastClick)
        self.bLast.grid(row=4,column=0,padx=10, pady=5)
        self.bLast["state"]="disable"

        #volume adjust
        self.volumeScale=ttk.Scale(self.root,orient=HORIZONTAL,from_=0,to=100,length=200,command=self.volumeAd)
        self.volumeScale.grid(row=5,column=0,padx=10, pady=5)

        # #music position
        # self.pos = ttk.Scale(self.frame, from_=0, to=round(
        #         MP3(self.music).info.length),
        #                 orient=HORIZONTAL, tickinterval=50, length=300)

        # self.pos.place(x=180, y=60)
        
        #path
        self.bPath=ttk.Button(self.root,text="Add path",width=10)
        self.bPath.grid(row=7,column=2,padx=10, pady=5)
        self.bPath["state"]="normal"

    def menuInit(self):
        my_menu=Menu(self.root)
        
        file_menu=Menu(my_menu,tearoff=0)
        file_menu.add_command(label="Open File",command=self.addFile)
        file_menu.add_command(label="Open Folder",command=self.addFolder)
        file_menu.add_command(label="Clear Play List",command=self.clearList)
        file_menu.add_separator()
        file_menu.add_command(label="Exit",command=self.windowClose)

        action_menu=Menu(my_menu,tearoff=0)
        action_menu.add_command(label="Pause/Continue",command=self.playClick)
        action_menu.add_command(label="Stop",command=self.stopClick)
        action_menu.add_command(label="Next",command=self.nextClick)
        action_menu.add_command(label="Last",command=self.lastClick)
        

        my_menu.add_cascade(label="File",menu=file_menu)
        my_menu.add_cascade(label="Control",menu=action_menu)
        my_menu.add_cascade(label="About",command=self.About)
        
        self.root.config(menu=my_menu)
    
    def About(self):
        print(messagebox.showinfo(title="message",\
            message="Author:何沛霖\nStudentID:1809853U-I011-0078"))
    
    def addFile(self):
        musicFile=filedialog.askopenfilename()
        music=os.path.split(musicFile)[1]
        
        if music.endswith((".mp3",".flac",".wav","ape")):
            self.playList.append([self.counter]+[music])
            self.num=self.counter-1
            self.counter+=1
        elif not musicFile:
            pass
        else:
            print(messagebox.showwarning(title="error",\
                message="Please add the files ending with'.mp3','.flac','.wav','ape'"))
        self.showList()
    
    def addFolder(self):
        folder=filedialog.askdirectory()
        if folder:
            for music in os.listdir(folder):
                if music.endswith((".mp3",".flac",".wav","ape")):
                    self.playList.append([self.counter]+[music])
                    self.res.append(folder+'/'+music)
                    self.counter+=1
        else:
            pass
        self.showList()

    def volumeAd(self,arg):
        if self.isPlaying:
            pygame.mixer.music.set_volume(self.volumeScale.get()*0.01)

    def play(self):
        if self.playList:
            while self.isPlaying:
                if not pygame.mixer.music.get_busy():
                    self.playing.set(self.playList[self.num][1])
                    print(self.playList[self.num])

                    pygame.mixer.music.load(self.res[self.num].encode())
                    pygame.mixer.music.play(1)
                else:
                    time.sleep(1)

    def playClick(self):
        self.bNext["state"]="normal"
        self.bLast["state"]="normal"
        self.bStop["state"]="normal"

        if self.flag.get()=="Play":
            if self.isPlaying==False:
                self.isPlaying=True
            threading.Thread(target=self.play).start()
            self.flag.set("Pause")
        elif self.flag.get()=="Pause":
            if self.isPlaying==True:
                self.isPlaying=False
            pygame.mixer.music.pause()
            self.flag.set("Continue")
        elif self.flag.get()=="Continue":
            if self.isPlaying==False:
                self.isPlaying=True
            pygame.mixer.music.unpause()
            self.flag.set("Pause")
    
    def stopClick(self):
        if pygame.mixer.music.get_busy():
            self.isPlaying=False
            pygame.mixer.music.stop()
            self.playing.set("")
            self.flag.set("Play")
        else:
            pass
    
    def nextClick(self):
        self.isPlaying=False
        pygame.mixer.music.stop()
        if self.num==len(self.res)-1:
            self.num=0
        else:
            self.num+=1
        self.isPlaying=True
        threading.Thread(target=self.play).start()
    
    def lastClick(self):
        self.isPlaying=False
        pygame.mixer.music.stop()
        if self.num==0:
            self.num=len(self.res)-1
        else:
            self.num-=1
        self.isPlaying=True
        threading.Thread(target=self.play).start()
    
    def showList(self):
        if self.playList:
            var=StringVar()
            var.set(self.playList)

            self.listbox=Listbox(self.root,listvariable=var,font=('Helvetica','8'),fg="red",height=2,width=20)
            self.listbox.grid(row=4,column=1,rowspan=3,columnspan=2,ipadx=100,ipady=60)
            
            self.isPlaying=True
            self.bPlay["state"]="normal"
        else:
            pass
    
    def clearList(self):
        if self.playList:
            self.stopClick()
            
            self.res=[]
            self.num=0
            self.playList=[]
            self.counter=1
            self.isPlaying=False
            self.listbox.destroy()

            self.bPlay["state"]="disable"
            self.bStop["state"]="disable"
            self.bNext["state"]="disable"
            self.bLast["state"]="disable"
        else:
            pass



music=Music()
music.windowInit()
