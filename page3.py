from cProfile import label
from sqlite3 import Cursor
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import os
from Slinklist import Slinklist

window = tk.Tk()

sl_rank = Slinklist() #linklist rank
sl_user = Slinklist()
sl_salary = Slinklist()

# import file txt
file_rank = open("ProjectmangeHR/data/rank.txt",encoding="utf8")
rank = file_rank.read()
rank_list = rank.split("\n")
print(rank_list)
for data_r in rank_list:
    sl_rank.insertAtEnd(data_r)

# sl_rank.printList(sl_rank.head)
    

file_User = open("ProjectmangeHR/data/user.txt",encoding="utf8") #input file user.txt
user = file_User.read() #ใช้ .Read() เพื่อให้นำข้อมูลมาใช้ได้
user_list = user.split("\n")
print(user_list)
for data_r in user_list:
    sl_user.insertAtEnd(data_r)
    
sl_user.printList(sl_user.head)

file_salary = open("ProjectmangeHR/data/salary.txt",encoding="utf8")
salary = file_salary.read()
salary_list = salary.split("\n")
print(salary_list)
for data_r in salary_list:
    sl_salary.insertAtEnd(data_r)

# เปลี่ยนหน้า
def page1():
    window.withdraw()
    os.system("python page1.py")
    window.deiconify()
    

def page2():
    window.withdraw()
    os.system("python page2.py")
    window.deiconify()

# search
def clear_search(event):
    en_searchbar.delete(0, tk.END)
    
def search(event):
    index = 0
    data = search_bar.get()
    print(data)
    print(user_list)
    
    index = sl_user.search(data)
    print(index)
    
    if index >= 0:
            messagebox.showinfo("Show info",user_list[index]+" "+rank_list[index]+"\n"+salary_list[index]+" BATH")
            
    elif index < 0:
            messagebox.showinfo("Show info","ไม่พบข้อมูล")
    else:
            messagebox.showinfo("Show info","ไม่พบข้อมูล")

def search_icon():
    data = search_bar.get()
    print(data)
    print(user_list)
    index = 0
    for i in range(len(user_list)+1):
        if i == (len(user_list)):
            index = -1
            break
        elif data == user_list[i]:
            index = i
            break
        
    if index >= 0:
            messagebox.showinfo("Show info",user_list[index]+" "+rank_list[index]+"\n"+salary_list[index]+" BATH")
            
    elif index < 0:
            messagebox.showinfo("Show info","ไม่พบข้อมูล")
    else:
            messagebox.showinfo("Show info","ไม่พบข้อมูล")
           
        
     



#พื้นหลัง
bg = PhotoImage(file="ProjectmangeHR/UI/bg_page3.png")
bg_label = tk.Label(window,image=bg)
bg_label.pack()

#ปุ่มเปลี่ยนหน้า
bg_btpage1 = PhotoImage(file="ProjectmangeHR/UI/bt_page1.png")
bt_page1 = tk.Button(window,image=bg_btpage1,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page1,cursor="hand2")
bt_page1.place(x=30,y=90)

bg_btpage2 = PhotoImage(file="ProjectmangeHR/UI/bt_page2.png")
bt_page2 = tk.Button(window,image=bg_btpage2,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page2,cursor="hand2")
bt_page2.place(x=35,y=150)


#ช่องค้นหา
search_bar = StringVar()
en_searchbar = tk.Entry(window,textvariable=search_bar,font="supermarket 18",fg="#ffffff",bg="#f35c22",borderwidth=0)
en_searchbar.insert(0, "ค้นหา...")
en_searchbar.place(x=290,y=40,width=500)
en_searchbar.bind("<Button-1>", clear_search)

bg_icon = PhotoImage(file="ProjectmangeHR/UI/icon_search.png")
bt_iconSearch = tk.Button(window,image=bg_icon,bg="#f35c22",activebackground="#f35c22",borderwidth=0,command=search_icon,cursor="hand2") #ปุ่มค้นหา
bt_iconSearch.place(x=950,y=40)


#แสดงผลการค้นหา
text_user = Text(window,height=16,width=30,font="supermarket 14",bg="#4c525f",fg="#ffffff",borderwidth=0)
text_user.place(x=280,y=180)
text_user.insert(tk.END,user) #ใช้ insert ใน text เพื่อแสดงผล
text_user.configure(state=DISABLED)


text_salary = Text(window,height=16,width=30,font="supermarket 14",bg="#4c525f",fg="#ffffff",borderwidth=0)
text_salary.place(x=740,y=180)
text_salary.insert(tk.END,salary)
text_salary.configure(state=DISABLED)


text_rank = Text(window,height=16,width=18,font="supermarket 14",bg="#4c525f",fg="#ffffff",borderwidth=0)
text_rank.place(x=840,y=180)
text_rank.configure(state=NORMAL)
text_rank.insert(tk.END,rank)
text_rank.configure(state=DISABLED)

# user = StringVar()
# user.set("AKKARAPON KRAIKLIN\nTHITIKORN INDEE\nKARANRAT SUPASON\nKITTIPAK LUANMANEE\nSUMITA SRIPROM\nCHONTICHA DUEMCHAI\nCHAIWAT RUEANGKHETPHIT\nPAPICHAYA DEDKHAD\nTHANATHIP TRAKRUD")
# labelUser = tk.Label(window,textvariable=user,font="supermarket 16",bg="#4c525f",fg="#ffffff",anchor=NW,justify=LEFT)
# labelUser.place(x=280,y=190)

window.bind("<Return>",search)

window.resizable(False, False)
window.geometry("1048x786+250+5")
window.title("ระบบจัดตำแหน่งและพนักงาน")
# window.iconbitmap(r'ui/icon_app_OSE_icon.ico') #icon
window.mainloop()