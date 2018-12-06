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
  
        self.inputPage = InputFrame(self.root, self.page) # 创建不同Frame		
        self.queryPage = QueryFrame(self.root, self.page)		
        self.countPage = CountFrame(self.root, self.page)		
        self.aboutPage = AboutFrame(self.root, self.page)		
        #self.inputPage.pack() #默认显示数据录入界面	
        '''
        menubar = Menu(self.root)		
        menubar.add_command(label='数据录入', command = self.inputData)		
        menubar.add_command(label='查询', command = self.queryData)		
        menubar.add_command(label='统计', command = self.countData)		
        menubar.add_command(label='关于', command = self.aboutDisp)		
        self.root['menu'] = menubar  # 设置菜单栏 	
        '''
        Label(self.page).grid(row=0, stick=W)	
        Button(self.page, text='who?', command=self.inputData).grid(row=1,  pady=10)		
        Button(self.page, text='time', command=self.queryData).grid(row=2) 
        Button(self.page, text='sonnet', command=self.countData).grid(row=3,  pady=10)		
        Button(self.page, text='search', command=self.aboutDisp).grid(row=4) 
        
    def inputData(self):	
        self.page.pack_forget()	
        self.inputPage.pack()
        self.queryPage.pack_forget()		
        self.countPage.pack_forget()		
        self.aboutPage.pack_forget() 	
        
    def queryData(self):		
        self.page.pack_forget()	
        self.inputPage.pack_forget()		
        self.queryPage.pack()		
        self.countPage.pack_forget()		
        self.aboutPage.pack_forget() 	
        
    def countData(self):		
        self.page.pack_forget()	
        self.inputPage.pack_forget()		
        self.queryPage.pack_forget()		
        self.countPage.pack()		
        self.aboutPage.pack_forget() 	
        
    def aboutDisp(self):		
        self.page.pack_forget()	
        self.inputPage.pack_forget()		
        self.queryPage.pack_forget()		
        self.countPage.pack_forget()		
        self.aboutPage.pack()
