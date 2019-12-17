#names correct ga ivvu
from tkinter import *
def display():
    text=e.get()
    msg.set("input is:"+text)
    return

root=Tk()
#root.title("GUI")
root.geometry("400x300")
msg=StringVar()
#custom =('Times',5)
e=Entry(root,font="times 20")
#e=Entry(root,font=custom)
e.pack()
b = Button(root,text="Display",font="times 25",command=display)
b.pack()
L=Label(root,textvariable=msg,font="times 40",fg="red")
L.place(x=200,y=500)

root.mainloop()
