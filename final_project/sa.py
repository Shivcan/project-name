from tkinter import *
from PIL import ImageTk, Image
import os

root = Tk()
img = ImageTk.PhotoImage(Image.open("road.png"))
panel = Label(root, image = img)
panel.grid(row=10, column=0) 
root.mainloop()
