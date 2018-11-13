'''
Created on 10 лист. 2018 р.

@author: F
'''
import tkinter
import csv
from tkinter import ttk
from distutils import command
from tkinter import messagebox


root = tkinter.Tk()
#top = tkinter.Tk()

# open file
with open('students.csv', newline = '', encoding='utf-8') as file:
    reader = csv.reader(file)
    
    r = 0
    for col in reader:
      c = 0
      for row in col:
         
         label = tkinter.Label(root, width = 30, height = 2, \
                               text = row, relief = tkinter.RIDGE)
         label.grid(row = r, column = c)
         c += 1
      r += 1

content = ttk.Frame(root)

def showDialog():
    messagebox.showinfo("Say Hello", "Hello World")



edit = ttk.Button(content, text="Edit", command=showDialog)
quit = ttk.Button(content, text="Quit", command=quit)

content.grid(column=c, row=r)
edit.grid(column=c+1, row=r+1)
quit.grid(column=c+2, row=r+1)


root.geometry("1200x600")   
root.mainloop()