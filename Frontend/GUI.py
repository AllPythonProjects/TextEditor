#  hear goes the GUI code ...

from tkinter import *
from tkinter import filedialog
import speech_recognition as sr

class GUI:
   
    def __init__(self, root):
        self.root = root
        mainFrame =  Frame(root ,  bg="#1E1E1E" , padx=10 , pady=10)
        mainFrame.pack( side=TOP,fill=BOTH, expand=1)


        textArea = Text(mainFrame , width=60 , height=80 , bg="#1E1E1E" , fg="white", padx=5 ,pady=5)
        textArea.pack( fill=BOTH , expand=1)
        textArea.bind('<Key>' , self.textAreaEventLoop)

        #               Scroll bar for text area
        ScrollbarForTextArea = Scrollbar(mainFrame)
        ScrollbarForTextArea.pack(side=RIGHT , fill=Y )
        ScrollbarForTextArea.config(command=textArea.yview)

        #               If This Button is Clicked Microphone will be enabeled and Speach Will Be Recognized

        speakBtn =  Button(mainFrame, text="Speak",padx=10 , pady=5 , bg="#5A23CE" , font=("Arial" , 16) , fg="white" , borderwidth=0 , command=self.speakBtnfun)
        speakBtn.place(relx=1.0, rely=1.0 ,anchor='se')


        topMenu = Menu(root , bg="gray", fg="white", font=("Arial", 12))
        root.config(menu = topMenu)

        fileitem = Menu(topMenu , tearoff=False)
        topMenu.add_cascade(label="File" , menu=fileitem)

        fileitem.add_cascade(label="New" , command=self.newFun)
        fileitem.add_cascade(label="Open" , command=self.openFun)
        fileitem.add_cascade(label="Save" , command=self.saveFun)


        editItem =  Menu(topMenu , tearoff=False)
        topMenu.add_cascade(label="Edit" , menu=editItem)
        editItem.add_cascade(label="Undo" , command=self.Undo)
        editItem.add_cascade(label="Redo" , command=self.Redo)

        
        newTab = Menu(topMenu , tearoff=False)
        topMenu.add_cascade(label="New Tab" , menu=newTab)

    
    # --------------------- F U N C T I O N A L I T Y E S ----------------------------- 

    

    # Functions Related to File menu 

    # fileLoc = ""
    def newFun(self):
        fileLoc = filedialog.askopenfilename(title="Select the File")

        print("new function")
    
    def openFun(self):
        print("open fun")

    def saveFun(self):
        print("save fun")
        # self.pasteIntoDesiredFile(fileLoc)

    def pasteIntoDesiredFile(loc):
        print(" past into desired file")
         # file = OpenFile(loc)
         # textArea.insert(END, file.read())

    
       # Function related to Tab menu
    def newTabBtnHandler(self):
        print("new tab is clicked ")

    

    
    # functions Related to Edit menu 
    
    def Undo(self):
        print("go to privious stage")

    def Redo(self):
        print("go to forword stage")

    
    # This function runs when Speech Button is Clicked
    
    def speakBtnfun(self):
         r = sr.Recognizer()
        with sr.Microphone() as source:
            # reading the audio data from the default microphone
            print("Speak")
            audio= r.record(source, duration=7)
            print("Recognizing speech...")
            # converting speech to text
            text = r.recognize_google(audio)
            print(text)
    # Hear we call the function present in SpeachToCode file present in Login Dir...
        

    
    def textAreaEventLoop(self , event):   
        print("eventloop is running " , event.char)
    



root = Tk()
root.geometry("500x500")  # when application is menisized
root.title("Code Editor")
root.state("zoomed")      # Opening size will be full screen
gui = GUI(root)
root.mainloop()
