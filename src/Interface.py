import os

import Capture1
import check_camera
import Train_Image
import Recognize1
from functools import partial
from tkinter import *

root = Tk()

root.geometry('500x400')

def enterdata():
    root2=Tk()
    root2.geometry('500x400')
    L1 = Label(root2, text="Roll Number")
    L1.grid(row=1, column=0)

    E1 = Entry(root2, bd=5)
    E1.grid(row=1, column=1)

    L2 = Label(root2, text="Name")
    L2.grid(row=2, column=0)

    E2 = Entry(root2, bd=5)
    E2.grid(row=2, column=1)

    L3 = Label(root2, text="Gender")
    L3.grid(row=3, column=0)

    E3 = Entry(root2, bd=5)
    E3.grid(row=3, column=1)

    L4 = Label(root2, text="Academic Year")
    L4.grid(row=4, column=0)

    E4 = Entry(root2, bd=5)
    E4.grid(row=4, column=1)

    L5 = Label(root2, text="Branch")
    L5.grid(row=5, column=0)

    E5 = Entry(root2, bd=5)
    E5.grid(row=5, column=1)

    L6 = Label(root2, text="Section")
    L6.grid(row=6, column=0)

    E6 = Entry(root2, bd=5)
    E6.grid(row=6, column=1)



    import Capture1
    def passdata():
        Capture1.takeImages(E1.get(),E2.get(), E3.get(),E4.get(), E5.get(),E6.get())

    btnx = Button(root2, text = 'Capture Images', bd = '5',command = passdata)
    btnx.grid(row = 7, column = 0)


btn = Button(root, text = 'Capture Images', bd = '5',command = enterdata)
btn.grid(row = 1, column = 1)

btn2 = Button(root, text = 'Store Images', bd = '5',command = Train_Image.TrainImages)
btn2.grid(row = 1, column = 2)

btn3 = Button(root, text = 'Take Attendance', bd = '5',command=lambda: Recognize1.recognize_attendence())
btn3.grid(row = 1, column = 3)

root.mainloop()
