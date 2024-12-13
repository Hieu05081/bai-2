print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


from tkinter import *

def NewFile():
    print("New File!")

def OpenFile():
    print("Open File!")

def Exit():
    print("Exit!")

def InsText():
    print("Insert Text!")

def InsPic():
    print("Insert Picture!")

def About():
    print("This is a simple example of a menu")

root = Tk()
root.title("Menu Example")
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

editmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Insert Text", command=InsText)
editmenu.add_command(label="Insert Picture", command=InsPic)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()
