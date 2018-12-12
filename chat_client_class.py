import time
import socket
import select
import sys
import json
from chat_utils import *
import client_state_machine as csm

import threading

from tkinter import *
import LoginPage as lp

class Client:
    def __init__(self, args):
        self.peer = ''
        self.console_input = []
        self.console_last = ""
        self.state = S_OFFLINE
        self.system_msg = ''
        self.local_msg = ''
        self.peer_msg = ''
        self.args = args
        
        self.root = Tk()
        self.root.title('Welcome to ICS chat')

        

    def quit(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()

    def get_name(self):
        return self.name

    def init_chat(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
        svr = SERVER if self.args.d == None else (self.args.d, CHAT_PORT)
        self.socket.connect(svr)
        self.sm = csm.ClientSM(self.socket)
        reading_thread = threading.Thread(target=self.read_input)
        reading_thread.daemon = True
        reading_thread.start()

    def shutdown_chat(self):
        return

    def send(self, msg):
        mysend(self.socket, msg)

    def recv(self):
        return myrecv(self.socket)

    def get_msgs(self):
        read, write, error = select.select([self.socket], [], [], 0)
        my_msg = ''
        peer_msg = []
        #peer_code = M_UNDEF    for json data, peer_code is redundant
        if len(self.console_input) > 0:
            my_msg = self.console_input.pop(0)
        if self.socket in read:
            peer_msg = self.recv()
        return my_msg, peer_msg

    def output(self):
        if self.sm.get_state() == S_LOGGEDIN:
            if len(self.system_msg) > 0:
                if self.MPage.point_to == 1:
                    if self.MPage.whoPage.point_to == 0 or self.MPage.whoPage.chatPage.point_to == 1:     #whopage
                        #print("whopage")
                        self.MPage.whoPage.list_all.delete(0.0, END)# clear previous info
                        self.MPage.whoPage.add_names(self.system_msg) #insert text
                        self.system_msg = self.system_msg.split("\n")[2].strip("{").strip("}")
                        names = self.system_msg.split(", ")
                        namelst = [names[i][1:-4] for i in range(len(names))]
                        self.MPage.whoPage.set_namelst(namelst)
                        self.system_msg = ''
                    if self.MPage.whoPage.chatPage.point_to == 0:
                        self.MPage.whoPage.chatPage.msglst.insert(END,self.system_msg) #insert text
                        self.system_msg = ''
                if self.MPage.point_to == 2:
                    if self.MPage.timePage.point_to == 0:
                        self.MPage.timePage.timeUpdate(self.system_msg)
                        self.system_msg = ''
                        '''
                if self.MPage.point_to == 3:
                    if self.MPage.sonnetPage.point_to == 2:
                        try:
                            self.MPage.sonnetPage.list_s.delete(0.0, END)# clear previous info
                            self.MPage.sonnetPage.add_sonnet(self.system_msg) #insert text
                            #print(self.system_msg)
                            #self.MPage.sonnetPage.sLabel.config(text = self.system_msg)
                            #self.MPage.sonnetPage.sUpdate(self.system_msg)
                            self.system_msg = ''
                        except:
                            pass
                            '''
                
            try:
                self.root.update()
            except:
                pass
            
        elif self.sm.get_state() == S_CHATTING:
            if len(self.system_msg) > 0:
                #print(self.system_msg)
                self.MPage.whoPage.chatPage.msglst.insert(END,self.system_msg + "\n") #insert text
                self.system_msg = ''
            try:
                self.root.update()
            except:
                pass


    def login(self):
        my_msg, peer_msg = self.get_msgs()
        if len(my_msg) > 0:
            self.name = my_msg
            msg = json.dumps({"action":"login", "name":self.name})
            self.send(msg)
            response = json.loads(self.recv())
            if response["status"] == 'ok':
                self.state = S_LOGGEDIN
                self.sm.set_state(S_LOGGEDIN)
                self.sm.set_myname(self.name)
                #self.print_instructions()  temporarily comment
                return (True)
            elif response["status"] == 'duplicate':
                #self.system_msg += 'Duplicate username, try again'
                self.LPage.showinfo()
                return False
        else:               # fix: dup is only one of the reasons
           return(False)


    def read_input(self):
        #while True:
            #text = sys.stdin.readline()[:-1]
            #self.console_input.append(text) # no need for lock, append is thread safe
            

        while True:
            if self.sm.get_state() == S_OFFLINE:
                try:
                    if self.LPage.name != '' and self.console_last != 'name':
                        self.name = self.LPage.name
                        self.console_input.append(self.name)
                        self.console_last = 'name'
                except:
                    self.console_input = []
            elif self.sm.get_state() == S_LOGGEDIN:
                try:
                    if self.MPage.point_to == 1:
                        if self.MPage.whoPage.point_to == 0 or (self.MPage.whoPage.point_to == 2 and self.MPage.whoPage.chatPage.point_to == 1):#whopage
                            if self.console_last != 'who':
                                self.console_input.append('who')
                                self.console_last = 'who'
                                #print("whopage")
                        if (self.MPage.whoPage.point_to == 2 and self.MPage.whoPage.chatPage.point_to == 0):#to chatpage
                            if self.console_last != 'c':
                                self.console_input.append('c '+ self.MPage.whoPage.target)                                
                                self.console_last = 'c'
                            else:
                                try:
                    
                                    text = self.MPage.whoPage.chatPage.getText().strip("\n")
                                    #self.MPage.whoPage.chatPage.deletetxtlst()
                                    if text != "":
                                        self.console_input.append(text)
                                        #self.MPage.whoPage.chatPage.msglst.insert(END,text + "\n")  #Not here
                        
                                        self.MPage.whoPage.chatPage.deleteText()
                            
                        
                                except:
                                    self.console_input = []
                                    
                        if self.MPage.whoPage.point_to == 1:  #mainpage
                            self.console_last = "main"
                    '''
                    now cant go back to whopage when requested chatting
                    divide main to who and chat to who
                    '''
                        
                    if self.MPage.point_to == 2:
                        if self.MPage.timePage.point_to == 0:
                            if self.console_last != 'time':
                                self.console_input.append('time')
                                self.console_last = 'time'
                        if self.MPage.timePage.point_to == 1:          # changed
                            self.console_last = "main"
                            '''
                    if self.MPage.point_to == 3:
                        if self.MPage.sonnetPage.point_to == 2:
                            #print("there")
                            self.MPage.sonnetPage.getNum()
                            sonnetNumber = self.MPage.sonnetPage.numStr
                            #print(self.sonnetNumber)
                            #print("here")
                            print(sonnetNumber)
                            if self.console_last != 'p ' + sonnetNumber: 
                           
                                #print(sonnetNumber)
                                self.console_input.append('p ' + sonnetNumber)
                                self.console_last = 'p ' + sonnetNumber
                        if self.MPage.sonnetPage.point_to == 1:
                            self.console_last = "main"
                            
                    if self.MPage.point_to == 4: 
                        if self.MPage.searchPage.point_to == 0:
                            if self.console_last != '?':
                                self.console_input.append('?')
                                self.console_last = '?'  
                        if self.MPage.searchPage.point_to == 1:
                            self.console_last = "main"
                            '''
                except:
                    self.console_input = []
            elif self.sm.get_state() == S_CHATTING:
                #self.MPage.whoPage.chatPage.pack()
                #self.root.update()
                #self.text_last = ""   #avoid endless loop
                #if self.MPage.whoPage.chatPage.point_to == 1:
                    #self.MPage.whoPage.chatPage.goBack()
                    #self.console_input.append('bye')
                    #self.MPage.whoPage.chatPage.setBack(1)
                #else:
                try:
                    
                    text = self.MPage.whoPage.chatPage.getText().strip("\n")
                    #self.MPage.whoPage.chatPage.deletetxtlst()
                    if text != "":
                        self.console_input.append(text)
                        #self.MPage.whoPage.chatPage.msglst.insert(END,text + "\n")  #Not here
                        
                        self.MPage.whoPage.chatPage.deleteText()
                                               
                        
                except:
                    self.console_input = []

            
                   
                    
    def print_instructions(self):
        self.system_msg += menu

    def run_chat(self):
        self.init_chat() 
        self.LPage = lp.LoginPage(self.root)
        while self.login() != True:
            self.root.update()  
        self.LPage.page.destroy()			
        self.MPage = lp.MainPage(self.root)
        #self.system_msg += 'Welcome, ' + self.get_name() + '!'  comment temporarily
        self.output()
        while self.sm.get_state() != S_OFFLINE:
            self.proc()
            if self.sm.get_state() == S_CHATTING:
                self.MPage.whoPage.req_target()
                self.MPage.forget_to_chat()
                self.console_last = 'c'
  
            self.output()
            time.sleep(CHAT_WAIT)
        self.quit()
            
        
            
           
        
        
        '''
        self.system_msg += 'Welcome to ICS chat\n'
        self.system_msg += 'Please enter your name: '
        self.output()
        
        while self.login() != True:
            self.output()
            
        
        self.system_msg += 'Welcome, ' + self.get_name() + '!'
        self.output()
        while self.sm.get_state() != S_OFFLINE:
            self.proc()
            self.output()
            time.sleep(CHAT_WAIT)
        self.quit()
        '''

#==============================================================================
# main processing loop
#==============================================================================
    def proc(self):
        my_msg, peer_msg = self.get_msgs()
        #print(my_msg) 
        self.system_msg += self.sm.proc(my_msg, peer_msg)
