from tkinter import *
import os
def capture () :
    import cap

def makeFolder ():
    RoomerName=Name.get()
    mlabel = Label(content,text=RoomerName).pack()
    os.chdir("dataset")
    try:
        if not os.path.exists(RoomerName):
            os.makedirs(RoomerName)
    except OSError:
        print("ERROR : Can not make floder!!!")

root = Tk()
content = Frame(root)
content.pack()
root.geometry("680x368")
root.title("เพิ่มฬบหน้าผู้ใช้")
root.option_add("*Font","consolas 20")
Name = StringVar()
E1 = Entry(frame,textvariable=Name) . pack()
roomer = Name.get()
b1 = Button(frame,text ="make",command= makeFolder) .pack()
b2 = Button(frame,text ="cap",command= Cap(roomer)) .pack()


root.mainloop()