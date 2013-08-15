#Author: Andrew Harmathy and Leugim Lim
#Last modified by: Andrew Harmathy
#Date: July 29, 2013
#Description: A game where the player plays as the enterprise as it dodges borg ships.
#The player also has to gather intel blocks for points.
#Version 0.1: Enterprise ship is displayed and controllable

import pygame
pygame.init()

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enterprise.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (mousex, mousey)
        
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption("Star Trek! version 0.1 - creating the ship sprite")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 255))
    screen.blit(background, (0, 0))
    ship = Ship()
    
    allSprites = pygame.sprite.Group(ship)
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