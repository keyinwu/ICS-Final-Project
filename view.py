from tkinter import *
from tkinter import ttk
from tkinter.messagebox import * 

class WhoFrame(Frame): # inherit Frame class
    def __init__(self, master=None,mainpage = None):		
        Frame.__init__(self, master)		
        self.root = master 		
        self.itemName = StringVar()		
        self.importPrice = StringVar()		
        self.sellPrice = StringVar()		
        self.deductPrice = StringVar()	
        self.page = mainpage
        
        self.namelst = ["hi","yo","uouo","fygu"]
        self.target = ''
        
        self.createPage()
        
        
        
    def createPage(self):		
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1,  pady=10)
        
        self.names = StringVar()
        self.namesChosen = ttk.Combobox(self, width = 20, textvariable = self.names, state='readonly')
        self.namesChosen.grid(row=2, pady = 20)
        self.namesChosen['values'] = tuple(self.namelst)
        self.namesChosen.current(0)
        
        Button(self, text='chat with him/her', command=self.get_target).grid(row=3,  pady=10)
        
        self.chatPage = ChatFrame(self.root, self)
        
        '''
        Label(self, text = '药品名称: ').grid(row=1, stick=W, pady=10)		
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)		
        '''
        
    def get_namelst(self,namelst):
        self.namelst = namelst
        
    def get_target(self):
        self.target = self.namesChosen.get()
        print(self.target)
        	
        self.pack_forget()
        self.chatPage.pack()
        
    
    def back(self):
        self.page.pack()	
        self.pack_forget()		
         
        
class TimeFrame(Frame): 
    def __init__(self, master=None,mainpage = None):		
        Frame.__init__(self, master)		
        self.root = master 
        self.itemName = StringVar()	
        self.page = mainpage
        self.createPage() 
              
    def createPage(self):		
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1,  pady=10)
        
    def back(self):
        self.page.pack()	
        self.pack_forget()	
        
class SonnetFrame(Frame): 
    def __init__(self, master=None,mainpage = None):		
        Frame.__init__(self, master)		
        self.root = master 
        self.page = mainpage
        self.createPage() 	
        
    def createPage(self):		  
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1,  pady=10)
        
    def back(self):
        self.page.pack()	
        self.pack_forget()	
        
class SearchFrame(Frame):
    def __init__(self, master=None,mainpage = None):		
        Frame.__init__(self, master)		
        self.root = master 
        self.page = mainpage
        self.createPage() 	
   
    def createPage(self):		
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1,  pady=10)
        
    def back(self):
        self.page.pack()	
        self.pack_forget()	
        
class ChatFrame(Frame):
    def __init__(self, master = None, mainpage = None):
        Frame.__init__(self, master)
        self.root = master 
        self.page = mainpage
        self.createPage()
        
    def createPage(self):
        #Label(self, text='chat').pack()
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1, stick=E)
        self.msglst = Text(self,width=55)
        self.msglst.grid(row=2)
        self.txtlst = Text(self,width=55)
        self.txtlst.grid(row=3,pady = 20)
        
    def back(self):
        self.page.pack()	
        self.pack_forget()
        
        
        
        
        
        
        
        
        
        
        
        
        
