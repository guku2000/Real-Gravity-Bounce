import pygame
import os, sys
from pygame.locals import *
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
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_h:
                    print("g switch")
                    self.v = 0
                    if self.gravitydown == True:
                        self.gravitydown = False
                    elif self.gravitydown == False:
                        self.gravitydown = True
                if event.key == pygame.K_g:
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
        
        if self.gravitydown == True:
            if self.rect.bottom< self.height:
                self.v+=.4
                self.y+=self.v

        elif self.gravitydown == False:
            if self.rect.top>0:
                self.v-=.4
                self.y+=self.v
        self.rect.topleft = self.x,self.y

class Level:
    def GetLayout(lvln = 1):
        print("getting layout")
        layout= open('resources/maps/' + lvln + '/layout.rgb')
    def GetImage():
        print("getting image")
        

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
            self.allsprites.update()
            self.allsprites.draw(self.screen)
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            pygame.display.update()
            self.clock.tick(60)
    def LoadGame(self):
        #load everything we need
        self.cube=Cube(self.width,self.height)
        self.allsprites = pygame.sprite.RenderPlain((self.cube))

def main():
    maingame = mainG()
    maingame.MainLoop()
    

if __name__ == '__main__':
    main()
