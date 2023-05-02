#  hear goes the GUI code ...

from tkinter import *

class GUI:

    def __init__(self, root):
        self.root = root
        root.geometry("{0}x{1}".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        root.title("Code Editor")

        mainFrame =  Frame(root ,  bg="#1E1E1E" , bd=5)
        mainFrame.pack( side=TOP,fill=BOTH, expand=1)


root = Tk()
root.title("Code Editor")
gui = GUI(root)
root.mainloop()
