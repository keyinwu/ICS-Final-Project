import sys
import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
from pygame.locals import *
import random
import createImg
import createCard
import time
import pickle



class App(Sprite):
    def __init__(self):
        #self.name = name
        self._running = True
        self.width = 1200
        self.height = 750
        self.screen = pygame.display.set_mode((self.width,self.height), pygame.SRCALPHA)
        self.background = pygame.Surface(self.screen.get_size())
        self.clock = pygame.time.Clock()
        self.color = (230,200,200)
        #store cards
        self.basicImages = []
        self.images = []
        #card image source
        self.srcx = ""
        self.srcy = ""
        #count flipped card, matched cards
        self.count = 0
        self.stage = 0
        #store cards to be removed
        self.toCheck = []
        self.toCancel = []
        #chosen card number
        self.i = 0
        self.j = 0
        #time count
        self.time_start = 0
        self.time_end = 0
        self.time_use = 0
        #start counting from the moments two cards are flipped
        self.time_click = 0
        self.time_delay = 1
        #conditions for opening and ending page
        self.start = False
        self.open = False
        self.end = True
        #two cards are clicked?
        self.click = False
        #flip back the cards?
        self.next = False
        #other cards can't be clicked when two cards flipped over
        self.can_click = True
        #opening and ending message
        self.myfont = None
        self.text = None
        #level
        self.level = 0
        #level row level column
        self.row = 0
        self.column = 0
        self.distanceX = 0
        self.marginX = 0
        #records
        self.scores={}
        
    def on_setup(self):
        #update settings
        self.basicImages = []
        self.images = []
        self.src = []
        self.count = 0
        self.stage = 0
        self.toCheck = []
        self.toCancel = []
        self.i = 0
        self.j = 0
        self.time_start = 0
        self.time_end = 0
        self.time_click = 0
        self.time_delay = 0.5
        self.start = False
        self.open = False
        self.end = True
        self.click = False
        self.next = False
        self.time_use = 0
        #change level
        if self.level == 0:   
            self.color = (230,200,200)
            self.row = 3
            self.column = 5
            self.distanceX = 240
            self.marginX = 40
        elif self.level == 1:
            self.color = (200,230,200)
            self.row = 3
            self.column = 3
            self.distanceX = 280
            self.marginX = 270
        elif self.level == 2:
            self.color = (180,200,230)
            self.row = 3
            self.column = 4
            self.distanceX = 260
            self.marginX = 150
        self.background.fill(self.color)
        #load image classes
        for i in range(self.row):
            self.basicImages.append([])
            self.images.append([])
            for j in range(self.column):
                self.basicImages[i].append(createImg.basicImg(self.screen,"images/00.png",185,210,self.marginX,20))
        #a list of sources   
        for i in range((self.row*self.column)//2):
            self.srcx = str(random.randint(1,4))
            self.srcy = str(random.randint(1,13))
            self.src.append("images/"+self.srcx+self.srcy+".png")
            self.src.append("images/"+self.srcx+self.srcy+".png")
        if (self.row*self.column)%2 != 0:
            self.src.append("images/"+str(random.randint(1,4))+str(random.randint(1,13))+".png")
        #randomly choose sources
        for i in range(len(self.images)):
            for j in range(self.column):
                item = random.choice(self.src)
                self.images[i].append(createCard.Img(self.screen,item,185,210,self.marginX,20))
                self.src.remove(item)

    def on_init(self):
        pygame.init() 
        self._running = True
        self.background.fill(self.color)
        self.background = self.background.convert()
        self.screen.blit(self.background, (0,0))
        pygame.display.set_caption('Flip-Flop Match Game')
        pygame.display.flip()
        

    def opening(self):
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.font2 = pygame.font.SysFont('Comic Sans MS', 50)
        self.text1 = self.font.render('Press SPACE to start', False, (0, 0, 0))
        self.text2 = self.font2.render('Welcome to Flip-FLop Match Game!', False, (0, 0, 0))
        self.text3 = self.font.render('Press q to leave', False, (0, 0, 0))
        self.screen.blit(self.text1,(self.width/2-95,self.height/2-20))
        self.screen.blit(self.text3,(self.width/2-70,self.height/2+20))
        self.screen.blit(self.text2,(self.width/2-280,self.height/2-100))
        
    def ending(self):
        self.screen.blit(self.background, (0,0))
        if self.level > 0:
            self.text1 = self.font.render('Press SPACE to go to the next level', False, (0, 0, 0))
            self.screen.blit(self.text1,(self.width/2-140,self.height/2-20))
        else:
            self.text1 = self.font.render('Press SPACE to play again from level one', False, (0, 0, 0))
            self.screen.blit(self.text1,(self.width/2-160,self.height/2-20))
        self.text3 = self.font.render('Press q to leave', False, (0, 0, 0))
        self.text2 = self.font2.render('Total time use: '+"{:.2f}".format(self.time_use)+" seconds", False, (0, 0, 0))
        self.screen.blit(self.text3,(self.width/2-65,self.height/2+20))
        self.screen.blit(self.text2,(self.width/2-230,self.height/2-100))
        self.end = True
        
    def on_go(self):
        self.screen.blit(self.background, (0,0))
        for i in range(len(self.basicImages)):
            for j in range(len(self.basicImages[i])):
                if i>0:
                    self.basicImages[i][j].rect.y = self.basicImages[i-1][j].rect.y + 240
                if j>0:
                    self.basicImages[i][j].rect.x = self.basicImages[i][j-1].rect.x + self.distanceX
                self.basicImages[i][j].blitme()
               
        for s in range(len(self.images)):
            for t in range(len(self.images[s])):
                if s>0:
                    self.images[s][t].rect.y = self.images[s-1][t].rect.y + 240
                if t>0:
                    self.images[s][t].rect.x = self.images[s][t-1].rect.x + self.distanceX
                    
        self.start = False        
    
    def on_exit(self):
        self._running = False

    def on_cleanup(self):
        pygame.quit()
        sys.exit()
        
    def on_keydown(self,event):
        if event.key == pygame.K_q:
            self.on_exit()
        elif event.key == pygame.K_SPACE:
            if self.level < 2:
                self.level += 1
            else:
                self.level = 0
            self.on_setup()
            self.start = True
            self.end = False

    def on_click_pos(self):
        print(self.i,self.j)
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        for l in self.basicImages:   
            for v in l:
                if v.rect.collidepoint(mouseX, mouseY) == True:
                    self.i = self.basicImages.index(l)
                    self.j = l.index(v)
                    print(self.i,self.j)
                
    def add_check(self,i,j):
        if len(self.toCheck)<2:
            self.toCheck.append(self.images[i][j])
        elif len(self.toCheck)==2 and self.images[i][j] not in self.toCheck:
            self.toCheck.append(self.images[i][j])
        if len(self.toCancel)<2:
            self.toCancel.append(self.basicImages[i][j])
        elif len(self.toCancel)==2 and self.basicImages[i][j] not in self.toCancel:
            self.toCancel.append(self.basicImages[i][j])
        
    def check_same(self):
        if self.toCheck[0].src == self.toCheck[1].src:
            self.count = 0
            self.stage += 2
            self.toCancel[0].rect.x = 2000
            self.toCancel[1].rect.x = 2000
        else:
            self.count = 0
            
    def update(self):
        self.screen.blit(self.background, (0,0))
        for i in range(len(self.basicImages)):
            for j in range(len(self.basicImages[i])):
                self.basicImages[i][j].blitme()
                    
    def calc_time(self):
        if self.start == True:
            self.time_start = time.time()
        if self.end == False:
            self.time_end = time.time()  
        self.time_use = self.time_end-self.time_start
        if time.time() - self.time_click > self.time_delay and time.time() - self.time_click < self.time_delay+0.1:
            self.next = True
        if time.time()-self.time_click < self.time_delay:
            self.can_click = False
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        previ = -1
        prevj = -1
        while(self._running):
            self.calc_time()
            #draw opening page
            if self.open == False:
                self.opening()
                self.open = True
            #cover with game page
            if self.start == True:
                self.on_go()                
            #click = pygame.mouse.get_pressed()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.on_exit()
                    self.on_cleanup() 
                if event.type == pygame.KEYDOWN:
                    self.on_keydown(event)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.on_click_pos()
                    i,j = self.i,self.j
                    if (i != previ or j != prevj) and self.end == False and self.can_click == True:
                        self.images[i][j].blitme() 
                        previ = i
                        prevj = j
                        self.count += 1
                        if self.count<=2:
                            self.add_check(i,j)
                            if self.count == 2:
                                self.click = True
                                if self.click == True:
                                    self.time_click = time.time()
                                    self.click = False
                                self.check_same()
                                self.toCheck = []
                                self.toCancel = []
                                previ = -1
                                prevj = -1
                if self.next == True and self.end == False:
                    self.update()
                    self.next = False
                    self.can_click = True
            if self.stage == (self.row*self.column)//2*2 and time.time() - self.time_click > self.time_delay and time.time() - self.time_click < self.time_delay+0.1:
                #self.score()
                self.ending()
                
            pygame.display.flip()
            self.clock.tick(240)

        self.on_cleanup()
<<<<<<< HEAD
'''
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
'''
=======
    
    def score(self):
        if self.level in self.scores.keys():
            self.scores[self.level] += [self.time_use]
        else:
            self.scores[self.level] = [self.time_use]
        pickle.dump(self.scores,open("scores.idx",'wb'))
            
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
    theApp.score()
>>>>>>> 984eb869a0f086f11439650017424b9b4a358ca2
