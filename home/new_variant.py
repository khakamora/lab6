'''
Created on 15 лист. 2018 р.

@author: F
'''
from tkinter import *
import tkinter.ttk as ttk
import csv



root = Tk()
root.title("Python - Import CSV File To Tkinter Table")
width = 500
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)



TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("number", "lastname", "age", "groupNumber"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('number', text="№", anchor=W)
tree.heading('lastname', text="ФИО", anchor=W)
tree.heading('age', text="Возраст", anchor=W)
tree.heading('groupNumber', text="Номер группы", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=100)
tree.column('#2', stretch=NO, minwidth=0, width=200)
tree.column('#3', stretch=NO, minwidth=0, width=90)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.pack()



with open('students.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        number = row['number']
        lastname = row['lastname']
        age = row['age']
        groupNumber = row['groupNumber']
        tree.insert("", 0, values=(number, lastname, age, groupNumber))



#============================INITIALIZATION==============================
if __name__ == '__main__':

#https://www.youtube.com/watch?v=ViWXxf8CZd4
    root.mainloop()