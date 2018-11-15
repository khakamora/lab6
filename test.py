'''
Created on 14 лист. 2018 р.

@author: default-user
'''
#from tkinter import *
#root = Tk()
 
#def changeFont(font):
 #   l['font'] = font
 
#l = Label(text="Hello World")
#l.pack()
#Button(command=lambda f="Verdana": changeFont(f)).pack()
#Button(command=lambda f="Times": changeFont(f)).pack()
 
#root.mainloop()

from tkinter import *
root = Tk()
frame = Frame(root)
frame.pack()

def prep(event):
    event.widget.config(bg='light blue')
    event.widget.focus_set()  # give keyboard focus to the label
    event.widget.bind('<Key>', edit)

def edit(event):
    print(event.char)

example = Label(frame, text='Click me')
example.pack()
example.bind('<Button-1>', prep)
mainloop()