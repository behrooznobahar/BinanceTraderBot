
from email.mime import image
from tkinter import *
import tkinter.messagebox as mesagebox
import os
from PIL import ImageTk,Image
root = Tk()
root.geometry('600x400')
root.title('Botich')
wlcomel = Label(root, text='Welcom \n I am Botich, Congratulations on your choice',bg='#AA1923', width=len('I am Botich, Congratulations on your choice')+10,pady=10)
wlcomel.place(relx=0.5,rely=0.1,anchor=CENTER)
btn_register=Button(text='Register',command='run',padx=10,bg='#AA1923',width=10)
btn_register.place(relx=0.6,rely=0.3,anchor=CENTER)
btn_log_in=Button(text='Login',command='run',padx=10,bg='#AA1923',width=10)
btn_log_in.place(relx=0.4,rely=0.3,anchor=CENTER)
image=Image.open('botich.jpg')
image.resize((20,20),Image.ANTIALIAS)
userimg=ImageTk.PhotoImage(image)
userimg=Label(root,image=userimg,width=100)
userimg.place(relx=0.5,rely=0.8,anchor=CENTER)
root.mainloop()
