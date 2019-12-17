from datetime import *
from tkinter import *



def disp():
    year1 = int(e1.get())#int(input('Enter year  '))
    month1 = int(e2.get())#int(input('Enter month    '))
    day1 = int(e3.get())#int(input('Enter day    '))
    d1 = date.today() - date(year1, month1, day1)
    msg.set(d1)
    print(d1)
    return

root=Tk()
root.title("Calculate age in days ")
root.geometry("400x300")
msg=StringVar()
custom =('Times',20)

Year=Label(root,text="Year:",font="times 23")
Month=Label(root,text="Month:",font="times 23")
Day=Label(root,text="Day:",font="times 23")


e1=Entry(root,font="times 23")
e2=Entry(root,font="times 23")
e3=Entry(root,font="times 23")

Year.grid(row=0,column=0)
e1.grid(row=0,column=1)
Month.grid(row=1,column=0)
e2.grid(row=1,column=1)
Day.grid(row=2,column=0)
e3.grid(row=2,column=1)

b = Button(root,text="Calculate",font="times 15",command=disp)
b.place(x=80,y=120)

L=Label(root,textvariable=msg,font="times 20",fg="red")
L.place(x=80,y=160)

root.mainloop()

