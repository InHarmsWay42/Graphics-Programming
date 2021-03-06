#Author: Andrew Harmathy and Leugim Lim
#Last Modified by: Andrew Harmathy
#Date: July 30, 2013
#Description: A game where the player plays as the enterprise as it dodges borg ships.
#The player also has to gather intel blocks for points.
#Version 0.1: Enterprise ship is displayed and controllable
#Version 0.2: Power modules move across screen
#Version 0.3: Space background scrolls from right to left
#Version 0.4: Borg cube added. Scrolls right from random positions from the y-axis.
#Version 0.5: More borg cubes added. Background fixed to prevent skipping
#Version 0.6: Collision detection added. Pick-ups and borg ships disappear when touched by ship sprite
#Version 0.7: Intel sprites added. Power sprites will (in a future version) give health. Intel gives points.
#Version 0.8: Sounds added. Background music added.
#Version 0.9: Scoreboard added. Lives are tracked.

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
        
        #sounds added to resources
        if not pygame.mixer:
            print("problem with sound")
        else:
            pygame.mixer.init()
            self.sndComputer = pygame.mixer.Sound("computer.ogg")
            self.sndTorpedo = pygame.mixer.Sound("torpedo.ogg")
            #background music
            self.sndSuspense = pygame.mixer.Sound("suspense.ogg")
            self.sndSuspense.play(-1)
    
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
        
#creates intel pick-up sprites, sprite allows player to earn points        
class Intel(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("iicon.gif")
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
        
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right < 0:
            self.reset()
            
    def reset(self):
        self.rect.left = screen.get_width()
        self.dx = random.randrange(-10, -2)
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

#keeps track of score and lives the player has
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
        
    def update(self):
        self.text = "Shield Level: %d. Score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()


def main():
    #creates screen dimension
    screen = pygame.display.set_mode((640, 480))
    #caption at top
    pygame.display.set_caption("Star Trek! version 0.9 - scoreboard!")

    #gives default background
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #calls sprite classes
    ship = Ship()
    power = Power()
    intel1 = Intel()
    intel2 = Intel()
    intel3 = Intel()
    borg1 = Borg()
    borg2 = Borg()
    borg3 = Borg()
    space = Space()
    scoreboard = Scoreboard()
    
    allSprites = pygame.sprite.Group(power, intel1, intel2, intel3, borg1, borg2, borg3, ship, space)
    scoreSprite = pygame.sprite.Group(scoreboard)
    
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
            ship.sndComputer.play()
            scoreboard.lives += 1
            power.reset()
        if ship.rect.colliderect(borg1.rect):
            ship.sndTorpedo.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                print("Game over!")
                scoreboard.lives = 5
                scoreboard.score = 0
            borg1.reset()
        if ship.rect.colliderect(borg2.rect):
            ship.sndTorpedo.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                print("Game over!")
                scoreboard.lives = 5
                scoreboard.score = 0
            borg2.reset()
        if ship.rect.colliderect(borg3.rect):
            ship.sndTorpedo.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                print("Game over!")
                scoreboard.lives = 5
                scoreboard.score = 0
            borg3.reset()
        if ship.rect.colliderect(intel1.rect):
            ship.sndComputer.play()
            scoreboard.score += 100
            intel1.reset()
        if ship.rect.colliderect(intel2.rect):
            ship.sndComputer.play()
            scoreboard.score += 100
            intel2.reset()
        if ship.rect.colliderect(intel3.rect):
            ship.sndComputer.play()
            scoreboard.score += 100
            intel3.reset()
        
        allSprites.clear(screen, background)
        allSprites.update()
        scoreSprite.update()
        
        scoreSprite.draw(screen)
        allSprites.draw(screen)
        
        pygame.display.flip()
    
    #return mouse cursor
    pygame.mouse.set_visible(True) 
    ship.sndSuspense.stop() 

if __name__ == "__main__":
    main()
