from tkinter  import *
from tkinter import ttk,messagebox

GUI = Tk()

GUI.geometry('500x500')
GUI.title('โปรแกรมคำนวน')

L = ttk.Label(GUI,text='โปรแกรมหารกัน',font=('Angsana New',30))
L.pack()

L1 = ttk.Label(GUI,text='ราคาอาหารทั้งหมด',font=('Angsana New',20))
L1.pack()

v_total = StringVar() # StringVar ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(GUI,textvariable=v_total,font=('Angsana New',20))
E1.pack(pady=10)

L1 = ttk.Label(GUI,text='มากันกี่คน',font=('Angsana New',30))
L1.pack()

v_person = StringVar() # StringVar ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E2 = ttk.Entry(GUI,textvariable=v_person,font=('Angsana New',20))
E2.pack(pady=10)

def Calculate():
    total = float(v_total.get())
    person = int(v_person.get())
    calc = total / person
    # print('แบ่งจ่ายคนละ {:.2f} บาท'.format(calc))
    text = 'รวมทั้งหมด {} บาท จำนวน {} คน ({:,.2f} ต่อคน)'.format(total,person,calc)
    v_result.set(text)
    messagebox.showinfo('','ตกลง')

B1 = ttk.Button(GUI,text='calculate',command=Calculate)
B1.pack(pady=10,ipadx=20,ipady=10)

v_result = StringVar()
result = ttk.Label(GUI,textvariable=v_result,font=('Angsana New',25),foreground='green')
result.pack(pady=20)

def Close():
    GUI.quit()

B2 = ttk.Button(GUI,text='X',width=5,command=Close)
B2.place(x=450,y=450)

GUI.mainloop()