#Author: Andrew Harmathy
#Date: July 10, 2013
#Description: A game where the player plays as the enterprise as it dodges borg ships.
#Version 0.1: Enterprise ship is displayed and controllable
#Version 0.2: Power modules move across screen

import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

#creates enterprise ship that is controllable
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enterprisetest.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
    
    #player's mouse controls the ships position    
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)
        
class Power(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("thunder.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dy = 5
    
    def update(self):
        self.rect.centery += self.dy
        if self.rect.top > screen.get_height():
            self.reset()
            
    def reset(self):
        self.rect.top = 0
        self.rect.centerx = random.randrange(0, screen.get_width())
        
def main():
    #creates screen dimension
    screen = pygame.display.set_mode((640, 480))
    #caption at top
    pygame.display.set_caption("Star Trek! version 0.2 - creating the ship sprite")

    #gives default background
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #calls sprite classes
    ship = Ship()
    power = Power()
    
    allSprites = pygame.sprite.Group(power, ship)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 

if __name__ == "__main__":
    main()