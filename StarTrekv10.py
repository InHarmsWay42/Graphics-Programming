#Author: Andrew Harmathy
#Date: July 14, 2013
#Description: A game where the player plays as the enterprise as it dodges borg ships.
#Version 0.1: Enterprise ship is displayed and controllable
#Version 0.2: Power modules move across screen
#Version 0.3: Space background scrolls from right to left
#Version 0.4: Borg cube added. Scrolls right from random positions from the y-axis.
#Version 0.5: More borg cubes added. Background fixed to prevent skipping
#Version 0.6: Collision detection added. Pick-ups and borg ships disappear when touched 
#by ship sprite
#Version 0.7: Intel sprites added. Power sprites will (in a future version) give health. 
#Intel gives points.
#Version 0.8: Sounds added. Background music added.
#Version 0.9: Scoreboard added. Lives are tracked.
#Version 1.0: Start and end screen added. An unknown error appeared that created 
#trails of all the sprites. Background class Space() is remove to stop ghostly error.
#Information about error is recorded in the external document.
    
import pygame, random
pygame.init()

screen = pygame.display.set_mode((640, 480))

#creates enterprise ship that is controllable
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        #creates ship sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enterprise.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        
        #imports sound files
        if not pygame.mixer:
            print ("problem with sound")
        else:
            pygame.mixer.init()
            self.sndComputer = pygame.mixer.Sound("computer.ogg")
            self.sndLife = pygame.mixer.Sound("urlifeisover.ogg")
            self.sndTorpedo = pygame.mixer.Sound("torpedo.ogg")
            self.sndSuspense = pygame.mixer.Sound("suspense.ogg")
            self.sndSuspense.play(-1)
    
    #position of ship 
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
    
    #sprite moves right to left
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right < 0:
            self.reset()
    
    #sprite resets when it reaches the left
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
    
    #sprite moves right to left 
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right < 0:
            self.reset()
    
    #sprite resets when it reaches the left
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
    
    #sprite moves right to left 
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right < 0:
            self.reset()
            
    #sprite resets when it reaches the left       
    def reset(self):
        self.rect.left = screen.get_width()
        self.dx = random.randrange(-10, -2)
        self.rect.centery = random.randrange(0, screen.get_height())

#creates scrolling background    
class Space(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("spacetest.gif")
        self.rect = self.image.get_rect()
        self.dy = 5
        self.reset()
       
    #sprite background scrolls from right to left 
    def update(self):
        self.rect.bottom += self.dy
        if self.rect.bottom >= 1440:
            self.reset() 
    
    #sprite background resets
    def reset(self):
        self.rect.top = -960

#creates scrolling background that goes from right to left
#This class worked flawlessly in the last 9 versisons but suddenly went haywire in this
#version. I removed this class to prioritize the start and end screens.
#class Space(pygame.sprite.Sprite):
#    def __init__(self):
#        pygame.sprite.Sprite.__init__(self)
#        self.image = pygame.image.load("space.gif")
#        self.image = self.image.convert()
#        self.rect = self.image.get_rect()
 
#        self.reset()
#        self.dx = -10
        
#    def update(self):
#        self.rect.left += self.dx
#        if self.rect.left <= -1224:
#            self.reset() 
    
#    def reset(self):
#        self.rect.left = 0

#keeps track of score and lives the player has
class Scoreboard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lives = 5
        self.score = 0
        self.font = pygame.font.SysFont("None", 50)
    
    #text updates with new score and life count
    def update(self):
        self.text = "Shield Level: %d, score: %d" % (self.lives, self.score)
        self.image = self.font.render(self.text, 1, (255, 255, 255))
        self.rect = self.image.get_rect()

#class plays game  
def game():
    pygame.display.set_caption("Star Trek Dark Collective")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    #sprite variables
    ship = Ship()
    intel = Intel()
    power = Power()
    borg1 = Borg()
    borg2 = Borg()
    borg3 = Borg()
    space = Space()
    scoreboard = Scoreboard()

    #groups sprites and update order
    friendSprites = pygame.sprite.OrderedUpdates(space, intel, power, ship)
    borgSprites = pygame.sprite.Group(borg1, borg2, borg3)
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
        
        if ship.rect.colliderect(intel.rect):
            ship.sndComputer.play()
            intel.reset()
            scoreboard.score += 100
        if ship.rect.colliderect(power.rect):
            ship.sndComputer.play()
            power.reset()
            scoreboard.lives += 1
            
        hitBorgs = pygame.sprite.spritecollide(ship, borgSprites, False)
        if hitBorgs:
            ship.sndTorpedo.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
                ship.sndLife.play()
            for theBorg in hitBorgs:
                theBorg.reset()
        
        friendSprites.update()
        borgSprites.update()
        scoreSprite.update()
        
        friendSprites.draw(screen)
        borgSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    #turn off music
    ship.sndSuspense.stop()
    #show mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score
    
def instructions(score):
    ship = Ship()
    space = Space()
    
    allSprites = pygame.sprite.OrderedUpdates(space, ship)
    insFont = pygame.font.SysFont(None, 50)

    instructions = (
    "Star Trek.     Last score: %d" % score ,
    "",
    "Instructions:  You are Captain",
    "Kirk. The Borg are attacking ",
    "and you must, collect intel",
    "to give to the Federation. ",
    "Collect Intel cubes for points ",    
    "and power cubes for shield. ",
    "Avoid the Borg cubes who are",
    "trying to stop you.",
    "",
    "Live Long and Prosper",
    "",
    "Click to start, Press Esc to quit..."
    )

    insLabels = []    
    for line in instructions:
        tempLabel = insFont.render(line, 1, (255, 255, 255))
        insLabels.append(tempLabel)
 
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                donePlaying = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
                donePlaying = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    donePlaying = True
    
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
    
    #ends background music    
    ship.sndSuspense.stop()
    pygame.mouse.set_visible(True)
    return donePlaying

#starts program
def main():
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            score = game()

if __name__ == "__main__":
    main()