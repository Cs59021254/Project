from tkinter import *
import sys
import os

def Face_rec() :
    import face_rec

def Encode():
    import en


        

    
def PrintName() :  
    Names=Name.get()
    mlabel = Label(content,text=Names).pack()
    
    try:
        if not os.path.exists(Names):
            path = "/dataset"
            os.chdir(path)
            os.makedirs(Names)
    except OSError:
        print("ERROR : Can not make floder!!!")
    return 
       

root = Tk()
content = Frame(root)
content.pack()
root.geometry("680x368")
root.title("Face Recognition System")
root.option_add("*Font","consolas 20")
Name = StringVar()
l1 =Label(content, text="Face Recognition System").pack()
b1 =Button(content, text="Face Recognition",command=Face_rec) .pack()
b2 =Button(content,text="Endcodeing",command=Encode).pack()
E1 = Entry(content,textvariable=Name) . pack()
b3 = Button(content,text ="Print",command= PrintName) .pack()
#RoomerName = Name.get()
#b4 = Button(content,text ="MakeFolder",command= Make_folder(RoomerName)) .pack()


root.mainloop()
