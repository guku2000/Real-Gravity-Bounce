import pygame
import os, sys
from pygame.locals import *
from pygame import draw
#Made by Julian -_-
#This is a 32bit game resulting in a window that is 32x16 wide
if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')
print (os.getcwd())
class Cube(pygame.sprite.Sprite):
    def __init__(self,width,height):
        self.width = width
        self.height = height
        pygame.sprite.Sprite.__init__(self)
        self.color = "red"
        self.image= pygame.image.load('resources/sprites/cube/red.png')
        self.rect = self.image.get_rect()
        self.x,self.y = self.width//4, self.height//2
        self.v = 0
        self.rect.topleft= (self.x, self.y)
        self.gravitydown = True
        0
    def update(self):
        if self.gravitydown == True:
            if self.rect.bottom< self.height:
                self.v+=.4
                self.y+=self.v

        elif self.gravitydown == False:
            if self.rect.top>0:
                self.v-=.4
                self.y+=self.v
        self.rect.topleft = self.x,self.y
    def switchgrav(self):
        print("g switch")
        self.v = 0
        if self.gravitydown == True:
            self.gravitydown = False
        elif self.gravitydown == False:
            self.gravitydown = True

    def switchcol(self):
        print("c switch")
        if self.color == 'red':
            self.color = 'green'
            self.image= pygame.image.load('resources/sprites/cube/green.png')
        elif self.color == 'green':
            self.color = 'blue'
            self.image= pygame.image.load('resources/sprites/cube/blue.png')
        elif self.color == 'blue':
            self.color = 'red'
            self.image= pygame.image.load('resources/sprites/cube/red.png')
        
class rectsprite(pygame.sprite.Sprite):
    def __init__(self,color,x,y,length):
        self.x,self.y = x,y
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((length*32,32))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x,self.y)
    def update(self):
        print("help")
class mainG:
    def __init__(self,width =1024,height=512):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Real Gravity Bounce')
        
    def MainLoop(self):
        self.LoadGame()
        while 1:
            self.screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:
                        self.cube.switchgrav()
                    if event.key == pygame.K_g:
                        self.cube.switchcol()
            self.allsprites.update()
            self.level_s.draw(self.screen)
            self.allsprites.draw(self.screen)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            pygame.display.flip()
            self.clock.tick(60)
    def LoadGame(self):
        #load everything we need
        self.cube=Cube(self.width,self.height)
        self.allsprites = pygame.sprite.Group((self.cube))
        self.level_s = pygame.sprite.Group()
        self.GetLayout()
        self.drawMap()

    def GetLayout(self,lvln = 1):
        self.lvln=lvln
        print("getting layout")
        self.layout= open('resources/maps/' + str(self.lvln) + '/layout.rgb','r')
        self.mapar = []
        linen = 0
        for line in self.layout:
            self.mapar.append([])
            for unit in line:
                if unit != '\n':
                    self.mapar[linen].append(int(unit))
            linen+=1

    def drawMap(self,lvln = 1):
        length=0
        rownum = 0
        lastcolumn = False
        for row in self.mapar:
            column=0
            for num in self.mapar[rownum]:
                try:
                    self.mapar[rownum][(column+1)]
                except:
                    lastcolumn=True
                if length>=16:
                    lastcolumn = True
                if lastcolumn == False:
                    if self.mapar[rownum][column]==self.mapar[rownum][(column+1)]:
                        length+=1
                        
                    else:
                        self.drawrect(rownum,column,length,num)
                        length = 0
                else:
                    self.drawrect(rownum,column,length,num)
                    length=0
                    lastcolumn = False
                column+=1
            rownum+=1
                    
    def drawrect(self,row,column,length,colorcode):
        x=(column-length)*32
        y=row*32
        length+=1
        if colorcode == 0:
            pass
        if colorcode == 1:
            print("black")
            brect=rectsprite((0,0,0),x,y,length)
            self.level_s.add(brect)

def main():
    maingame = mainG()
    maingame.MainLoop()
    
    

if __name__ == '__main__':
    main()
