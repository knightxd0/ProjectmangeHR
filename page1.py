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
    os.system("python ProjectmangeHR/page2.py")
    window.deiconify()
    

def page3():
    window.withdraw()
    os.system("python ProjectmangeHR/page3.py")
    window.deiconify()
    
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
    
numofperson = sl_user.len()
print("num of person = "+ str(numofperson))
      
canvas = Canvas(window)

count_develop = 1  
count_marketing = 1      
i = numofperson
if i == 4:
    print("person "+str(i))
    #พื้นหลัง
    bg = ImageTk.PhotoImage(file="ProjectmangeHR/UI/bg_page1_10.png")
    # bg_label = tk.Label(window,image=bg)
    # bg_label.pack()
    # cancvas
    bg_page = canvas.create_image(0,0, image=bg, anchor=NW) #bg
    for r in rank_list:
        if r == "CEO" or r == "Ceo" or r == "ceo": 
            #index rank
            index1 = sl_rank.search(r)
            #img person
            name_person1 = "ProjectmangeHR/DCIM/" + str(user_list[index1]) + "_" + str(rank_list[index1])+".png"
            imgperson1 = Image.open(name_person1)
            resize_imgperson1 = imgperson1.resize((90,90))
            # imgperson3 = Image.open()
            img_person1 = ImageTk.PhotoImage(resize_imgperson1)
            #ceo
            img_p1 = canvas.create_image(615,110, image=img_person1)
            label_ceo = canvas.create_text(620,200, text=str(user_list[index1]),font="supermarket 16",fill='#ffffff')

        elif r == "Vice Chairman" or r == "Vice chairman" or r == "vice chairman": 
            #index rank
            index2 = sl_rank.search(r)
            #img person
            name_person2 = "ProjectmangeHR/DCIM/" + str(user_list[index2]) + "_" + str(rank_list[index2])+".png"
            imgperson2 = Image.open(name_person2)
            resize_imgperson2 = imgperson2.resize((90,90))
            # imgperson3 = Image.open()
            img_person2 = ImageTk.PhotoImage(resize_imgperson2)
            #รองประธาน
            img_p2 = canvas.create_image(425,230, image=img_person2)
            label_ViceChairman = canvas.create_text(430,290, text="รองประธาน",font="supermarket 16",fill='#ffffff')
            label_name_ViceChairman = canvas.create_text(430,320, text=str(user_list[index2]),font="supermarket 16",fill='#ffffff')

        elif r == "Secretary" or r == "secretary": 
            #index rank
            index3 = sl_rank.search(r)
            #img person
            name_person3 = "ProjectmangeHR/DCIM/" + str(user_list[index3]) + "_" + str(rank_list[index3])+".png"
            imgperson3 = Image.open(name_person3)
            resize_imgperson3 = imgperson3.resize((90,90))
            # imgperson3 = Image.open()
            img_person3 = ImageTk.PhotoImage(resize_imgperson3)
            # เลขา
            img_p3 = canvas.create_image(820,230, image=img_person3)
            label_Secretary = canvas.create_text(820,290, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(820,320, text=str(user_list[index3]),font="supermarket 16",fill='#ffffff')

        elif r == "Development Manager" or r == "Development manager" or r == "development manager": 
            #index rank
            index4 = sl_rank.search(r)
            #img person
            name_person4 = "ProjectmangeHR/DCIM/" + str(user_list[index4]) + "_" + str(rank_list[index4])+".png"
            imgperson4 = Image.open(name_person4)
            resize_imgperson4 = imgperson4.resize((90,90))
            # imgperson3 = Image.open()
            img_person4 = ImageTk.PhotoImage(resize_imgperson4)
            # หัวหน้า Development
            img_p5 = canvas.create_image(320,410, image=img_person4)
            label_Development_manager = canvas.create_text(330,470, text="หัวหน้านักพัฒนา",font="supermarket 16",fill='#ffffff')
            label_name_Development_manager = canvas.create_text(330,500, text=str(user_list[index4]),font="supermarket 16",fill='#ffffff')

        elif r == "Marketing Manager" or r == "Marketing manager" or r == "marketing manager": 
            #index rank
            index5 = sl_rank.search(r)
            #img person
            name_person5 = "ProjectmangeHR/DCIM/" + str(user_list[index5]) + "_" + str(rank_list[index5])+".png"
            imgperson5 = Image.open(name_person5)
            resize_imgperson5 = imgperson5.resize((90,90))
            # imgperson3 = Image.open()
            img_person5 = ImageTk.PhotoImage(resize_imgperson5)
            # หัวหน้า ฝ่ายขาย
            img_p6 = canvas.create_image(625,410, image=img_person5)
            label_Marketing_manager = canvas.create_text(630,470, text="หัวหน้าฝ่ายขาย",font="supermarket 16",fill='#ffffff')
            label_name_Marketing_manager = canvas.create_text(630,500, text=str(user_list[index5]),font="supermarket 16",fill='#ffffff')

        elif r == "Personnel Manager" or r == "Personnel manager" or r == "personnel manager": 
            #index rank
            index6 = sl_rank.search(r)
            #img person
            name_person6 = "ProjectmangeHR/DCIM/" + str(user_list[index6]) + "_" + str(rank_list[index6])+".png"
            imgperson6 = Image.open(name_person6)
            resize_imgperson6 = imgperson6.resize((90,90))
            # imgperson3 = Image.open()
            img_person6 = ImageTk.PhotoImage(resize_imgperson6)
            # ฝ่ายบุคล
            img_p4 = canvas.create_image(940,410, image=img_person6)
            label_Secretary = canvas.create_text(940,470, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(940,500, text=str(user_list[index6]),font="supermarket 16",fill='#ffffff')

        elif r == "Developer Member1" or r == "Developer member1" or r == "developer member1": 
                #index rank
                index7 = sl_rank.search(r)
                #img person
                name_person7 = "ProjectmangeHR/DCIM/" + str(user_list[index7]) + "_" + str(rank_list[index7])+".png"
                imgperson7 = Image.open(name_person7)
                resize_imgperson7 = imgperson7.resize((90,90))
                # imgperson3 = Image.open()
                img_person7 = ImageTk.PhotoImage(resize_imgperson7)
                # Developer
                img_p7 = canvas.create_image(290,650, image=img_person7)
                label_Developer_1 = canvas.create_text(285,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_1 = canvas.create_text(285,730, text=str(user_list[index7]),font="supermarket 9",fill='#ffffff')
                
        elif r == "Developer Member2" or r == "Developer member2" or r == "developer member2": 
                #index rank
                index8 = sl_rank.search(r)
                #img person
                name_person8 = "ProjectmangeHR/DCIM/" + str(user_list[index8]) + "_" + str(rank_list[index8])+".png"
                imgperson8 = Image.open(name_person8)
                resize_imgperson8 = imgperson8.resize((90,90))
                # imgperson3 = Image.open()
                img_person8 = ImageTk.PhotoImage(resize_imgperson8)
                # Developer
                img_p8 = canvas.create_image(415,650, image=img_person8)
                label_Developer_2 = canvas.create_text(425,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_2 = canvas.create_text(425,730, text=str(user_list[index8]),font="supermarket 9",fill='#ffffff')

        elif r == "Marketing Member1" or r == "Marketing member1" or r == "marketing member1": 
                #index rank
                index9 = sl_rank.search(r)
                #img person
                name_person9 = "ProjectmangeHR/DCIM/" + str(user_list[index9]) + "_" + str(rank_list[index9])+".png"
                imgperson9 = Image.open(name_person9)
                resize_imgperson9 = imgperson9.resize((90,90))
                # imgperson3 = Image.open()
                img_person9 = ImageTk.PhotoImage(resize_imgperson9)
                # ฝ่ายขาย
                img_p9 = canvas.create_image(570,650, image=img_person9)
                label_Marketing_1 = canvas.create_text(570,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_1 = canvas.create_text(570,730, text=str(user_list[index9]),font="supermarket 9",fill='#ffffff')
                count_marketing = count_marketing + 1
        elif r == "Marketing Member2" or r == "Marketing member2" or r == "marketing member2": 
                #index rank
                index11 = sl_rank.search(r)
                #img person
                nameperson11 = "ProjectmangeHR/DCIM/" + str(user_list[index11]) + "_" + str(rank_list[index11])+".png"
                imgperson11 = Image.open(nameperson11)
                resize_imgperson11 = imgperson11.resize((90,90))
                # imgperson3 = Image.open()
                img_person11 = ImageTk.PhotoImage(resize_imgperson11)
                # ฝ่ายขาย
                img_p10 = canvas.create_image(695,650, image=img_person11)
                label_Marketing_2 = canvas.create_text(700,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_2 = canvas.create_text(700,730, text=str(user_list[index11]),font="supermarket 9",fill='#ffffff')
elif i == 9:
    print("person "+str(i))
    #พื้นหลัง
    bg = ImageTk.PhotoImage(file="ProjectmangeHR/UI/bg_page1_10.png")
    # bg_label = tk.Label(window,image=bg)
    # bg_label.pack()
    # cancvas
    bg_page = canvas.create_image(0,0, image=bg, anchor=NW) #bg
    for r in rank_list:
        if r == "CEO" or r == "Ceo" or r == "ceo": 
            #index rank
            index1 = sl_rank.search(r)
            #img person
            name_person1 = "ProjectmangeHR/DCIM/" + str(user_list[index1]) + "_" + str(rank_list[index1])+".png"
            imgperson1 = Image.open(name_person1)
            resize_imgperson1 = imgperson1.resize((90,90))
            # imgperson3 = Image.open()
            img_person1 = ImageTk.PhotoImage(resize_imgperson1)
            #ceo
            img_p1 = canvas.create_image(615,110, image=img_person1)
            label_ceo = canvas.create_text(620,200, text=str(user_list[index1]),font="supermarket 16",fill='#ffffff')

        elif r == "Vice Chairman" or r == "Vice chairman" or r == "vice chairman": 
            #index rank
            index2 = sl_rank.search(r)
            #img person
            name_person2 = "ProjectmangeHR/DCIM/" + str(user_list[index2]) + "_" + str(rank_list[index2])+".png"
            imgperson2 = Image.open(name_person2)
            resize_imgperson2 = imgperson2.resize((90,90))
            # imgperson3 = Image.open()
            img_person2 = ImageTk.PhotoImage(resize_imgperson2)
            #รองประธาน
            img_p2 = canvas.create_image(425,230, image=img_person2)
            label_ViceChairman = canvas.create_text(430,290, text="รองประธาน",font="supermarket 16",fill='#ffffff')
            label_name_ViceChairman = canvas.create_text(430,320, text=str(user_list[index2]),font="supermarket 16",fill='#ffffff')

        elif r == "Secretary" or r == "secretary": 
            #index rank
            index3 = sl_rank.search(r)
            #img person
            name_person3 = "ProjectmangeHR/DCIM/" + str(user_list[index3]) + "_" + str(rank_list[index3])+".png"
            imgperson3 = Image.open(name_person3)
            resize_imgperson3 = imgperson3.resize((90,90))
            # imgperson3 = Image.open()
            img_person3 = ImageTk.PhotoImage(resize_imgperson3)
            # เลขา
            img_p3 = canvas.create_image(820,230, image=img_person3)
            label_Secretary = canvas.create_text(820,290, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(820,320, text=str(user_list[index3]),font="supermarket 16",fill='#ffffff')

        elif r == "Development Manager" or r == "Development manager" or r == "development manager": 
            #index rank
            index4 = sl_rank.search(r)
            #img person
            name_person4 = "ProjectmangeHR/DCIM/" + str(user_list[index4]) + "_" + str(rank_list[index4])+".png"
            imgperson4 = Image.open(name_person4)
            resize_imgperson4 = imgperson4.resize((90,90))
            # imgperson3 = Image.open()
            img_person4 = ImageTk.PhotoImage(resize_imgperson4)
            # หัวหน้า Development
            img_p5 = canvas.create_image(320,410, image=img_person4)
            label_Development_manager = canvas.create_text(330,470, text="หัวหน้านักพัฒนา",font="supermarket 16",fill='#ffffff')
            label_name_Development_manager = canvas.create_text(330,500, text=str(user_list[index4]),font="supermarket 16",fill='#ffffff')

        elif r == "Marketing Manager" or r == "Marketing manager" or r == "marketing manager": 
            #index rank
            index5 = sl_rank.search(r)
            #img person
            name_person5 = "ProjectmangeHR/DCIM/" + str(user_list[index5]) + "_" + str(rank_list[index5])+".png"
            imgperson5 = Image.open(name_person5)
            resize_imgperson5 = imgperson5.resize((90,90))
            # imgperson3 = Image.open()
            img_person5 = ImageTk.PhotoImage(resize_imgperson5)
            # หัวหน้า ฝ่ายขาย
            img_p6 = canvas.create_image(625,410, image=img_person5)
            label_Marketing_manager = canvas.create_text(630,470, text="หัวหน้าฝ่ายขาย",font="supermarket 16",fill='#ffffff')
            label_name_Marketing_manager = canvas.create_text(630,500, text=str(user_list[index5]),font="supermarket 16",fill='#ffffff')

        elif r == "Personnel Manager" or r == "Personnel manager" or r == "personnel manager": 
            #index rank
            index6 = sl_rank.search(r)
            #img person
            name_person6 = "ProjectmangeHR/DCIM/" + str(user_list[index6]) + "_" + str(rank_list[index6])+".png"
            imgperson6 = Image.open(name_person6)
            resize_imgperson6 = imgperson6.resize((90,90))
            # imgperson3 = Image.open()
            img_person6 = ImageTk.PhotoImage(resize_imgperson6)
            # ฝ่ายบุคล
            img_p4 = canvas.create_image(940,410, image=img_person6)
            label_Secretary = canvas.create_text(940,470, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(940,500, text=str(user_list[index6]),font="supermarket 16",fill='#ffffff')

        elif r == "Developer Member1" or r == "Developer member1" or r == "developer member1": 
                #index rank
                index7 = sl_rank.search(r)
                #img person
                name_person7 = "ProjectmangeHR/DCIM/" + str(user_list[index7]) + "_" + str(rank_list[index7])+".png"
                imgperson7 = Image.open(name_person7)
                resize_imgperson7 = imgperson7.resize((90,90))
                # imgperson3 = Image.open()
                img_person7 = ImageTk.PhotoImage(resize_imgperson7)
                # Developer
                img_p7 = canvas.create_image(290,650, image=img_person7)
                label_Developer_1 = canvas.create_text(285,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_1 = canvas.create_text(285,730, text=str(user_list[index7]),font="supermarket 9",fill='#ffffff')
                
        elif r == "Developer Member2" or r == "Developer member2" or r == "developer member2": 
                #index rank
                index8 = sl_rank.search(r)
                #img person
                name_person8 = "ProjectmangeHR/DCIM/" + str(user_list[index8]) + "_" + str(rank_list[index8])+".png"
                imgperson8 = Image.open(name_person8)
                resize_imgperson8 = imgperson8.resize((90,90))
                # imgperson3 = Image.open()
                img_person8 = ImageTk.PhotoImage(resize_imgperson8)
                # Developer
                img_p8 = canvas.create_image(415,650, image=img_person8)
                label_Developer_2 = canvas.create_text(425,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_2 = canvas.create_text(425,730, text=str(user_list[index8]),font="supermarket 9",fill='#ffffff')

        elif r == "Marketing Member1" or r == "Marketing member1" or r == "marketing member1": 
                #index rank
                index9 = sl_rank.search(r)
                #img person
                name_person9 = "ProjectmangeHR/DCIM/" + str(user_list[index9]) + "_" + str(rank_list[index9])+".png"
                imgperson9 = Image.open(name_person9)
                resize_imgperson9 = imgperson9.resize((90,90))
                # imgperson3 = Image.open()
                img_person9 = ImageTk.PhotoImage(resize_imgperson9)
                # ฝ่ายขาย
                img_p9 = canvas.create_image(570,650, image=img_person9)
                label_Marketing_1 = canvas.create_text(570,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_1 = canvas.create_text(570,730, text=str(user_list[index9]),font="supermarket 9",fill='#ffffff')
                count_marketing = count_marketing + 1
        elif r == "Marketing Member2" or r == "Marketing member2" or r == "marketing member2": 
                #index rank
                index11 = sl_rank.search(r)
                #img person
                nameperson11 = "ProjectmangeHR/DCIM/" + str(user_list[index11]) + "_" + str(rank_list[index11])+".png"
                imgperson11 = Image.open(nameperson11)
                resize_imgperson11 = imgperson11.resize((90,90))
                # imgperson3 = Image.open()
                img_person11 = ImageTk.PhotoImage(resize_imgperson11)
                # ฝ่ายขาย
                img_p10 = canvas.create_image(695,650, image=img_person11)
                label_Marketing_2 = canvas.create_text(700,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_2 = canvas.create_text(700,730, text=str(user_list[index11]),font="supermarket 9",fill='#ffffff')
elif i == 8:
    print("person "+str(i))
    #พื้นหลัง
    bg = ImageTk.PhotoImage(file="ProjectmangeHR/UI/bg_page1_10.png")
    # bg_label = tk.Label(window,image=bg)
    # bg_label.pack()
    # cancvas
    bg_page = canvas.create_image(0,0, image=bg, anchor=NW) #bg
    for r in rank_list:
        if r == "CEO" or r == "Ceo" or r == "ceo": 
            #index rank
            index1 = sl_rank.search(r)
            #img person
            name_person1 = "ProjectmangeHR/DCIM/" + str(user_list[index1]) + "_" + str(rank_list[index1])+".png"
            imgperson1 = Image.open(name_person1)
            resize_imgperson1 = imgperson1.resize((90,90))
            # imgperson3 = Image.open()
            img_person1 = ImageTk.PhotoImage(resize_imgperson1)
            #ceo
            img_p1 = canvas.create_image(615,110, image=img_person1)
            label_ceo = canvas.create_text(620,200, text=str(user_list[index1]),font="supermarket 16",fill='#ffffff')

        elif r == "Vice Chairman" or r == "Vice chairman" or r == "vice chairman": 
            #index rank
            index2 = sl_rank.search(r)
            #img person
            name_person2 = "ProjectmangeHR/DCIM/" + str(user_list[index2]) + "_" + str(rank_list[index2])+".png"
            imgperson2 = Image.open(name_person2)
            resize_imgperson2 = imgperson2.resize((90,90))
            # imgperson3 = Image.open()
            img_person2 = ImageTk.PhotoImage(resize_imgperson2)
            #รองประธาน
            img_p2 = canvas.create_image(425,230, image=img_person2)
            label_ViceChairman = canvas.create_text(430,290, text="รองประธาน",font="supermarket 16",fill='#ffffff')
            label_name_ViceChairman = canvas.create_text(430,320, text=str(user_list[index2]),font="supermarket 16",fill='#ffffff')

        elif r == "Secretary" or r == "secretary": 
            #index rank
            index3 = sl_rank.search(r)
            #img person
            name_person3 = "ProjectmangeHR/DCIM/" + str(user_list[index3]) + "_" + str(rank_list[index3])+".png"
            imgperson3 = Image.open(name_person3)
            resize_imgperson3 = imgperson3.resize((90,90))
            # imgperson3 = Image.open()
            img_person3 = ImageTk.PhotoImage(resize_imgperson3)
            # เลขา
            img_p3 = canvas.create_image(820,230, image=img_person3)
            label_Secretary = canvas.create_text(820,290, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(820,320, text=str(user_list[index3]),font="supermarket 16",fill='#ffffff')

        elif r == "Development Manager" or r == "Development manager" or r == "development manager": 
            #index rank
            index4 = sl_rank.search(r)
            #img person
            name_person4 = "ProjectmangeHR/DCIM/" + str(user_list[index4]) + "_" + str(rank_list[index4])+".png"
            imgperson4 = Image.open(name_person4)
            resize_imgperson4 = imgperson4.resize((90,90))
            # imgperson3 = Image.open()
            img_person4 = ImageTk.PhotoImage(resize_imgperson4)
            # หัวหน้า Development
            img_p5 = canvas.create_image(320,410, image=img_person4)
            label_Development_manager = canvas.create_text(330,470, text="หัวหน้านักพัฒนา",font="supermarket 16",fill='#ffffff')
            label_name_Development_manager = canvas.create_text(330,500, text=str(user_list[index4]),font="supermarket 16",fill='#ffffff')

        elif r == "Marketing Manager" or r == "Marketing manager" or r == "marketing manager": 
            #index rank
            index5 = sl_rank.search(r)
            #img person
            name_person5 = "ProjectmangeHR/DCIM/" + str(user_list[index5]) + "_" + str(rank_list[index5])+".png"
            imgperson5 = Image.open(name_person5)
            resize_imgperson5 = imgperson5.resize((90,90))
            # imgperson3 = Image.open()
            img_person5 = ImageTk.PhotoImage(resize_imgperson5)
            # หัวหน้า ฝ่ายขาย
            img_p6 = canvas.create_image(625,410, image=img_person5)
            label_Marketing_manager = canvas.create_text(630,470, text="หัวหน้าฝ่ายขาย",font="supermarket 16",fill='#ffffff')
            label_name_Marketing_manager = canvas.create_text(630,500, text=str(user_list[index5]),font="supermarket 16",fill='#ffffff')

        elif r == "Personnel Manager" or r == "Personnel manager" or r == "personnel manager": 
            #index rank
            index6 = sl_rank.search(r)
            #img person
            name_person6 = "ProjectmangeHR/DCIM/" + str(user_list[index6]) + "_" + str(rank_list[index6])+".png"
            imgperson6 = Image.open(name_person6)
            resize_imgperson6 = imgperson6.resize((90,90))
            # imgperson3 = Image.open()
            img_person6 = ImageTk.PhotoImage(resize_imgperson6)
            # ฝ่ายบุคล
            img_p4 = canvas.create_image(940,410, image=img_person6)
            label_Secretary = canvas.create_text(940,470, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(940,500, text=str(user_list[index6]),font="supermarket 16",fill='#ffffff')

        elif r == "Developer Member1" or r == "Developer member1" or r == "developer member1": 
                #index rank
                index7 = sl_rank.search(r)
                #img person
                name_person7 = "ProjectmangeHR/DCIM/" + str(user_list[index7]) + "_" + str(rank_list[index7])+".png"
                imgperson7 = Image.open(name_person7)
                resize_imgperson7 = imgperson7.resize((90,90))
                # imgperson3 = Image.open()
                img_person7 = ImageTk.PhotoImage(resize_imgperson7)
                # Developer
                img_p7 = canvas.create_image(290,650, image=img_person7)
                label_Developer_1 = canvas.create_text(285,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_1 = canvas.create_text(285,730, text=str(user_list[index7]),font="supermarket 9",fill='#ffffff')
                
        elif r == "Developer Member2" or r == "Developer member2" or r == "developer member2": 
                #index rank
                index8 = sl_rank.search(r)
                #img person
                name_person8 = "ProjectmangeHR/DCIM/" + str(user_list[index8]) + "_" + str(rank_list[index8])+".png"
                imgperson8 = Image.open(name_person8)
                resize_imgperson8 = imgperson8.resize((90,90))
                # imgperson3 = Image.open()
                img_person8 = ImageTk.PhotoImage(resize_imgperson8)
                # Developer
                img_p8 = canvas.create_image(415,650, image=img_person8)
                label_Developer_2 = canvas.create_text(425,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_2 = canvas.create_text(425,730, text=str(user_list[index8]),font="supermarket 9",fill='#ffffff')

        elif r == "Marketing Member1" or r == "Marketing member1" or r == "marketing member1": 
                #index rank
                index9 = sl_rank.search(r)
                #img person
                name_person9 = "ProjectmangeHR/DCIM/" + str(user_list[index9]) + "_" + str(rank_list[index9])+".png"
                imgperson9 = Image.open(name_person9)
                resize_imgperson9 = imgperson9.resize((90,90))
                # imgperson3 = Image.open()
                img_person9 = ImageTk.PhotoImage(resize_imgperson9)
                # ฝ่ายขาย
                img_p9 = canvas.create_image(570,650, image=img_person9)
                label_Marketing_1 = canvas.create_text(570,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_1 = canvas.create_text(570,730, text=str(user_list[index9]),font="supermarket 9",fill='#ffffff')
                count_marketing = count_marketing + 1
        elif r == "Marketing Member2" or r == "Marketing member2" or r == "marketing member2": 
                #index rank
                index11 = sl_rank.search(r)
                #img person
                nameperson11 = "ProjectmangeHR/DCIM/" + str(user_list[index11]) + "_" + str(rank_list[index11])+".png"
                imgperson11 = Image.open(nameperson11)
                resize_imgperson11 = imgperson11.resize((90,90))
                # imgperson3 = Image.open()
                img_person11 = ImageTk.PhotoImage(resize_imgperson11)
                # ฝ่ายขาย
                img_p10 = canvas.create_image(695,650, image=img_person11)
                label_Marketing_2 = canvas.create_text(700,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_2 = canvas.create_text(700,730, text=str(user_list[index11]),font="supermarket 9",fill='#ffffff')
elif i == 7:
    print("person "+str(i))
    #พื้นหลัง
    bg = ImageTk.PhotoImage(file="ProjectmangeHR/UI/bg_page1_10.png")
    # bg_label = tk.Label(window,image=bg)
    # bg_label.pack()
    # cancvas
    bg_page = canvas.create_image(0,0, image=bg, anchor=NW) #bg
    for r in rank_list:
        if r == "CEO" or r == "Ceo" or r == "ceo": 
            #index rank
            index1 = sl_rank.search(r)
            #img person
            name_person1 = "ProjectmangeHR/DCIM/" + str(user_list[index1]) + "_" + str(rank_list[index1])+".png"
            imgperson1 = Image.open(name_person1)
            resize_imgperson1 = imgperson1.resize((90,90))
            # imgperson3 = Image.open()
            img_person1 = ImageTk.PhotoImage(resize_imgperson1)
            #ceo
            img_p1 = canvas.create_image(615,110, image=img_person1)
            label_ceo = canvas.create_text(620,200, text=str(user_list[index1]),font="supermarket 16",fill='#ffffff')

        elif r == "Vice Chairman" or r == "Vice chairman" or r == "vice chairman": 
            #index rank
            index2 = sl_rank.search(r)
            #img person
            name_person2 = "ProjectmangeHR/DCIM/" + str(user_list[index2]) + "_" + str(rank_list[index2])+".png"
            imgperson2 = Image.open(name_person2)
            resize_imgperson2 = imgperson2.resize((90,90))
            # imgperson3 = Image.open()
            img_person2 = ImageTk.PhotoImage(resize_imgperson2)
            #รองประธาน
            img_p2 = canvas.create_image(425,230, image=img_person2)
            label_ViceChairman = canvas.create_text(430,290, text="รองประธาน",font="supermarket 16",fill='#ffffff')
            label_name_ViceChairman = canvas.create_text(430,320, text=str(user_list[index2]),font="supermarket 16",fill='#ffffff')

        elif r == "Secretary" or r == "secretary": 
            #index rank
            index3 = sl_rank.search(r)
            #img person
            name_person3 = "ProjectmangeHR/DCIM/" + str(user_list[index3]) + "_" + str(rank_list[index3])+".png"
            imgperson3 = Image.open(name_person3)
            resize_imgperson3 = imgperson3.resize((90,90))
            # imgperson3 = Image.open()
            img_person3 = ImageTk.PhotoImage(resize_imgperson3)
            # เลขา
            img_p3 = canvas.create_image(820,230, image=img_person3)
            label_Secretary = canvas.create_text(820,290, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(820,320, text=str(user_list[index3]),font="supermarket 16",fill='#ffffff')

        elif r == "Development Manager" or r == "Development manager" or r == "development manager": 
            #index rank
            index4 = sl_rank.search(r)
            #img person
            name_person4 = "ProjectmangeHR/DCIM/" + str(user_list[index4]) + "_" + str(rank_list[index4])+".png"
            imgperson4 = Image.open(name_person4)
            resize_imgperson4 = imgperson4.resize((90,90))
            # imgperson3 = Image.open()
            img_person4 = ImageTk.PhotoImage(resize_imgperson4)
            # หัวหน้า Development
            img_p5 = canvas.create_image(320,410, image=img_person4)
            label_Development_manager = canvas.create_text(330,470, text="หัวหน้านักพัฒนา",font="supermarket 16",fill='#ffffff')
            label_name_Development_manager = canvas.create_text(330,500, text=str(user_list[index4]),font="supermarket 16",fill='#ffffff')

        elif r == "Marketing Manager" or r == "Marketing manager" or r == "marketing manager": 
            #index rank
            index5 = sl_rank.search(r)
            #img person
            name_person5 = "ProjectmangeHR/DCIM/" + str(user_list[index5]) + "_" + str(rank_list[index5])+".png"
            imgperson5 = Image.open(name_person5)
            resize_imgperson5 = imgperson5.resize((90,90))
            # imgperson3 = Image.open()
            img_person5 = ImageTk.PhotoImage(resize_imgperson5)
            # หัวหน้า ฝ่ายขาย
            img_p6 = canvas.create_image(625,410, image=img_person5)
            label_Marketing_manager = canvas.create_text(630,470, text="หัวหน้าฝ่ายขาย",font="supermarket 16",fill='#ffffff')
            label_name_Marketing_manager = canvas.create_text(630,500, text=str(user_list[index5]),font="supermarket 16",fill='#ffffff')

        elif r == "Personnel Manager" or r == "Personnel manager" or r == "personnel manager": 
            #index rank
            index6 = sl_rank.search(r)
            #img person
            name_person6 = "ProjectmangeHR/DCIM/" + str(user_list[index6]) + "_" + str(rank_list[index6])+".png"
            imgperson6 = Image.open(name_person6)
            resize_imgperson6 = imgperson6.resize((90,90))
            # imgperson3 = Image.open()
            img_person6 = ImageTk.PhotoImage(resize_imgperson6)
            # ฝ่ายบุคล
            img_p4 = canvas.create_image(940,410, image=img_person6)
            label_Secretary = canvas.create_text(940,470, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(940,500, text=str(user_list[index6]),font="supermarket 16",fill='#ffffff')

        elif r == "Developer Member1" or r == "Developer member1" or r == "developer member1": 
                #index rank
                index7 = sl_rank.search(r)
                #img person
                name_person7 = "ProjectmangeHR/DCIM/" + str(user_list[index7]) + "_" + str(rank_list[index7])+".png"
                imgperson7 = Image.open(name_person7)
                resize_imgperson7 = imgperson7.resize((90,90))
                # imgperson3 = Image.open()
                img_person7 = ImageTk.PhotoImage(resize_imgperson7)
                # Developer
                img_p7 = canvas.create_image(290,650, image=img_person7)
                label_Developer_1 = canvas.create_text(285,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_1 = canvas.create_text(285,730, text=str(user_list[index7]),font="supermarket 9",fill='#ffffff')
                
        elif r == "Developer Member2" or r == "Developer member2" or r == "developer member2": 
                #index rank
                index8 = sl_rank.search(r)
                #img person
                name_person8 = "ProjectmangeHR/DCIM/" + str(user_list[index8]) + "_" + str(rank_list[index8])+".png"
                imgperson8 = Image.open(name_person8)
                resize_imgperson8 = imgperson8.resize((90,90))
                # imgperson3 = Image.open()
                img_person8 = ImageTk.PhotoImage(resize_imgperson8)
                # Developer
                img_p8 = canvas.create_image(415,650, image=img_person8)
                label_Developer_2 = canvas.create_text(425,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_2 = canvas.create_text(425,730, text=str(user_list[index8]),font="supermarket 9",fill='#ffffff')

        elif r == "Marketing Member1" or r == "Marketing member1" or r == "marketing member1": 
                #index rank
                index9 = sl_rank.search(r)
                #img person
                name_person9 = "ProjectmangeHR/DCIM/" + str(user_list[index9]) + "_" + str(rank_list[index9])+".png"
                imgperson9 = Image.open(name_person9)
                resize_imgperson9 = imgperson9.resize((90,90))
                # imgperson3 = Image.open()
                img_person9 = ImageTk.PhotoImage(resize_imgperson9)
                # ฝ่ายขาย
                img_p9 = canvas.create_image(570,650, image=img_person9)
                label_Marketing_1 = canvas.create_text(570,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_1 = canvas.create_text(570,730, text=str(user_list[index9]),font="supermarket 9",fill='#ffffff')
                count_marketing = count_marketing + 1
        elif r == "Marketing Member2" or r == "Marketing member2" or r == "marketing member2": 
                #index rank
                index11 = sl_rank.search(r)
                #img person
                nameperson11 = "ProjectmangeHR/DCIM/" + str(user_list[index11]) + "_" + str(rank_list[index11])+".png"
                imgperson11 = Image.open(nameperson11)
                resize_imgperson11 = imgperson11.resize((90,90))
                # imgperson3 = Image.open()
                img_person11 = ImageTk.PhotoImage(resize_imgperson11)
                # ฝ่ายขาย
                img_p10 = canvas.create_image(695,650, image=img_person11)
                label_Marketing_2 = canvas.create_text(700,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_2 = canvas.create_text(700,730, text=str(user_list[index11]),font="supermarket 9",fill='#ffffff')
elif i == 6:
    print("person "+str(i))
    #พื้นหลัง
    bg = ImageTk.PhotoImage(file="ProjectmangeHR/UI/bg_page1_10.png")
    # bg_label = tk.Label(window,image=bg)
    # bg_label.pack()
    # cancvas
    bg_page = canvas.create_image(0,0, image=bg, anchor=NW) #bg
    for r in rank_list:
        if r == "CEO" or r == "Ceo" or r == "ceo": 
            #index rank
            index1 = sl_rank.search(r)
            #img person
            name_person1 = "ProjectmangeHR/DCIM/" + str(user_list[index1]) + "_" + str(rank_list[index1])+".png"
            imgperson1 = Image.open(name_person1)
            resize_imgperson1 = imgperson1.resize((90,90))
            # imgperson3 = Image.open()
            img_person1 = ImageTk.PhotoImage(resize_imgperson1)
            #ceo
            img_p1 = canvas.create_image(615,110, image=img_person1)
            label_ceo = canvas.create_text(620,200, text=str(user_list[index1]),font="supermarket 16",fill='#ffffff')

        elif r == "Vice Chairman" or r == "Vice chairman" or r == "vice chairman": 
            #index rank
            index2 = sl_rank.search(r)
            #img person
            name_person2 = "ProjectmangeHR/DCIM/" + str(user_list[index2]) + "_" + str(rank_list[index2])+".png"
            imgperson2 = Image.open(name_person2)
            resize_imgperson2 = imgperson2.resize((90,90))
            # imgperson3 = Image.open()
            img_person2 = ImageTk.PhotoImage(resize_imgperson2)
            #รองประธาน
            img_p2 = canvas.create_image(425,230, image=img_person2)
            label_ViceChairman = canvas.create_text(430,290, text="รองประธาน",font="supermarket 16",fill='#ffffff')
            label_name_ViceChairman = canvas.create_text(430,320, text=str(user_list[index2]),font="supermarket 16",fill='#ffffff')

        elif r == "Secretary" or r == "secretary": 
            #index rank
            index3 = sl_rank.search(r)
            #img person
            name_person3 = "ProjectmangeHR/DCIM/" + str(user_list[index3]) + "_" + str(rank_list[index3])+".png"
            imgperson3 = Image.open(name_person3)
            resize_imgperson3 = imgperson3.resize((90,90))
            # imgperson3 = Image.open()
            img_person3 = ImageTk.PhotoImage(resize_imgperson3)
            # เลขา
            img_p3 = canvas.create_image(820,230, image=img_person3)
            label_Secretary = canvas.create_text(820,290, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(820,320, text=str(user_list[index3]),font="supermarket 16",fill='#ffffff')

        elif r == "Development Manager" or r == "Development manager" or r == "development manager": 
            #index rank
            index4 = sl_rank.search(r)
            #img person
            name_person4 = "ProjectmangeHR/DCIM/" + str(user_list[index4]) + "_" + str(rank_list[index4])+".png"
            imgperson4 = Image.open(name_person4)
            resize_imgperson4 = imgperson4.resize((90,90))
            # imgperson3 = Image.open()
            img_person4 = ImageTk.PhotoImage(resize_imgperson4)
            # หัวหน้า Development
            img_p5 = canvas.create_image(320,410, image=img_person4)
            label_Development_manager = canvas.create_text(330,470, text="หัวหน้านักพัฒนา",font="supermarket 16",fill='#ffffff')
            label_name_Development_manager = canvas.create_text(330,500, text=str(user_list[index4]),font="supermarket 16",fill='#ffffff')

        elif r == "Marketing Manager" or r == "Marketing manager" or r == "marketing manager": 
            #index rank
            index5 = sl_rank.search(r)
            #img person
            name_person5 = "ProjectmangeHR/DCIM/" + str(user_list[index5]) + "_" + str(rank_list[index5])+".png"
            imgperson5 = Image.open(name_person5)
            resize_imgperson5 = imgperson5.resize((90,90))
            # imgperson3 = Image.open()
            img_person5 = ImageTk.PhotoImage(resize_imgperson5)
            # หัวหน้า ฝ่ายขาย
            img_p6 = canvas.create_image(625,410, image=img_person5)
            label_Marketing_manager = canvas.create_text(630,470, text="หัวหน้าฝ่ายขาย",font="supermarket 16",fill='#ffffff')
            label_name_Marketing_manager = canvas.create_text(630,500, text=str(user_list[index5]),font="supermarket 16",fill='#ffffff')

        elif r == "Personnel Manager" or r == "Personnel manager" or r == "personnel manager": 
            #index rank
            index6 = sl_rank.search(r)
            #img person
            name_person6 = "ProjectmangeHR/DCIM/" + str(user_list[index6]) + "_" + str(rank_list[index6])+".png"
            imgperson6 = Image.open(name_person6)
            resize_imgperson6 = imgperson6.resize((90,90))
            # imgperson3 = Image.open()
            img_person6 = ImageTk.PhotoImage(resize_imgperson6)
            # ฝ่ายบุคล
            img_p4 = canvas.create_image(940,410, image=img_person6)
            label_Secretary = canvas.create_text(940,470, text="เลขา",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(940,500, text=str(user_list[index6]),font="supermarket 16",fill='#ffffff')

        elif r == "Developer Member1" or r == "Developer member1" or r == "developer member1": 
                #index rank
                index7 = sl_rank.search(r)
                #img person
                name_person7 = "ProjectmangeHR/DCIM/" + str(user_list[index7]) + "_" + str(rank_list[index7])+".png"
                imgperson7 = Image.open(name_person7)
                resize_imgperson7 = imgperson7.resize((90,90))
                # imgperson3 = Image.open()
                img_person7 = ImageTk.PhotoImage(resize_imgperson7)
                # Developer
                img_p7 = canvas.create_image(290,650, image=img_person7)
                label_Developer_1 = canvas.create_text(285,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_1 = canvas.create_text(285,730, text=str(user_list[index7]),font="supermarket 9",fill='#ffffff')
                
        elif r == "Developer Member2" or r == "Developer member2" or r == "developer member2": 
                #index rank
                index8 = sl_rank.search(r)
                #img person
                name_person8 = "ProjectmangeHR/DCIM/" + str(user_list[index8]) + "_" + str(rank_list[index8])+".png"
                imgperson8 = Image.open(name_person8)
                resize_imgperson8 = imgperson8.resize((90,90))
                # imgperson3 = Image.open()
                img_person8 = ImageTk.PhotoImage(resize_imgperson8)
                # Developer
                img_p8 = canvas.create_image(415,650, image=img_person8)
                label_Developer_2 = canvas.create_text(425,705, text="นักพัฒนา",font="supermarket 16",fill='#ffffff')
                label_name_Developer_2 = canvas.create_text(425,730, text=str(user_list[index8]),font="supermarket 9",fill='#ffffff')

        elif r == "Marketing Member1" or r == "Marketing member1" or r == "marketing member1": 
                #index rank
                index9 = sl_rank.search(r)
                #img person
                name_person9 = "ProjectmangeHR/DCIM/" + str(user_list[index9]) + "_" + str(rank_list[index9])+".png"
                imgperson9 = Image.open(name_person9)
                resize_imgperson9 = imgperson9.resize((90,90))
                # imgperson3 = Image.open()
                img_person9 = ImageTk.PhotoImage(resize_imgperson9)
                # ฝ่ายขาย
                img_p9 = canvas.create_image(570,650, image=img_person9)
                label_Marketing_1 = canvas.create_text(570,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_1 = canvas.create_text(570,730, text=str(user_list[index9]),font="supermarket 9",fill='#ffffff')
                count_marketing = count_marketing + 1
        elif r == "Marketing Member2" or r == "Marketing member2" or r == "marketing member2": 
                #index rank
                index11 = sl_rank.search(r)
                #img person
                nameperson11 = "ProjectmangeHR/DCIM/" + str(user_list[index11]) + "_" + str(rank_list[index11])+".png"
                imgperson11 = Image.open(nameperson11)
                resize_imgperson11 = imgperson11.resize((90,90))
                # imgperson3 = Image.open()
                img_person11 = ImageTk.PhotoImage(resize_imgperson11)
                # ฝ่ายขาย
                img_p10 = canvas.create_image(695,650, image=img_person11)
                label_Marketing_2 = canvas.create_text(700,705, text="ฝ่ายขาย",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_2 = canvas.create_text(700,730, text=str(user_list[index11]),font="supermarket 9",fill='#ffffff')
else:
    print("person "+str(i))
    #พื้นหลัง
    bg = ImageTk.PhotoImage(file="ProjectmangeHR/UI/bg_page1_12.png")
    # bg_label = tk.Label(window,image=bg)
    # bg_label.pack()
    # cancvas
    bg_page = canvas.create_image(0,0, image=bg, anchor=NW) #bg
    for r in rank_list:
        if r == "ประธานบริษัท": 
            #index rank
            index1 = sl_rank.search(r)
            #img person
            name_person1 = "ProjectmangeHR/DCIM/" + str(user_list[index1]) + "_" + str(rank_list[index1])+".png"
            imgperson1 = Image.open(name_person1)
            resize_imgperson1 = imgperson1.resize((90,90))
            # imgperson3 = Image.open()
            img_person1 = ImageTk.PhotoImage(resize_imgperson1)
            #ceo
            img_p1 = canvas.create_image(615,110, image=img_person1)
            label_ceo = canvas.create_text(620,200, text=str(user_list[index1]),font="supermarket 16",fill='#ffffff')

        elif r == "แผนกบุคคล": 
            #index rank
            index2 = sl_rank.search(r)
            #img person
            name_person2 = "ProjectmangeHR/DCIM/" + str(user_list[index2]) + "_" + str(rank_list[index2])+".png"
            imgperson2 = Image.open(name_person2)
            resize_imgperson2 = imgperson2.resize((90,90))
            # imgperson3 = Image.open()
            img_person2 = ImageTk.PhotoImage(resize_imgperson2)
            #รองประธาน
            img_p2 = canvas.create_image(425,230, image=img_person2)
            label_ViceChairman = canvas.create_text(430,290, text="แผนกบุคคล",font="supermarket 16",fill='#ffffff')
            label_name_ViceChairman = canvas.create_text(430,320, text=str(user_list[index2]),font="supermarket 16",fill='#ffffff')

        elif r == "รองประธาน": 
            #index rank
            index3 = sl_rank.search(r)
            #img person
            name_person3 = "ProjectmangeHR/DCIM/" + str(user_list[index3]) + "_" + str(rank_list[index3])+".png"
            imgperson3 = Image.open(name_person3)
            resize_imgperson3 = imgperson3.resize((90,90))
            # imgperson3 = Image.open()
            img_person3 = ImageTk.PhotoImage(resize_imgperson3)
            # เลขา
            img_p3 = canvas.create_image(820,230, image=img_person3)
            label_Secretary = canvas.create_text(820,290, text="รองประธาน",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(820,320, text=str(user_list[index3]),font="supermarket 16",fill='#ffffff')

        elif r == "พนักงานการตลาด1": 
            #index rank
            index4 = sl_rank.search(r)
            #img person
            name_person4 = "ProjectmangeHR/DCIM/" + str(user_list[index4]) + "_" + str(rank_list[index4])+".png"
            imgperson4 = Image.open(name_person4)
            resize_imgperson4 = imgperson4.resize((90,90))
            # imgperson3 = Image.open()
            img_person4 = ImageTk.PhotoImage(resize_imgperson4)
            # หัวหน้า Development
            img_p5 = canvas.create_image(320,410, image=img_person4)
            label_Development_manager = canvas.create_text(330,470, text="พนักงานการตลาด",font="supermarket 16",fill='#ffffff')
            label_name_Development_manager = canvas.create_text(330,500, text=str(user_list[index4]),font="supermarket 16",fill='#ffffff')

        elif r == "พนักงานการตลาด2": 
            #index rank
            index5 = sl_rank.search(r)
            #img person
            name_person5 = "ProjectmangeHR/DCIM/" + str(user_list[index5]) + "_" + str(rank_list[index5])+".png"
            imgperson5 = Image.open(name_person5)
            resize_imgperson5 = imgperson5.resize((90,90))
            # imgperson3 = Image.open()
            img_person5 = ImageTk.PhotoImage(resize_imgperson5)
            # หัวหน้า ฝ่ายขาย
            img_p6 = canvas.create_image(625,410, image=img_person5)
            label_Marketing_manager = canvas.create_text(630,470, text="พนักงานการตลาด",font="supermarket 16",fill='#ffffff')
            label_name_Marketing_manager = canvas.create_text(630,500, text=str(user_list[index5]),font="supermarket 16",fill='#ffffff')

        elif r == "ผู้จัดการ": 
            #index rank
            index6 = sl_rank.search(r)
            #img person
            name_person6 = "ProjectmangeHR/DCIM/" + str(user_list[index6]) + "_" + str(rank_list[index6])+".png"
            imgperson6 = Image.open(name_person6)
            resize_imgperson6 = imgperson6.resize((90,90))
            # imgperson3 = Image.open()
            img_person6 = ImageTk.PhotoImage(resize_imgperson6)
            # ฝ่ายบุคล
            img_p4 = canvas.create_image(940,410, image=img_person6)
            label_Secretary = canvas.create_text(940,470, text="ผู้จัดการ",font="supermarket 16",fill='#ffffff')
            label_name_Secretary = canvas.create_text(948,500, text=str(user_list[index6]),font="supermarket 16",fill='#ffffff')

        elif r == "การบัญชี": 
                #index rank
                index7 = sl_rank.search(r)
                #img person
                name_person7 = "ProjectmangeHR/DCIM/" + str(user_list[index7]) + "_" + str(rank_list[index7])+".png"
                imgperson7 = Image.open(name_person7)
                resize_imgperson7 = imgperson7.resize((90,90))
                # imgperson3 = Image.open()
                img_person7 = ImageTk.PhotoImage(resize_imgperson7)
                # Developer
                img_p7 = canvas.create_image(290,650, image=img_person7)
                label_Developer_1 = canvas.create_text(285,705, text="การบัญชี",font="supermarket 16",fill='#ffffff')
                label_name_Developer_1 = canvas.create_text(285,730, text=str(user_list[index7]),font="supermarket 9",fill='#ffffff')
                
        elif r == "ผู้ช่วยผู้จัดการ1": 
                #index rank
                index8 = sl_rank.search(r)
                #img person
                name_person8 = "ProjectmangeHR/DCIM/" + str(user_list[index8]) + "_" + str(rank_list[index8])+".png"
                imgperson8 = Image.open(name_person8)
                resize_imgperson8 = imgperson8.resize((90,90))
                # imgperson3 = Image.open()
                img_person8 = ImageTk.PhotoImage(resize_imgperson8)
                # Developer
                img_p8 = canvas.create_image(850,650, image=img_person8)
                label_Developer_2 = canvas.create_text(847,705, text="ผู้ช่วยผู้จัดการ",font="supermarket 16",fill='#ffffff')
                label_name_Developer_2 = canvas.create_text(845,730, text=str(user_list[index8]),font="supermarket 9",fill='#ffffff')
        
        elif r == "ผู้ช่วยผู้จัดการ2": 
                #index rank
                index12 = sl_rank.search(r)
                #img person
                name_person12 = "ProjectmangeHR/DCIM/" + str(user_list[index12]) + "_" + str(rank_list[index12])+".png"
                imgperson12 = Image.open(name_person12)
                resize_imgperson12 = imgperson12.resize((90,90))
                # imgperson3 = Image.open()
                img_person12 = ImageTk.PhotoImage(resize_imgperson12)
                # Developer
                img_p12 = canvas.create_image(975,650, image=img_person12)
                label_Developer_3 = canvas.create_text(977,705, text="ผู้ช่วยผู้จัดการ",font="supermarket 16",fill='#ffffff')
                label_name_Developer_3 = canvas.create_text(980,730, text=str(user_list[index12]),font="supermarket 9",fill='#ffffff')

        elif r == "หัวหน้าแม่บ้าน": 
                #index rank
                index9 = sl_rank.search(r)
                #img person
                name_person9 = "ProjectmangeHR/DCIM/" + str(user_list[index9]) + "_" + str(rank_list[index9])+".png"
                imgperson9 = Image.open(name_person9)
                resize_imgperson9 = imgperson9.resize((90,90))
                # imgperson3 = Image.open()
                img_person9 = ImageTk.PhotoImage(resize_imgperson9)
                # ฝ่ายขาย
                img_p9 = canvas.create_image(570,650, image=img_person9)
                label_Marketing_1 = canvas.create_text(570,705, text="หัวหน้าแม่บ้าน",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_1 = canvas.create_text(570,730, text=str(user_list[index9]),font="supermarket 9",fill='#ffffff')
                count_marketing = count_marketing + 1
        elif r == "แม่บ้าน": 
                #index rank
                index11 = sl_rank.search(r)
                #img person
                nameperson11 = "ProjectmangeHR/DCIM/" + str(user_list[index11]) + "_" + str(rank_list[index11])+".png"
                imgperson11 = Image.open(nameperson11)
                resize_imgperson11 = imgperson11.resize((90,90))
                # imgperson3 = Image.open()
                img_person11 = ImageTk.PhotoImage(resize_imgperson11)
                # ฝ่ายขาย
                img_p10 = canvas.create_image(695,650, image=img_person11)
                label_Marketing_2 = canvas.create_text(700,705, text="แม่บ้าน",font="supermarket 16",fill='#ffffff')
                label_name_Marketing_2 = canvas.create_text(700,730, text=str(user_list[index11]),font="supermarket 9",fill='#ffffff')






#พื้นหลัง
# bg = ImageTk.PhotoImage(file="ProjectmangeHR/UI/bg_page1_10.png")
# bg_label = tk.Label(window,image=bg)
# bg_label.pack()



#img person
# name_person1 = "ProjectmangeHR/DCIM/" + str(user_list[0]) + "_" + str(rank_list[0])+".png"
# imgperson1 = Image.open(name_person1)
# resize_imgperson1 = imgperson1.resize((90,90))

# name_person2 = "ProjectmangeHR/DCIM/" + str(user_list[1]) + "_" + str(rank_list[1])+".png"
# imgperson2 = Image.open(name_person2)
# resize_imgperson2 = imgperson2.resize((90,90))

# name_person3 = "ProjectmangeHR/DCIM/" + str(user_list[2]) + "_" + str(rank_list[2])+".png"
# imgperson3 = Image.open(name_person3)
# resize_imgperson3 = imgperson3.resize((90,90))

# name_person4 = "ProjectmangeHR/DCIM/" + str(user_list[3]) + "_" + str(rank_list[3])+".png"
# imgperson4 = Image.open(name_person4)
# resize_imgperson4 = imgperson4.resize((90,90))

# name_person5 = "ProjectmangeHR/DCIM/" + str(user_list[4]) + "_" + str(rank_list[4])+".png"
# imgperson5 = Image.open(name_person5)
# resize_imgperson5 = imgperson5.resize((90,90))

# name_person6 = "ProjectmangeHR/DCIM/" + str(user_list[5]) + "_" + str(rank_list[5])+".png"
# imgperson6 = Image.open(name_person6)
# resize_imgperson6 = imgperson6.resize((90,90))

# name_person7 = "ProjectmangeHR/DCIM/" + str(user_list[6]) + "_" + str(rank_list[6])+".png"
# imgperson7 = Image.open(name_person7)
# resize_imgperson7 = imgperson7.resize((90,90))

# name_person8 = "ProjectmangeHR/DCIM/" + str(user_list[7]) + "_" + str(rank_list[7])+".png"
# imgperson8 = Image.open(name_person8)
# resize_imgperson8 = imgperson8.resize((90,90))

# name_person9 = "ProjectmangeHR/DCIM/" + str(user_list[8]) + "_" + str(rank_list[8])+".png"
# imgperson9 = Image.open(name_person9)
# resize_imgperson9 = imgperson9.resize((90,90))

# name_person10 = "ProjectmangeHR/DCIM/" + str(user_list[9]) + "_" + str(rank_list[9])+".png"
# imgperson10 = Image.open(name_person10)
# resize_imgperson10 = imgperson10.resize((90,90))



# imgperson3 = Image.open()
# img_person1 = ImageTk.PhotoImage(resize_imgperson1)
# img_person2 = ImageTk.PhotoImage(resize_imgperson2)
# img_person3 = ImageTk.PhotoImage(resize_imgperson3)
# img_person4 = ImageTk.PhotoImage(resize_imgperson4)
# img_person5 = ImageTk.PhotoImage(resize_imgperson5)
# img_person6 = ImageTk.PhotoImage(resize_imgperson6)
# img_person7 = ImageTk.PhotoImage(resize_imgperson7)
# img_person8 = ImageTk.PhotoImage(resize_imgperson8)
# img_person9 = ImageTk.PhotoImage(resize_imgperson9)
# img_person10 = ImageTk.PhotoImage(resize_imgperson10)








#ปุ่มเปลี่ยนหน้า
bg_btpage2 = PhotoImage(file="ProjectmangeHR/UI/bt_page2.png")
bt_page2 = tk.Button(window,image=bg_btpage2,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page2,cursor="hand2")
bt_page2.place(x=38,y=160)

bg_btpage3 = PhotoImage(file="ProjectmangeHR/UI/bt_page3.png")
bt_page3 = tk.Button(window,image=bg_btpage3,bg="#2c333e",activebackground="#2c333e",borderwidth=0,command=page3,cursor="hand2")
bt_page3.place(x=35,y=220)





canvas.place(x=0,y=0,width=1048,height=1048)

window.resizable(False, False)
window.geometry("1048x786+250+5")
window.title("ระบบจัดตำแหน่งและพนักงาน")
# window.iconbitmap(r'ui/icon_app_OSE_icon.ico') #icon
window.mainloop()