from tkinter import *
from tkinter import ttk

import sqlite3

conn = sqlite3.connect('Book.sqlite3') # สร้างไฟล์ฐานข้อมูล
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS rentbook(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            namebook Text,
            nameauthors Text,
            namedateofpublication Text,
            namepublisher Text
            )""")


def Insert_Nameofbook(namebook,nameauthors,namedateofpublication,namepublisher):
    with conn:
        command = 'INSERT INTO rentbook VALUES (?,?,?,?,?)'
        c.execute(command,(None,namebook,nameauthors,namedateofpublication,namepublisher))
        conn.commit() #Save data
        print('Saved')

#Insert_Nameofbook('การเขียนโปรเเกรมด้วย Python ฉบับพื้นฐาน','บัญชา ปะสีละเตสัง','2022','ซีเอ็ดยูเคชั่น, บมจ.')

def View_namebook():
    # READ
    with conn:
        command = 'SELECT * FROM rentbook'
        c.execute(command)
        ressult = c.fetchall()
    # print(ressult)
    return ressult
data = View_namebook()
# print(data[0][1],data[0][2])


GUI = Tk()
GUI.title('โปรแกรมยืมหนังสือ')


w = 910
h = 600

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2) - 20

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')


FONT1 = ('Angsana New',25)
FONT2 = ('Angsana New',19)

#################### Config TAB ##################
Tab = ttk.Notebook(GUI)
Tab.pack(fill=BOTH,expand=1)

T1 = Frame(Tab)
T2 = Frame(Tab)

icon_tab1 = PhotoImage(file='tab1.png')
icon_tab2 = PhotoImage(file='tab2.png')
Tab.add(T1,text='บันทึกข้อมูลหนังสือ',image=icon_tab1,compound='left')
Tab.add(T2,text='ยืมหนังสือ',image=icon_tab2,compound='left')

#################### Config TAB ##################

########### Tab1 ###############

L1  = Label(T1,text = 'เพิ่มหนังสือ',font=FONT1,fg='green')
L1.pack()

frame1 = Frame(T1)
frame1.place(x=150,y=50)



L2 = Label(frame1,text='ชื่อหนังสือ',font=FONT1,fg='green').grid(row=0,column=0,ipadx=5)

V_Namebook = StringVar()
E1 = ttk.Entry(frame1,textvariable=V_Namebook,font=FONT2).grid(row=0,column=1,ipadx=5)

L3 = Label(frame1,text='ผู้แต่ง',font=FONT1,fg='green').grid(row=0,column=2,ipadx=5)

V_Authors = StringVar()
E2 = ttk.Entry(frame1,textvariable=V_Authors,font=FONT2).grid(row=0,column=3,ipadx=5)

L4 = Label(frame1,text='ปีพิมพ์',font=FONT1,fg='green').grid(row=1,column=0,ipadx=5)
DateOfPublication = StringVar()
E3 = ttk.Entry(frame1,text=DateOfPublication,font=FONT2).grid(row=1,column=1,ipadx=5)

L5 = Label(frame1,text='สำนักพิมพ์',font=FONT1,fg='green').grid(row=1,column=2,ipadx=5)
V_Publisher = StringVar()
E4 = ttk.Entry(frame1,textvariable=V_Publisher,font=FONT2).grid(row=1,column=3,ipadx=5)

def Save_Book():

    Name_Book = V_Namebook.get()
    Name_Authors = V_Authors.get()
    Name_DateOfPublication = DateOfPublication.get()
    Name_V_Publisher = V_Publisher.get()
    Insert_Nameofbook(Name_Book,Name_Authors,Name_DateOfPublication,Name_V_Publisher)
    V_Namebook.set('')
    V_Authors.set('')
    DateOfPublication.set('')
    V_Publisher.set('')


 
B1 = ttk.Button(frame1,text='บันทึกข้อมูล',command=Save_Book).grid(row=3,column=2,ipadx=20,ipady=10,pady=5)

header = ['ลำดับ','ชื่อหนังสือ','ผู้แต่ง','ปีพิมพ์','สำนักพิมพ์']
hwidth = [50,400,150,80,200]

table = ttk.Treeview(T1, columns=header, show='headings', height=8)
table.place(x=10,y=250)

# resize
style = ttk.Style()
style.configure('Treeview.Heading',font=(None,15))
style.configure('Treeview',font=(None,13),rowheight=30)

for h,w in zip(header,hwidth):
    table.column(h,width=w)
    table.heading(h,text=h)

for i,d in enumerate(data,start=1):
    #d.insert(0,i)
    #table.insert('','end',values=d)
    table.insert('','end',values=[d[0],d[1],d[2],d[3],d[4]])


########### Tab1 ###############

########### Tab2 ###############
T2L1  = Label(T2,text = 'โปรแกรมยืมคืนหนังสือ',font=FONT1,fg='green').pack()

frame2 = Frame(T2)
frame2.place(x=10,y=50)

T2L2  = Label(frame2,text = 'ชื่อ',font=FONT1,fg='green').grid(row =0 ,column = 0)
T2E1 = ttk.Entry(frame2,font=FONT2).grid(row=0,column=1)

T2L3  = Label(frame2,text = 'นามสกุล',font=FONT1,fg='green').grid(row = 0 , column = 2)
T2E2 = ttk.Entry(frame2,font=FONT2).grid(row=0,column=3)


T2L4 = Label(frame2,text='บัตรประชาชน',font=FONT1,fg='green').grid(row=0,column=4)
T2E3 = ttk.Entry(frame2,font=FONT2).grid(row=0,column=5)

T2L5 = Label(frame2,text='โทร',font=FONT1,fg='green').grid(row=1,column=0)
T2E4 = ttk.Entry(frame2,font=FONT2).grid(row=1,column=1)

T2L6 = Label(frame2,text='อีเมล์',font=FONT1,fg='green').grid(row=1,column=2)
T2E5 = ttk.Entry(frame2,font=FONT2).grid(row=1,column=3)

T2L6 = Label(frame2,text='ชื่อหนังสือ',font=FONT1,fg='green').grid(row=1,column=4)
T2E5 = ttk.Entry(frame2,font=FONT2).grid(row=1,column=5)

T2B1 = ttk.Button(frame2,text='ค้นหา').grid(row=1,column=6,ipadx=4,ipady=9)

T2L6 = Label(frame2,text='ผู้แต่ง',font=FONT1,fg='green').grid(row=2,column=0)

authors = ttk.Combobox(frame2, width = 24)

names = []
for i in data:
    names.append(i[2])
#print(names)
authors['values'] = names

authors.grid(row = 2,column = 1,padx=10,pady=30)
authors.current()

T2B1 = ttk.Button(frame2,text='บันทึกข้อมูล').grid(row=2,column=3,ipadx=20,ipady=10,pady=5)

########### Tab2 ###############

GUI.mainloop()