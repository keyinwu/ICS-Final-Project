from tkinter import *
from LoginPage import *

root = Tk()
root.title('chat system')
LoginPage(root)
root.mainloop()



'''
from tkinter import *
 
window = Tk()
 
window.title("Welcome to chat system")
 
window.geometry('450x600')
 
lbl = Label(window, text="Welcome to chat system :)", font='Helvetica -20 bold')
 
lbl.grid(column=0, row=0, padx = 100, pady = 100, sticky = 's')
 
txt = Entry(window,width=20)
 
txt.grid(column=0, row=1)
 
def clicked():
 
    res = "Welcome to " + txt.get()
 
    lbl.configure(text= res)
 
btn = Button(window, text="log in",font='Helvetica -15 bold', command=clicked)
 
btn.grid(column=0, row=2, pady = 40)
 
window.mainloop()
'''



'''
from PIL import ImageTk as itk
from PIL import Image as Img
from tkinter import *
#import sql.sql_connect as s
import tkinter as tk

class Login_UI():
    def __init__(self,root):
        self.root = root
        var1 = StringVar()
        
        #===========history info=========
        #result = s.log_information.last_inf(self)
        #var1.set(result[0])
        
        self.root.geometry('450x600')
        self.root.title("login")
        
        #==========background=============
        #f = Frame(width = 450, height = 600)
        #canvas = tk.Canvas(self.root, width = 450, height = 600, bg = 'yellow')
        bgimg = PhotoImage(file = "images/login.png")
        theLabel = Label(self.root, image = bgimg)
        theLabel = Label(self.root, 
                         text = "welcome to chat system",
                         image = bgimg,
                         compound = CENTER, 
                         fg = "black"
                         )
        theLabel.pack()
        #canvas.create_image(450, 600, image = bgimg)
        #canvas.grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 3)
        
        #===========login==================
        #self.usr = Entry(self.root, textvariable = var1, bg = '#F5F5F5', highlightcolor = '#1E90FF')
        #self.usr.place(rexl = 0.35, rely = 0.56)      
        
        #=========button===================
        #login_btn = Button(self.root, text = 'log in', bg = '1E90FF')
        #login_btn.place(rexl = 0.37, rely = 0.8)
        #login_btn.bind("<Button-1>", self.load)        
        
if __name__ == "__main__":
    root = Toplevel()
    ui = Login_UI(root)
    ui.root.mainloop()
    
'''