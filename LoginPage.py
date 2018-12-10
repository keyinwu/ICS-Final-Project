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
        
        self.createPage()
        
    def createPage(self):		
        self.page = Frame(self.root) #create frame	
        self.page.pack()		
        Label(self.page).grid(row=0, stick=W)		
        Label(self.page, text = 'username: ').grid(row=1, stick=W, pady=10)		
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)		
        Label(self.page, text = 'password: ').grid(row=2, stick=W, pady=10)		
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)		
        Button(self.page, text='log in', command=self.loginCheck).grid(row=3, stick=W, pady=10)		
        Button(self.page, text='sign up', command=self.signup).grid(row=3, column=1, stick=E) 	
        
    def loginCheck(self):		
        self.name = self.username.get()	
        
        name = self.username.get()		
        secret = self.password.get()	
        self.page.destroy()			
        MainPage(self.root)
        '''
        if name=='ww' and secret=='123456':			
            self.page.destroy()			
            MainPage(self.root)
        else:
            showinfo(title='Error', message='incorrect username or password')
        '''
            
    def signup(self):
        
        self.top = Toplevel()
        self.top.geometry("%dx%d+%d+%d" % (100, 80, self.x + 500, self.y + 300))
        self.top.title("Success")
        Label(self.top, text = "Now you can log in").pack()