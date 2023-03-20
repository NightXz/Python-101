from tkinter import *
from tkinter import ttk #Theme of tk
from tkinter import messagebox

GUI = Tk()  #  นี่คือหน้าจอหลักของโปรเเกรม
GUI.title('โปรเเกรมบันทึกของข้อมูล')  #  นี่คือชื่อโปรเเกรม
GUI.geometry('500x400')  #  นี่คือขนาดของโปรเเกรม

L1 = Label(GUI,text= ' โปรเเกรมบันทึกความรู้ ' ,font('Angsana New',30),fg='green')
L1.place(x=30,y=20)
##################
def Button2() :
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี ',text)

FB1 = Frame(GUI)  #คล้ายกระดาน
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text = 'เงินมีอยู่กี่บาท',command=Button2)
#B2.(ipadx=20,ipady=20)
B2.pack(ipadx=20,ipady=20,)
##################
def Button3() :
    text = 'Python 101,Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 กพ. ',text)

FB2 = Frame(GUI)  #คล้ายกระดาน
FB2.place(x=100,y=300)
B3 = ttk.Button(FB1,text = 'เงินมีอยู่กี่บาท',command=Button2)
#B3.(ipadx=20,ipady=20)
B3.pack(ipadx=20,ipady=20,)

GUI.mainloop()
