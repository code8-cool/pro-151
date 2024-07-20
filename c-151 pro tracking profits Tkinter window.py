# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 20:17:29 2024

@author: occup
"""
from tkinter import *
root = Tk()
root.geometry("1000x500")
root.title("Tracking profits")

label_month = Label(root)
label_profits = Label(root, text = "90000, 50000, 65000, 70009, 40550, 47000, 60500, 59900, 46990, 46999, 80000")
labelmax_profits = Label(root)
labelmin_profits = Label(root)

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" )
profits = (90000, 50000, 65000, 70009, 40550, 47000, 60500, 59900, 46990, 46999, 80000 )
def show_max():
    max_profits = max(profits)
    max_profits_index = profits.index(max_profits)
    max_profits_month = month[max_profits_index]
    labelmax_profits ["text"] = "The most the company earned this year is " + str(max_profits) + " in the month of  " + str(max_profits_month) 


def show_min():
    min_profits = min(profits)
    min_profits_index = profits.index(min_profits)
    min_profits_month = month[min_profits_index]
    labelmin_profits ["text"] = "The least the company earned this year is " + str(min_profits) + " in the month of  " + str(min_profits_month) 


btn_max = Button(root, text = "maximum profit", command = show_max)
btn_min = Button(root, text = "minimum profit", command = show_min)

btn_max.place(relx = 0.5, rely = 0.3, anchor = CENTER)
btn_min.place(relx = 0.5, rely = 0.5, anchor = CENTER)
labelmax_profits.place(relx = 0.5, rely = 0.4, anchor = CENTER)
labelmin_profits.place(relx = 0.5, rely = 0.6, anchor = CENTER)

root.mainloop()