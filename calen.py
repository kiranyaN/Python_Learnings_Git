#final program
from tkinter import *
from datetime import *
month = list(range(1,13))
year = list(range(1980,2021))
date1 = list(range(1,31))

master = Tk()
master.geometry("400x300")
msg=StringVar()
variable1 = StringVar(master)
variable2 = StringVar(master)
variable3 = StringVar(master)
variable2.set(month[0])
variable3.set(year[0])
variable1.set(date1[0])
w1 = OptionMenu(master, variable1, *date1)
w2 = OptionMenu(master, variable2, *month)
w3 = OptionMenu(master, variable3, *year)

w1.place(x=20,y=120)
w2.place(x=100,y=120)
w3.place(x=200,y=120)
def disp():

    day1 = int(variable1.get())
    month1 = int(variable2.get())
    year1 = int(variable3.get())
    d1 = date.today() - date(year1, month1, day1)
    msg.set(d1)
    print(d1)
    return

button = Button(master, text="Calculate", command=disp)
button.place(x=80,y=180)#wait
L=Label(master,textvariable=msg,font="times 20",fg="red")
L.place(x=100,y=220)
mainloop()
