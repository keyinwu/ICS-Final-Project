from tkinter import *
from view import *  

class MainPage(object):	
    def __init__(self, master=None):		
        self.root = master 	
        self.root.geometry('%dx%d' % (450, 600)) #window size

        self.point_to = 0 #point to itself
        
        self.createPage() 	
    
    def createPage(self):	
        self.page = Frame(self.root) #create frame	
        self.page.pack()
  
        self.whoPage = WhoFrame(self.root, self.page) # create different Frame
        self.timePage = TimeFrame(self.root, self.page)		
        self.sonnetPage = SonnetFrame(self.root, self.page)		
        self.searchPage = SearchFrame(self.root, self.page)		

        '''
        menubar = Menu(self.root)		
        menubar.add_command(label='1', command = self.inputData)		
        menubar.add_command(label='2', command = self.queryData)		
        menubar.add_command(label='3', command = self.countData)		
        menubar.add_command(label='4', command = self.aboutDisp)		
        self.root['menu'] = menubar  # menu
        '''
        Label(self.page).grid(row=0, stick=W)	
        Button(self.page, text='who?', command=self.whoDisp).grid(row=1,  pady=10)		
        Button(self.page, text='time', command=self.timeDisp).grid(row=2) 
        Button(self.page, text='sonnet', command=self.sonnetDisp).grid(row=3,  pady=10)		
        Button(self.page, text='search', command=self.searchDisp).grid(row=4) 

        
    def whoDisp(self):	
        self.page.pack_forget()	
        self.whoPage.pack()
        self.point_to = 1
        self.whoPage.point_to = 0
        #print(self.point_to)		


	
        
    def timeDisp(self):		
        self.page.pack_forget()		
        self.timePage.pack()
        self.point_to = 2	
        self.timePage.point_to = 0
	
        
    def sonnetDisp(self):		
        self.page.pack_forget()		
        self.sonnetPage.pack()
        self.point_to = 3
        self.sonnetPage.point_to = 0

        
    def searchDisp(self):		
        self.page.pack_forget()			
        self.searchPage.pack()
        self.point_to = 4
        self.searchPage.point_to = 0
        
    def forget_to_chat(self):
        self.page.pack_forget()	
        self.whoPage.pack_forget()
        self.timePage.pack_forget()
        self.sonnetPage.pack_forget()
        self.searchPage.pack_forget()
        self.point_to = 1
        self.whoPage.point_to = 2
        
