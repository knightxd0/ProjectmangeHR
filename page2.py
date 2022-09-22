import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

window = tk.Tk()

#เปลี่ยนหน้า
def page1():
    window.destroy()
    import page1
    

def page3():
    window.destroy()
    import page3
    


#พื้นหลัง
bg = PhotoImage(file="UI/bg_page2.png")
bg_label = tk.Label(window,image=bg)
bg_label.pack()

#ปุ่มเปลี่ยนหน้า
bg_btpage1 = PhotoImage(file="UI/bt_page1.png")
bt_page1 = tk.Button(window,image=bg_btpage1,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page1)
bt_page1.place(x=30,y=90)

bg_btpage3 = PhotoImage(file="UI/bt_page3.png")
bt_page2 = tk.Button(window,image=bg_btpage3,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page3)
bt_page2.place(x=35,y=220)


#ช่องค้นหา
search_bar = StringVar()
search_bar.set("ค้นหา")
en_searchbar = tk.Entry(window,textvariable=search_bar,font="supermarket 18",fg="#ffffff",bg="#d0b484",borderwidth=0)
en_searchbar.place(x=290,y=275,width=500)

bg_icon = PhotoImage(file="UI/icon_search.png")
bt_iconSearch = tk.Button(window,image=bg_icon,bg="#f35c22",activebackground="#f35c22",borderwidth=0) #ปุ่มค้นหา
bt_iconSearch.place(x=950,y=40)

#ปุ่ม insert delete
bg_btinsert = PhotoImage(file="UI/icon_insert.png")
bt_insert = tk.Button(window,image=bg_btinsert,bg="#2c333e",activebackground="#2c333e",borderwidth=0)
bt_insert.place(x=924,y=450)

bg_btdel = PhotoImage(file="UI/icon_del.png")
bt_del = tk.Button(window,image=bg_btdel,bg="#2c333e",activebackground="#2c333e",borderwidth=0)
bt_del.place(x=924,y=550)

#ช่อง insert delete
inAndDel = StringVar()

en_inAndDel = tk.Entry(window,font="supermarket 18",fg="#ffffff",bg="#2c333e",borderwidth=0)
en_inAndDel.place(x=310,y=685,width=450)



window.resizable(False, False)
window.geometry("1048x786+250+5")
window.title("ระบบจัดตำแหน่งและพนักงาน")
# window.iconbitmap(r'ui/icon_app_OSE_icon.ico') #icon
window.mainloop()