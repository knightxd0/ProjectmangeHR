import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
# To get the dialog box to open when required
from tkinter import filedialog

#count นับรอบในแต่ละบรรทัดของแชทบอท
# count = 0
# logic เลือกส่งข้อความในช่องใส่เพิ่มกับลด 
# logic = 1 ใช้เพิ่มบุคคล
# logic = 2 ใช้ลดบุคคล
logic = 0

window = tk.Tk()


#เปลี่ยนหน้า
def page1():
    window.withdraw()
    os.system("python page1.py")
    window.deiconify()
    

def page3():
    window.withdraw()
    os.system("python page3.py")
    window.deiconify()

#count นับรอบในแต่ละบรรทัดของแชทบอท
cnum = 0
def delMember():
    global cnum
    global logic
    countnum = cnum
    logic = 2
    data = inAndDel.get()
    label_tree.configure(state=NORMAL)
    if countnum == 0:
        text_del = "BOT: Hello user\n"
        label_tree.insert(tk.END,text_del)
        text_del = "       Please enter your name\n"
        label_tree.insert(tk.END,text_del)
        label_tree.configure(state=DISABLED)
        cnum = cnum+1
        
    elif countnum == 1 :
        text_del = "USER: "+data+"\n"
        label_tree.insert(tk.END,text_del)
        label_tree.configure(state=DISABLED)
        cnum = cnum+1
        delMember()
        
    elif countnum == 2:
        text_del = "bot: Please enter your rank\n"
        label_tree.insert(tk.END,text_del)
        label_tree.configure(state=DISABLED)
        cnum = cnum+1 
        
    elif countnum == 3 and data != None:
        text_del = "USER: "+data+"\n"
        label_tree.insert(tk.END,text_del)
        label_tree.configure(state=DISABLED)
        cnum = cnum+1   
        delMember()
        
    elif countnum == 4:
        text_del = "bot: Successfully delete members\n"
        label_tree.insert(tk.END,text_del)
        label_tree.configure(state=DISABLED)
        cnum = 0
        logicnum = 0
        
def insertMember():
    logic = 1
    data = inAndDel.get()
    label_tree.configure(state=NORMAL)
    if count == 0:
        text_del = "Hello user"
        label_tree.insert(tk.END,text_del)
        label_tree.configure(state=DISABLED)
        count = count+1
    elif count == 1 :
        label_tree.insert(tk.END,data)
        label_tree.configure(state=DISABLED)
        count = count+1

def inputbar(event):
    if logic == 1:
        insertMember()
        en_inAndDel.delete(0,tk.END)
    elif logic == 2:
        delMember()
        en_inAndDel.delete(0,tk.END)
        
# search
def clear_search(event):
    en_searchbar.delete(0, tk.END)

# import photo
def open_img():
	# Select the Imagename from a folder
	x = openfilename()

	# opens the image
	img = Image.open(x)
	
	# resize the image and apply a high-quality down sampling filter
	img = img.resize((250, 250), Image.ANTIALIAS)

	# PhotoImage class is used to add image to widgets, icons etc
	img = ImageTk.PhotoImage(img)

	# create a label
	panel = Label(window, image = img)
	
	# set the image as img
	panel.image = img
	panel.grid(row = 2)

def openfilename():
	# open file dialog box to select image
	# The dialogue box has a title "Open"
	filename = filedialog.askopenfilename(title ='"pen')
	return filename


    
    
    


#พื้นหลัง
bg = PhotoImage(file="UI/bg_page2.png")
bg_label = tk.Label(window,image=bg)
bg_label.pack()

#ปุ่มเปลี่ยนหน้า
bg_btpage1 = PhotoImage(file="UI/bt_page1.png")
bt_page1 = tk.Button(window,image=bg_btpage1,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page1,cursor="hand2")
bt_page1.place(x=30,y=90)

bg_btpage3 = PhotoImage(file="UI/bt_page3.png")
bt_page2 = tk.Button(window,image=bg_btpage3,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page3,cursor="hand2")
bt_page2.place(x=35,y=220)


#ช่องค้นหา
search_bar = StringVar()
search_bar.set("ค้นหา")
en_searchbar = tk.Entry(window,textvariable=search_bar,font="supermarket 18",fg="#ffffff",bg="#d0b484",borderwidth=0)
en_searchbar.place(x=290,y=275,width=500)
en_searchbar.bind("<Button-1>", clear_search)

bg_icon = PhotoImage(file="UI/icon_search.png")
bt_iconSearch = tk.Button(window,image=bg_icon,bg="#d0b484",activebackground="#d0b484",borderwidth=0,cursor="hand2") #ปุ่มค้นหา
bt_iconSearch.place(x=950,y=280)

#ปุ่ม insert delete
bg_btinsert = PhotoImage(file="UI/icon_insert.png")
bt_insert = tk.Button(window,image=bg_btinsert,bg="#2c333e",activebackground="#2c333e",borderwidth=0,cursor="hand2")
bt_insert.place(x=924,y=450)

bg_btdel = PhotoImage(file="UI/icon_del.png")
bt_del = tk.Button(window,image=bg_btdel,bg="#2c333e",activebackground="#2c333e",borderwidth=0,cursor="hand2",command=delMember)
bt_del.place(x=924,y=550)

#ช่อง insert delete
inAndDel = StringVar()
en_inAndDel = tk.Entry(window,textvariable=inAndDel,font="supermarket 18",fg="#ffffff",bg="#2c333e",borderwidth=0)
en_inAndDel.place(x=310,y=685,width=450)


#show ชื่อ
scorebarry = Scrollbar(window,orient=VERTICAL)
label_tree = tk.Text(window,yscrollcommand=scorebarry.set,bg="#4c525f",bd=0,fg="#ffffff",font="supermarket 18")
label_tree.place(x=275, y=360, width=600, height=300)


window.bind("<Return>",inputbar)
window.resizable(False, False)
window.geometry("1048x786+250+5")
window.title("ระบบจัดตำแหน่งและพนักงาน")
# window.iconbitmap(r'ui/icon_app_OSE_icon.ico') #icon
window.mainloop()