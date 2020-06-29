import tkinter
import os
from tkinter import *
#messagebox is used to write the message in the white box called notepad
from tkinter.messagebox import *
#filedialog is used for the dialog box to appear when you are opening file from anywhere in your system or saving your file in a particular position or place.
from tkinter.filedialog import *

class Editor:
    __root = Tk()

    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    def __init__(self, **kwargs):
        self.__thisWidth = kwargs['width']
        self.__thisHeight = kwargs['height']
        self.__root.title("Untitled - Notepad")

        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,self.__thisHeight,left, top))

        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        self.__thisTextArea.grid(sticky = N + E + S + W)
        self.__thisFileMenu.add_command(label="New",command=self.__newFile)

        self.__thisFileMenu.add_separator()
        self.__thisMenuBar.add_cascade(label="File",menu=self.__thisFileMenu)


        self.__root.config(menu=self.__thisMenuBar)
    def __newFile(self):
        self.__root.title('Untitled - Editor')
        self.__file  = None
        self.__thisTextArea.delete(1.0,END)
    def run(self):
        # Run main application
        self.__root.mainloop()
    

Editor = Editor(width = 600 ,height = 600)
Editor.run()