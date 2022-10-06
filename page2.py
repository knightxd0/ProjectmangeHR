import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import numpy as np
from PIL import Image, ImageDraw
# To get the dialog box to open when required
from tkinter import filedialog
from Slinklist import Slinklist

#count นับรอบในแต่ละบรรทัดของแชทบอท
# count = 0
# logic เลือกส่งข้อความในช่องใส่เพิ่มกับลด 
# logic = 1 ใช้เพิ่มบุคคล
# logic = 2 ใช้ลดบุคคล
logic = 0

window = tk.Tk()

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
    
#เปลี่ยนหน้า
def page1():
    window.withdraw()
    os.system("python page1.py")
    window.deiconify()
    

def page3():
    window.withdraw()
    os.system("python page3.py")
    window.deiconify()
    
def search():
    index = 0
    data = search_bar.get()
    print(data)
    print(user_list)
    
    index = sl_user.search(data)
    print(index)
    
    if index >= 0:
            messagebox.showinfo("Show info",user_list[index]+" "+rank_list[index]+"\n"+salary_list[index]+" BATH")
            inAndDel.set(user_list[index])
            
    elif index < 0:
            messagebox.showinfo("Show info","ไม่พบข้อมูล")
    else:
            messagebox.showinfo("Show info","ไม่พบข้อมูล")

#count นับรอบในแต่ละบรรทัดของแชทบอท
cnum = 0
def delMember():
    global cnum
    global logic
    global user,rank
    countnum = cnum
    logic = 2
    data = inAndDel.get()
    label_tree.configure(state=NORMAL)
    c = "cancel"
    if data == c:
        logic = 0
        cnum = 0
        label_tree.configure(state=NORMAL)
        label_tree.insert(tk.END,"BOT: Failed to execute\n")
        label_tree.configure(state=DISABLED)
    
    else:
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
            user = data     #เก็บชื่อ user ที่จะลบ
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
            rank = data #เก็บตำแหน่งของ user ที่จะถูกลบ
            cnum = cnum+1   
            delMember()
            
        elif countnum == 4:
            delete_user(user,rank)
            text_del = "bot: Successfully delete members\n"
            label_tree.insert(tk.END,text_del)
            label_tree.configure(state=DISABLED)
            cnum = 0
            logicnum = 0
#function delete user rank salary
def delete_user(user, rank):
    u = user
    r = rank
    print("u = " + u)
    #search index user
    index_user = sl_user.search(u)
    index_rank = sl_rank.search(r)
    if index_rank == index_user:
        print("user = "+str(index_user))
        sl_user.printList(sl_user.head)
        sl_user.delete(u)
        sl_user.printList(sl_user.head)
        
        print("rank = "+str(index_rank))
        sl_rank.printList(sl_rank.head)
        sl_rank.delete(r)
        sl_rank.printList(sl_rank.head)
        
        sl_salary.delete_index(index_user)
        sl_user.list_file("user")
        sl_rank.list_file("rank")
        sl_salary.list_file("salary")
    
    

    
def insertMember():
    global cnum
    global logic
    global user,rank
    countnum = cnum
    logic = 1
    data = inAndDel.get()
    label_tree.configure(state=NORMAL)
    c = "cancel"
    if data == c:
        logic = 0
        cnum = 0
        label_tree.configure(state=NORMAL)
        label_tree.insert(tk.END,"BOT: Failed to execute\n")
        label_tree.configure(state=DISABLED)
    
    else:
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
            user = data
            insertMember()
            
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
            rank = data   
            insertMember()
            
        elif countnum == 4:
            text_del = "bot: Please import your image\n"
            label_tree.insert(tk.END,text_del)
            if open_img(user,rank) == 1:
                insert_user(user,rank)
                text_del = "bot: Successfully add members\n"
                label_tree.insert(tk.END,text_del)
                label_tree.configure(state=DISABLED)
                cnum = 0
                logicnum = 0
            elif open_img(user,rank) == 0:
                text_del = "bot: Not successfully add members\n"
                label_tree.insert(tk.END,text_del)
                label_tree.configure(state=DISABLED)
                cnum = 0
                logicnum = 0

def insert_user(user, rank):
    u = user
    r = rank
    if r == "CEO" or r == "Ceo" or r == "ceo": salary = 200,000
    elif r == "Vice Chairman" or r == "Vice chairman" or r == "vice chairman": salary = 80,000
    elif r == "Secretary" or r == "secretary": salary = 40,000
    elif r == "Development Manager" or r == "Development manager" or r == "development manager": salary = 50,000
    elif r == "Marketing Manager" or r == "Marketing manager" or r == "marketing manager": salary = 30,000
    elif r == "Personnel Manager" or r == "Personnel manager" or r == "personnel manager": salary = 26,000
    elif r == "Developer Member" or r == "Developer member" or r == "developer member": salary = 20,000
    elif r == "Marketing Member" or r == "Marketing member" or r == "marketing member": salary = 18,000
    
    
    print("u = " + u)
    #search index user
    if r == "ceo" or r == "Ceo" or r =="CEO": 
        salary = "200,000"
        s = str(salary)
        sl_user.insertAtHead(u)
        sl_rank.insertAtHead(r)
        sl_salary.insertAtHead(s)
    else:
        s = str(salary)
        sl_user.insertAtEnd(u)
        sl_rank.insertAtEnd(r)
        sl_salary.insertAtEnd(s)
    
    sl_user.list_file("user")
    sl_rank.list_file("rank")
    sl_salary.list_file("salary")
        
def inputbar(event):
    print(logic)
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
def open_img(user,rank):
    global w,h
	# Select the Imagename from a folder
    x = openfilename()
    if x:
        # opens the image
        img1 = Image.open(x)
        
        height,width = img1.size
        lum_img = Image.new('L', [height,width] , 0)
        print(height)
        print(width)
        
        draw = ImageDraw.Draw(lum_img)
        draw.pieslice([(0,0), (height,width)], 100, 2000, 
                    fill = 600, outline = "white")
        img_arr = np.array(img1)
        lum_img_arr =np.array(lum_img)
        # (Image.fromarray(lum_img_arr))
        final_img_arr = np.dstack((img_arr,lum_img_arr))
        img2 = (Image.fromarray(final_img_arr)).convert('RGBA')

        data = img2.getdata()

        datas = []

        for item in data:
            if item[0] == 0 and item[1] == 0 and item[2] == 0:
                datas.append((255,255,255,0))
            else:
                datas.append(item)
                
        img2.putdata(datas)
        name = "DCIM/"+str(user) +"_"+ str(rank)+".png"
        img_save = img2.save(name, quality=95)
        
        return 1
    else:
        return 0

def openfilename():
	# open file dialog box to select image
	# The dialogue box has a title "Open"
	filename = filedialog.askopenfilename(title ='import photo')
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
bt_iconSearch = tk.Button(window,image=bg_icon,bg="#d0b484",activebackground="#d0b484",borderwidth=0,cursor="hand2",command=search) #ปุ่มค้นหา
bt_iconSearch.place(x=950,y=280)

#ปุ่ม insert delete
bg_btinsert = PhotoImage(file="UI/icon_insert.png")
bt_insert = tk.Button(window,image=bg_btinsert,bg="#2c333e",activebackground="#2c333e",borderwidth=0,cursor="hand2",command=insertMember)
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