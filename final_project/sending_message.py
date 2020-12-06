from twilio.rest import Client 
import tkinter
from tkinter import *
from tkinter import messagebox
top = tkinter.Tk()
from PIL import Image  
  
# creating a object  
im = Image.open(r"road.png")  
  

account_sid = 'ACae7eccc2f100c7af953a981d373b96f4'
auth_token = 'd59f457e2ca0b10c72e9aa7abf5db198'
  
client = Client(account_sid, auth_token) 
  
''' Change the value of 'from' with the number  
received from Twilio and the value of 'to' 
with the number in which you want to send message.'''
def send():
    message = client.messages.create( 
                              from_='+12676139852', 
                              body ='Heavy Rain Alert ', 
                              to ='+917400302816'
                          )
def view():
    im.show()
    
 
    
B = tkinter.Button(top, text ="SEND MESSAGE", command = send,cursor="circle")
B.grid(row=1, column=0)

B1= tkinter.Button(top, text ="VIEW IMAGE", command = view,cursor="circle")
B1.grid(row=2, column=0)

#B = tkinter.Button(top, text ="SEND MESSAGE", command = send,cursor="circle")
#B.grid(row=1, column=0)

  
 
