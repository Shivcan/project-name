import tkinter
from tkinter import *
from tkinter import messagebox
top = tkinter.Tk()

import pandas as pd

df = pd.read_excel (r'C:\Users\admin1\Desktop\final_project\DATA_COLLECTION(PAST).xlsx')

data = pd.DataFrame(df, columns= ['NAME OF THE BRIDGE'])#printing the only requirement
place=pd.DataFrame(df, columns= ['PLACE'])
CON=pd.DataFrame(df, columns= ['CONTRACTOR'])
DAT=pd.DataFrame(df, columns= ['CONSTRUCTION DATE'])
DENSITY=pd.DataFrame(df, columns= ['VEHICHLE DENSITY(PR/HR)'])
LAST=pd.DataFrame(df, columns= ['LAST RENOVATED'])
COMM=pd.DataFrame(df, columns= ['COMMENTS ON LAST RENOVATION'])
BUD=pd.DataFrame(df, columns= ['BUDGET OF LAST RENOVATION'])
def NAMES():
    
    print(data)
def PLACE():
    print(place)

def CONTRACTOR():
    print(CON)
def DATE():
    print(DAT)
def DENSITY():
    print(DENSITY)
def LAST_RENOVATED():
    print(LAST)
def COMMENTS():
    print(COMM)
def BUDGET():
    print(BUD)







    

B = tkinter.Button(top, text ="NAME OF THE BRIDGE", command = NAMES,cursor="circle")
B1 = tkinter.Button(top, text ="PLACE", command = PLACE,cursor="plus")

B2 = tkinter.Button(top, text ="CONTRACTOR", command = CONTRACTOR,cursor="circle")
B3 = tkinter.Button(top, text ="DATE", command =DATE,cursor="plus")

B4= tkinter.Button(top, text ="DENSITY", command = DENSITY,cursor="circle")
B5 = tkinter.Button(top, text ="LAST_RENOVATED", command = LAST_RENOVATED,cursor="plus")
B6 = tkinter.Button(top, text ="COMMENTS", command = COMMENTS,cursor="circle")
B7 = tkinter.Button(top, text ="BUDGET", command = BUDGET,cursor="plus")



B.grid(row=1, column=0) 
B1.grid(row=3, column=0) 
B2.grid(row=5, column=0) 
B3.grid(row=7, column=0) 
B4.grid(row=9, column=0) 
B5.grid(row=11, column=0) 
B6.grid(row=13, column=0) 
B7.grid(row=15, column=0)

# Code to add widgets will go here...
top.mainloop()
