'''
Created on 10 лист. 2018 р.

@author: F
'''
import tkinter
import csv
from tkinter import ttk
from distutils import command
from tkinter import messagebox
from tkinter import *


root = tkinter.Tk()
#top = tkinter.Tk()

# open file
with open('students.csv', newline = '', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    r = 0
    for col in reader:
      c = 0
      for row in col:
         
         example = label = tkinter.Label(root, width = 30, height = 2, \
                               text = row, relief = tkinter.RIDGE)
         label.grid(row = r, column = c)
         c += 1
      r += 1

content = ttk.Frame(root)

def prep(event):
    event.widget.config(bg='light blue')
    event.widget.focus_set()  # give keyboard focus to the label
    event.widget.bind('<Key>', edit)

def edit(event):
    print(event.char)


def showDialog():
    #messagebox.showinfo("Say Hello", "Hello World")
    window = tkinter.Toplevel(root)
    window.geometry("300x300")
    tkinter.Label(window, text="№").grid(row=0)
    tkinter.Label(window, text="ФИО").grid(row=1)
    tkinter.Label(window, text="Возраст").grid(row=2)
    tkinter.Label(window, text="Группа").grid(row=3)
    

    e1 = tkinter.Entry(window)
    e2 = tkinter.Entry(window)
    e3 = tkinter.Entry(window)
    e4 = tkinter.Entry(window)

    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    
    #tkinter.Button(window, text='Click', command=showSelected).grid(row=4, column=0, pady=4)
    tkinter.Button(window, text='Close', command=window.quit).grid(row=4, column=0, pady=4)
    tkinter.Button(window, text='Save').grid(row=4, column=1, pady=4)

def showSelected():
    messagebox.showinfo("Say Hello", r)#example.cget("text"
    

show_info =  ttk.Button(content, text="Show", command=showSelected)
edit = ttk.Button(content, text="Edit", command=showDialog)
quit = ttk.Button(content, text="Quit", command=quit)

content.grid(column=c, row=r)
show_info.grid(column = c, row = r+1)
edit.grid(column=c+1, row=r+1)
quit.grid(column=c+2, row=r+1)


root.geometry("1200x600")   
example.grid()
example.bind('<Button-1>', prep)

root.mainloop()