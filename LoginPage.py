from tkinter import *
from tkinter.messagebox import *
from MainPage import *

class LoginPage(object):
    def __init__(self, master=None):		
        self.root = master 	
        self.root.geometry('%dx%d' % (300, 180)) #window size	
        self.username = StringVar()		
        self.password = StringVar()	
        
        self.x = self.root.winfo_x()
        self.y = self.root.winfo_y()
        
        self.name = ''
        self.logged = False
        
        self.createPage()
        
    def createPage(self):		
        self.page = Frame(self.root) #create frame	
        self.page.pack()		
        Label(self.page).grid(row=0)		
        Label(self.page, text = 'username: ').grid(row=1, stick=W, pady=10)		
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)		
        #Label(self.page, text = 'password: ').grid(row=2, stick=W, pady=10)		
        #Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)		
        Button(self.page, text='log in', command=self.loginCheck).grid(row=3, column=1, pady=10)		
        #Button(self.page, text='sign up', command=self.signup).grid(row=3, column=1, stick=E) 	
        
    def loginCheck(self):		
        self.name = self.username.get()	

    def showinfo(self):
        showinfo(title = 'Error', message = 'Duplicate username, try again')