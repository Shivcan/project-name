from twilio.rest import Client 
import tkinter
from tkinter import *
from tkinter import messagebox
import pandas as pd
from PIL import ImageTk, Image
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


top = tkinter.Tk()
img = ImageTk.PhotoImage(Image.open("road.png"))
panel = Label(top, image = img,width=1000,height=300)
panel.grid(row=20, column=0) 


from tkinter.ttk import *
from PIL import Image  
def DATAVIEW():
    view=tkinter.Tk()
    
    
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
    B = tkinter.Button(view, text ="NAME OF THE BRIDGE", command = NAMES,cursor="circle",fg="white",
    bg="blue",
    width=30,
    height=5)
    B1 = tkinter.Button(view, text ="PLACE", command = PLACE,cursor="plus",fg="white",
    bg="black",
    width=30,
    height=5)

    B2 = tkinter.Button(view, text ="CONTRACTOR", command = CONTRACTOR,cursor="circle",fg="white",
    bg="blue",
    width=30,
    height=5)
    B3 = tkinter.Button(view, text ="DATE", command =DATE,cursor="plus",fg="white",
    bg="green",
    width=30,
    height=5)

    B4= tkinter.Button(view, text ="DENSITY", command = DENSITY,cursor="circle",fg="white",
    bg="red",
    width=30,
    height=5)
    B5 = tkinter.Button(view, text ="LAST_RENOVATED", command = LAST_RENOVATED,cursor="plus",fg="white",
    bg="yellow",
    width=30,
    height=5)
    B6 = tkinter.Button(view, text ="COMMENTS", command = COMMENTS,cursor="circle",fg="white",
    bg="black",
    width=30,
    height=5)
    B7 = tkinter.Button(view, text ="BUDGET", command = BUDGET,cursor="plus",fg="white",
    bg="blue",
    width=30,
    height=5)



    B.grid(row=1, column=0) 
    B1.grid(row=3, column=0) 
    B2.grid(row=5, column=0) 
    B3.grid(row=7, column=0) 
    B4.grid(row=9, column=0) 
    B5.grid(row=11, column=0) 
    B6.grid(row=13, column=0) 
    B7.grid(row=15, column=0)


    
    top.destroy()
def cap_image():
    col=tkinter.Tk()
    def a():
        img = cv2.imread('pot.jpg',0)
        kernel = np.ones((5,5), np.uint8)
        img_erosion = cv2.erode(img, kernel, iterations=1) 
        img_dilation = cv2.dilate(img, kernel, iterations=1) 
  

        edges = cv2.Canny(img,100,200)
        cv2.imshow('Erosion', img_erosion) 
        cv2.imshow('Dilation', img_dilation) 
  

        plt.subplot(121),plt.imshow(img,cmap = 'gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        plt.show()
        
    def b():
        cap = cv2.VideoCapture(0)
        while(1): 

	# reads frames from a camera 
            ret, frame = cap.read() 

	# converting BGR to HSV 
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
	
	# define range of red color in HSV 
            lower_red = np.array([30,150,50]) 
            upper_red = np.array([255,255,180]) 
	
	# create a red HSV colour boundary and 
	# threshold HSV image 
            mask = cv2.inRange(hsv, lower_red, upper_red) 

	# Bitwise-AND mask and original image 
            res = cv2.bitwise_and(frame,frame, mask= mask) 

	# Display an original image 
            cv2.imshow('Original',frame) 

	# finds edges in the input image image and 
	# marks them in the output map edges 
            edges = cv2.Canny(frame,100,200)
            cv2.imshow('Edges',edges) 
  
    # Wait for Esc key to stop 
            k = cv2.waitKey(5) & 0xFF
            if k == 27: 
                break
        cap.release() 
  
# De-allocate any associated memory usage 
    cv2.destroyAllWindows() 

        
    B = tkinter.Button(col, text ="look for an existing image", command = a,cursor="circle",fg="white",
    bg="black",
    width=100,
    height=10)
    B1 = tkinter.Button(col, text ="live image ", command = b,cursor="plus",fg="white",
    bg="blue",
    width=100,
    height=10)
    B.grid(row=1, column=0) 
    B1.grid(row=3, column=0)



   

    
    top.destroy()
def alert():
    
    alert=tkinter.Tk()
    im = Image.open(r"road2.png")  
  

    account_sid = 'ACda1eb7bf965963295543fa25c1603400'
    auth_token = '127ebfe0655ee07e1f2b78d0cf26b826'
  
    client = Client(account_sid, auth_token) 
  
    ''' Change the value of 'from' with the number  
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
    def HEAVY():

        message = client.messages.create( 
                              from_='+17344717014',
                              body ='Heavy Rain Alert ', 
                              to ='+919769335037'
                          )
    def traffic():
        message = client.messages.create( 
                              from_='+17344717014', 
                              body ='Heavy traffic Alert ', 
                              to ='+919769335037'
                          )
    def potholes():
        
        message = client.messages.create( 
                              from_='+17344717014', 
                              body ='potholes observed so drive slow ', 
                              to ='+919769335037'
                          )
    
    def view():
        im.show()
        
    RAIN = tkinter.Button(alert, text ="HEAVY RAIN ALERT", command = HEAVY,cursor="circle",fg="white",
    bg="blue",
    width=30,
    height=10)
    RAIN.grid(row=1, column=0)
    TRAFFIC= tkinter.Button(alert, text ="HEAVY traffic ALERT", command = traffic,cursor="circle",fg="white",
    bg="black",
    width=30,
    height=10)
    TRAFFIC.grid(row=2, column=0)
    POTHOLES = tkinter.Button(alert, text ="potholes alert", command = potholes,cursor="circle",fg="white",
    bg="red",
    width=30,
    height=10)
    POTHOLES.grid(row=3, column=0)

    image= tkinter.Button(alert, text ="VIEW IMAGE", command = view,cursor="circle",fg="black",
    bg="yellow",
    width=30,
    height=10)
    image.grid(row=4, column=0)
  


#B = tkinter.Button(top, text ="SEND MESSAGE", command = send,cursor="circle")
#B.grid(row=1, column=0)

    top.destroy()


B = tkinter.Button(top, text ="DATA VIEW", command = DATAVIEW,cursor="circle",fg="white",
    bg="black",
    width=30,
    height=10)
B1 = tkinter.Button(top, text ="IMAGE COLLECTION ", command = cap_image,cursor="plus",fg="white",
    bg="black",
    width=30,
    height=10)

B2 = tkinter.Button(top, text ="ALERT", command =alert,cursor="circle",fg="white",
    bg="black",
    width=30,
    height=10)
B.grid(row=1, column=0) 
B1.grid(row=3, column=0) 
B2.grid(row=5, column=0) 
