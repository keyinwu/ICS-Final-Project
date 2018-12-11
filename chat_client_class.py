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
        if self.sm.get_state() != S_OFFLINE:
            if len(self.system_msg) > 0:
                if self.MPage.point_to == 1:
                    if self.MPage.whoPage.point_to == 0:     #whopage
                        #print("whopage")
                        self.MPage.whoPage.add_names(self.system_msg) #insert
                        self.system_msg = self.system_msg.split("\n")[2].strip("{").strip("}")
                        names = self.system_msg.split(", ")
                        namelst = [names[i][1:-4] for i in range(len(names))]
                        self.MPage.whoPage.set_namelst(namelst)
                        
                            
                        self.system_msg = ''
                '''
                    if self.MPage.whoPage.chatPage.point_to == 1:
                        self.MPage.whoPage.chatPage.msglst.insert(END,self.system_msg)
                        self.system_msg = ''
                        '''
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
                self.system_msg += 'Duplicate username, try again'
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
            elif self.sm.get_state() == S_LOGGEDIN or S_CHATTING:
                try:
                    if self.MPage.point_to == 1 and self.MPage.whoPage.point_to == 0 and self.console_last != 'who':
                #or \
                #(self.MPage.whoPage.point_to == 2 and\
                #self.MPage.whoPage.chatPage.point_to == 1) :
                        self.console_input.append('who')
                        self.console_last = 'who'
                        #print("getwho") once
                    if self.MPage.point_to == 2 and self.MPage.timePage.point_to == 0 and self.console_last != 'time':
                        self.console_input.append('time')
                        self.console_last = 'time'
                    if self.MPage.point_to == 3 and self.MPage.sonnetPage.point_to == 0 and self.console_last != 'p':
                        self.console_input.append('p')
                        self.console_last = 'p'
                    if self.MPage.point_to == 4 and self.MPage.searchPage.point_to == 0 and self.console_last != '?':
                        self.console_input.append('?')
                        self.console_last = '?'
                    if self.MPage.point_to == 1 and self.MPage.whoPage.point_to == 2 and self.MPage.whoPage.chatPage.point_to == 0 and self.console_last != 'c':
                        self.console_input.append('c')
                        self.console_last = 'c'
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
