import pygame
import os, sys
from pygame.locals import *

if not pygame.font: print ('Warning, fonts disabled')
if not pygame.mixer: print ('Warning, sound disabled')
print (os.getcwd())

class Cube(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image= pygame.image.load('resources/sprites/cube/red.png')
        self.rect = self.image.get_rect()
        self.x,self.y = 150, 200
        self.v = 0
        self.rect.topleft= (self.x, self.y)
        self.gravitydown = True
    def update(self):
        
        if self.gravitydown == True:
            self.v+=.4
            self.y+=self.v
        elif self.gravitydown == False:
            self.v-=.4
            self.y+=self.v
        self.rect.topleft = self.x,self.y
            
        print('update')
    def switchg(self):
        print('test')
        """gitTest"""

class mainG:
    def __init__(self,width =630,height=480):
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
        self.cube=Cube()
        self.allsprites = pygame.sprite.RenderPlain((self.cube))

def main():
    maingame = mainG()
    maingame.MainLoop()
    

if __name__ == '__main__':
    main()
