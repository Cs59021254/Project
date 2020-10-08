from tkinter import *

def Face_rec() :
    import face_rec.py
def Encode():
    import en.py
    
root = Tk()
root.geometry("680x368")
root.title("Face Recognition System")
root.option_add("*Font","consolas 20")
Label(root, text="Face Recognition System").pack()
Button(root, text="Face Recognition",command=Face_rec) .pack()
Button(root,text="Endcodeing",command=Encode).pack()
Name = Entry() . pack()
names = Name.get()
#Button(root,text = "Enter",command = InputName).pack()
Label(root , text = "{}".format(names).pack()
root.mainloop()
