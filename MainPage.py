from tkinter import *
from view import *  

class MainPage(object):	
    def __init__(self, master=None):		
        self.root = master 	
        self.root.geometry('%dx%d' % (450, 600)) #window size	
        self.createPage() 	
    
    def createPage(self):	
        self.page = Frame(self.root) #create frame	
        self.page.pack()
  
        self.inputPage = WhoFrame(self.root, self.page) # create different Frame
        self.queryPage = TimeFrame(self.root, self.page)		
        self.countPage = SonnetFrame(self.root, self.page)		
        self.aboutPage = SearchFrame(self.root, self.page)		

        
        '''
        menubar = Menu(self.root)		
        menubar.add_command(label='1', command = self.inputData)		
        menubar.add_command(label='2', command = self.queryData)		
        menubar.add_command(label='3', command = self.countData)		
        menubar.add_command(label='4', command = self.aboutDisp)		
        self.root['menu'] = menubar  # menu
        '''
        Label(self.page).grid(row=0, stick=W)	
        Button(self.page, text='who?', command=self.inputData).grid(row=1,  pady=10)		
        Button(self.page, text='time', command=self.queryData).grid(row=2) 
        Button(self.page, text='sonnet', command=self.countData).grid(row=3,  pady=10)		
        Button(self.page, text='search', command=self.aboutDisp).grid(row=4) 
        
    def inputData(self):	
        self.page.pack_forget()	
        self.inputPage.pack()
	
        
    def queryData(self):		
        self.page.pack_forget()		
        self.queryPage.pack()		
	
        
    def countData(self):		
        self.page.pack_forget()		
        self.countPage.pack()		
	
        
    def aboutDisp(self):		
        self.page.pack_forget()			
        self.aboutPage.pack()
