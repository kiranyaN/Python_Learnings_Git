#names correct ga ivvu edo okati le
#edo okati kadu
#import tkinter
from tkinter import *

def disp():
    f = e1.get()
    l = e2.get()
    print("button clicked...",f,l)
    return

root=Tk()
fn=Label(root,text="first name:",font="times 23")
ln=Label(root,text="last name:",font="times 23")

e1=Entry(root,font="times 23")
e2=Entry(root,font="times 23")

b1 = Button(root,text="Display",font="times 25",command=disp)
b2 = Button(root,text="exit",font="times 25",command=quit)

fn.grid(row=0,column=0)
e1.grid(row=0,column=1)
ln.grid(row=1,column=0)
e2.grid(row=1,column=1)
b1.grid(row=2,column=0)
b2.grid(row=2,column=1)

root.mainloop()

#hello spaces ok ..no problem ..e1 ante??/
#entry feild ani