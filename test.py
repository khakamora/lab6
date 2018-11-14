'''
Created on 14 лист. 2018 р.

@author: default-user
'''
from tkinter import *
root = Tk()
 
def changeFont(font):
    l['font'] = font
 
l = Label(text="Hello World")
l.pack()
Button(command=lambda f="Verdana": changeFont(f)).pack()
Button(command=lambda f="Times": changeFont(f)).pack()
 
root.mainloop()