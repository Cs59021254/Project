from tkinter import *
i=1
def mHello () :
    
    print("test Button")
import cv2 
gui=Tk()
gui.geometry("720x450")
gui.title("Face Recognition System")
mlabel = Label(text = "Face Recognition",fg="#000") .pack()
mButton=Button(text ="Submit",command=mHello) .pack()
gui.mainloop()
