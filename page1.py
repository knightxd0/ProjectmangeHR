import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from Slinklist import Slinklist

window = tk.Tk()


#เปลี่ยนหน้า
def page2():
    window.withdraw()
    os.system("python page2.py")
    window.deiconify()
    

def page3():
    window.withdraw()
    os.system("python page3.py")
    window.deiconify()
    
sl_rank = Slinklist() #linklist rank
sl_user = Slinklist()
sl_salary = Slinklist()

# import file txt
file_rank = open("data/rank.txt",encoding="utf8")
rank = file_rank.read()
rank_list = rank.split("\n")
print(rank_list)
for data_r in rank_list:
    sl_rank.insertAtEnd(data_r)

# sl_rank.printList(sl_rank.head)
    

file_User = open("data/user.txt",encoding="utf8") #input file user.txt
user = file_User.read() #ใช้ .Read() เพื่อให้นำข้อมูลมาใช้ได้
user_list = user.split("\n")
print(user_list)
for data_r in user_list:
    sl_user.insertAtEnd(data_r)
    
sl_user.printList(sl_user.head)

file_salary = open("data/salary.txt",encoding="utf8")
salary = file_salary.read()
salary_list = salary.split("\n")
print(salary_list)
for data_r in salary_list:
    sl_salary.insertAtEnd(data_r)
    
numofperson = sl_user.len()
print("num of person = "+ str(numofperson))


#พื้นหลัง
bg = ImageTk.PhotoImage(file="UI/bg_page1_10.png")
bg_label = tk.Label(window,image=bg)
bg_label.pack()

#img person
imgperson1 = Image.open('DCIM/prae_member.png')
resize_imgperson1 = imgperson1.resize((90,90))

img_person1 = ImageTk.PhotoImage(resize_imgperson1)

canvas = Canvas(window)
# cancvas
bg_page = canvas.create_image(0,0, image=bg, anchor=NW) #bg
img_p1 = canvas.create_image(615,110, image=img_person1) 
label_ceo = canvas.create_text(620,200, text="อัครพล ไกรกลิ่น",font="supermarket 20",fill='#ffffff')

#ปุ่มเปลี่ยนหน้า
bg_btpage2 = PhotoImage(file="UI/bt_page2.png")
bt_page2 = tk.Button(window,image=bg_btpage2,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page2,cursor="hand2")
bt_page2.place(x=38,y=160)

bg_btpage3 = PhotoImage(file="UI/bt_page3.png")
bt_page3 = tk.Button(window,image=bg_btpage3,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page3,cursor="hand2")
bt_page3.place(x=35,y=220)





canvas.place(x=0,y=0,width=1048,height=1048)

window.resizable(False, False)
window.geometry("1048x786+250+5")
window.title("ระบบจัดตำแหน่งและพนักงาน")
# window.iconbitmap(r'ui/icon_app_OSE_icon.ico') #icon
window.mainloop()