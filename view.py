from tkinter import *
from tkinter import ttk
from tkinter.messagebox import * 
import time

class WhoFrame(Frame): # inherit Frame class
    def __init__(self, master=None,mainpage = None):		
        Frame.__init__(self, master)		
        self.root = master 		
        self.itemName = StringVar()		
        self.importPrice = StringVar()		
        self.sellPrice = StringVar()		
        self.deductPrice = StringVar()	
        self.page = mainpage
        
        self.namelst = [""]
        self.target = ''
        self.point_to = 0 #point to itself 
        
        self.createPage()
        
        
        
    def createPage(self):		
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1,stick=E,  pady=10)
        
        self.names = StringVar()
        self.namesChosen = ttk.Combobox(self, width = 20, textvariable = self.names, state='readonly')
        self.namesChosen.grid(row=2, pady = 20)
        self.namesChosen['values'] = tuple(self.namelst)
        self.namesChosen.current(0)
        
        Button(self, text='chat with him/her', command=self.get_target).grid(row=3,  pady=10)
        
        self.list_all = Text(self,width=55,height=8)
        self.list_all.grid(row=4,pady=5)
        
        self.chatPage = ChatFrame(self.root, self)
        

    
    def set_namelst(self,namelst):
        self.namelst = namelst
        self.namesChosen['values'] = tuple(self.namelst)
        
    def add_names(self,msg):
        self.list_all.insert(END, msg)
        
    def get_target(self):
        self.target = self.namesChosen.get()
        #print(self.target)
        self.point_to = 2 #to chatpage
        self.chatPage.point_to = 0
        #print(self.point_to)
        	
        self.pack_forget()
        self.chatPage.pack()		

    def req_target(self): #when receive the chat request
        self.point_to = 2 #to chatpage
        self.chatPage.point_to = 0
        #self.pack_forget()
        self.chatPage.pack()		
    
    def back(self):
        self.target = ""
        self.point_to = 1 #to mainpage
        #print(self.point_to)
        self.page.pack()	
        self.pack_forget()
       	
         
        
class TimeFrame(Frame): 
    def __init__(self, master=None,mainpage = None):		
        Frame.__init__(self, master)		
        self.root = master 
        self.itemName = StringVar()	
        self.page = mainpage
        self.point_to = 0 #point to itself 
        self.createPage()
        
              
    def createPage(self):		
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1, pady=10)
        self.timeLabel = Label(self, text = "")
        self.timeLabel.grid(row=4, pady=10)
        
    def timeUpdate(self,cTime):
        self.timeLabel.config(text = cTime)
        
    def back(self):
        self.point_to = 1 #to mainpage        
        self.page.pack()	
        self.pack_forget()	
        
class SonnetFrame(Frame): 
    def __init__(self, master=None,mainpage = None):		
        Frame.__init__(self, master)		
        self.root = master 
        self.page = mainpage
        self.point_to = 0 #point to itself 
        self.ronum = StringVar()
        self.numStr = ""
        self.createPage() 	
        
        
    def createPage(self):		  
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1,column=2, stick=E,  pady=10)
        
        Label(self, text = 'Choose a number from 1 to 154 ').grid(row=2, stick=W, pady=10)		
        Entry(self, textvariable=self.ronum).grid(row=2, column=1, stick=E)	
        
        Button(self, text='OK', command = self.sUpdate).grid(row=2,column=2, pady=10)

        self.list_s = Text(self,width=55,height=10)
        self.list_s.grid(row=3,columnspan=3,pady=5)		

        #self.sLabel = Label(self, text = "")
        #self.sLabel.grid(row=4, pady=10)
        
    def getNum(self):
        #print("getnumber")
        self.numStr =  self.ronum.get()
        print("numstr:"+self.numStr)
        
    def sUpdate(self):
        self.point_to = 2 #point to sonnet
        #print("buttonclicked")
        
        
    def add_sonnet(self,msg):
        self.list_all.insert(END, msg)
        
    def back(self):
        self.point_to = 1 #to mainpage        
        self.page.pack()	
        self.pack_forget()	
        
class SearchFrame(Frame):
    def __init__(self, master=None,mainpage = None):		
        Frame.__init__(self, master)		
        self.root = master 
        self.page = mainpage
        self.subpoint_to = 0 #point to itself 
        self.createPage() 	
   
    def createPage(self):		
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1,stick=E,  pady=10)
        
    def back(self):
        self.subpoint_to = 1 #to mainpage        
        self.page.pack()	
        self.pack_forget()	
        
class ChatFrame(Frame):
    def __init__(self, master = None, mainpage = None):
        Frame.__init__(self, master)
        self.root = master 
        self.page = mainpage
        self.point_to = 0 #point to itself
        
        self.gettext = ''
        self.backcase = 1
        
        self.timeline = 0
        
        self.createPage()
        

        
    def createPage(self):
        #Label(self, text='chat').pack()
        Label(self).grid(row=0, stick=W)
        Button(self, text='back', command=self.back).grid(row=1, stick=E)
        self.msglst = Text(self,width=55)
        self.msglst.grid(row=2)
        self.txtlst = Text(self,width=55)
        self.txtlst.grid(row=3,pady = 20)
        self.txtlst.bind("<KeyPress-Return>", self.sendMsgEvent)
        
        self.scroll = Scrollbar(self, command = self.msglst.yview)
        self.scroll.grid(row=2,column=1, sticky = 'nsew')
        self.msglst['yscrollcommand'] = self.scroll.set

        

        
    def sendMsgEvent(self,event):
        if event.keycode==13:
            self.gettext, myMsg = self.txtlst.get("0.0",END), self.txtlst.get("0.0",END)
            self.txtlst.delete("0.0",END)
            self.msglst.insert(END,myMsg.strip("\n") + "\n") 
            #print("text: "+ self.gettext +"strip: " + self.gettext.strip("\n"))

                
    
    def getText(self):
        return self.gettext
    
    def deleteText(self):
        self.gettext = ""
        
    def goBack(self):
        self.msglst.insert(END,"Please say 'bye' to disconnect before you go back.\n")
        
        
    def back(self):
        #if self.backcase == 1:
        self.point_to = 1 #to whopage 
            #print(self.point_to)
        self.page.pack()	
        self.pack_forget()
        #if self.backcase == 2:
            #self.point_to = 2
            #self.setBack(1)
        
        
        
        
        
        
        
        
        
        
        
        
        
