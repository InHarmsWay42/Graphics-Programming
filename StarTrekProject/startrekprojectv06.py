#Author: Andrew Harmathy and Leugim Lim
#Last Modified by: Leugim Lim
#Date: July 29, 2013
#Description: A game where the player plays as the enterprise as it dodges borg ships.
#The player also has to gather intel blocks for points.
#Version 0.1: Enterprise ship is displayed and controllable
#Version 0.2: Power modules move across screen
#Version 0.3: Space background scrolls from right to left
#Version 0.4: Borg cube added. Scrolls right from random positions from the y-axis.
#Version 0.5: More borg cubes added. Background fixed to prevent skipping
#Version 0.6: Collision detection added. Pick-ups and borg ships disappear when touched by ship sprite


import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

#creates enterprise ship that is controllable
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enterprise.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
    
    #player's mouse controls the ships position    
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)
        
#creates power pick-up sprites, sprite allows player to earn health          
class Power(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("thunder.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = -5
    
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.left = screen.get_width()
        self.rect.centery = random.randrange(0, screen.get_height())
        
#creates borg ship sprites that move from left to right
class Borg(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("borg.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = -5
    
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.left = screen.get_width()
        self.rect.centery = random.randrange(0, screen.get_height())

#creates scrolling background
class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("space.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
 
        self.reset()
        self.dx = 10
        
    def update(self):
        self.rect.left -= self.dx
        if self.rect.left <= -1012:
            self.reset() 
    
    def reset(self):
        self.rect.left = 0

def main():
    #creates screen dimension
    screen = pygame.display.set_mode((640, 480))
    #caption at top
    pygame.display.set_caption("Star Trek! version 0.6 - collision detection!")

    #gives default background
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #calls sprite classes
    ship = Ship()
    power = Power()
    borg1 = Borg()
    borg2 = Borg()
    borg3 = Borg()
    space = Space()
    
    allSprites = pygame.sprite.Group(power, borg1, borg2, borg3, ship, space)
    clock = pygame.time.Clock()
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        
        #check collisions
        if ship.rect.colliderect(power.rect):
            power.reset()
        if ship.rect.colliderect(borg1.rect):
            borg1.reset()
        if ship.rect.colliderect(borg2.rect):
            borg2.reset()
        if ship.rect.colliderect(borg3.rect):
            borg3.reset()
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 

if __name__ == "__main__":
    main()
