import cv2
import numpy as np
from tkinter import *
from PIL import Image,ImageTk

def takephoto():
    image = Image.fromarray(img1)
    name = "photo"+".jpg"
    image.save(name)
    
r = Tk()
r.geometry("700x640")
f1 = LabelFrame(r)
f1.pack()
L1 = Label(f1)
L1.pack()

cap = cv2.VideoCapture(0)
but = Button(r,text="take photo",command=takephoto)
but.pack()

while True:
    img = cap.read()[1]
    img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image'] = img
    
    r.update()
    
cap.release()