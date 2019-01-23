'''
Created on 23 січ. 2019 р.

@author: F
'''

#  -*-coding:utf8 -*-

from tkinter import *
import re
from tkinter import messagebox

def task22():

    my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"

    spl_list = re.split('_',my_string)

    str1 = spl_list[0]
    header1 = str1.replace(";","", 2)

    str2 = spl_list[1]
    row1 = str2.replace(";"," ")

    str3 = spl_list[2]
    row2 = str3.replace(";"," ")

    messagebox.showinfo("Диаложек",'{:<24}{:<14}{}'.format(row1[0:20], row1[21:28], row1[29:44]))
def task4():
    my_list = ['list1', 'list2', 'list3', 'list4', 'list5', 'list6', 'list7', 'list8', 'list9', 'list10']

    del my_list[3:7]

    my_list.append('list11')
    my_list.append('list12')

    messagebox.showinfo("Диаложек", my_list)
   
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label="Task 2_2", command = task22)
filemenu.add_command(label = "Task 4", command = task4)

filemenu.add_separator()

filemenu.add_command(label = "Exit", command = root.quit)
menubar.add_cascade(label = "File", menu = filemenu)

root.config(menu = menubar)
root.mainloop()