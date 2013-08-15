#Author: Andrew Harmathy and Leugim Lim
#Last Modified by: Andrew Harmathy
#Date: August 13, 2013
#Description: A game where the player plays as the enterprise as it dodges borg ships.
#The player also has to gather intel blocks for points.
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
#Version 1.0: Introduction screen added.
#Version 1.1: End game screen added. Difficulty selection added. Torpedo sprites added for
#hard and medium difficulty
#Version 1.2: Extreme difficulty added. Splash screen placed in.
    
import pygame, random
import Tkinter as tk
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
        
#creates torpedo sprites that move from left to right
class Torpedo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("torpedo.gif")
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
        
        self.dx = -10
    
    #sprite moves right to left 
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right < 0:
            self.reset()
    
    #sprite resets when it reaches the left
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

#class plays game on easy mode 
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
        
        #clears sprites
        friendSprites.clear(screen, background)
        borgSprites.clear(screen, background)
        scoreSprite.clear(screen, background)
        
        #updates sprites
        friendSprites.update()
        borgSprites.update()
        scoreSprite.update()
        
        #draws sprites
        friendSprites.draw(screen)
        borgSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    #turn off music
    ship.sndSuspense.stop()
    #show mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

#class plays game on medium difficulty 
def gamem():
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
    torpedo1 = Torpedo()
    torpedo2 = Torpedo()
    space = Space()
    scoreboard = Scoreboard()

    #groups sprites and update order
    friendSprites = pygame.sprite.OrderedUpdates(space, intel, power, ship)
    borgSprites = pygame.sprite.Group(borg1, borg2, borg3)
    torpSprites = pygame.sprite.Group(torpedo1, torpedo2)
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
                
        hitTorpedo = pygame.sprite.spritecollide(ship, torpSprites, False)
        if hitTorpedo:
            ship.sndTorpedo.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
                ship.sndLife.play()
            for theTorpedo in hitTorpedo:
                theTorpedo.reset()
        
        #clears sprites
        friendSprites.clear(screen, background)
        borgSprites.clear(screen, background)
        torpSprites.clear(screen, background)
        scoreSprite.clear(screen, background)
        
        #updates sprites
        friendSprites.update()
        borgSprites.update()
        torpSprites.update()
        scoreSprite.update()
        
        #draws sprites
        friendSprites.draw(screen)
        borgSprites.draw(screen)
        torpSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    #turn off music
    ship.sndSuspense.stop()
    #show mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

#class plays game on hard difficulty
def gameh():
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
    torpedo1 = Torpedo()
    torpedo2 = Torpedo()
    torpedo3 = Torpedo()
    space = Space()
    scoreboard = Scoreboard()

    #groups sprites and update order
    friendSprites = pygame.sprite.OrderedUpdates(space, intel, power, ship)
    borgSprites = pygame.sprite.Group(borg1, borg2, borg3)
    torpSprites = pygame.sprite.Group(torpedo1, torpedo2, torpedo3)
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
                
        hitTorpedo = pygame.sprite.spritecollide(ship, torpSprites, False)
        if hitTorpedo:
            ship.sndTorpedo.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
                ship.sndLife.play()
            for theTorpedo in hitTorpedo:
                theTorpedo.reset()
        
        #clears sprites
        friendSprites.clear(screen, background)
        borgSprites.clear(screen, background)
        torpSprites.clear(screen, background)
        scoreSprite.clear(screen, background)
        
        #updates sprites
        friendSprites.update()
        borgSprites.update()
        torpSprites.update()
        scoreSprite.update()
        
        #draws sprites
        friendSprites.draw(screen)
        borgSprites.draw(screen)
        torpSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    #turn off music
    ship.sndSuspense.stop()
    #show mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

#class plays game on extreme difficulty
def gamek():
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
    borg4 = Borg()
    torpedo1 = Torpedo()
    torpedo2 = Torpedo()
    torpedo3 = Torpedo()
    torpedo4 = Torpedo()
    space = Space()
    scoreboard = Scoreboard()

    #groups sprites and update order
    friendSprites = pygame.sprite.OrderedUpdates(space, intel, power, ship)
    borgSprites = pygame.sprite.Group(borg1, borg2, borg3, borg4)
    torpSprites = pygame.sprite.Group(torpedo1, torpedo2, torpedo3, torpedo4)
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
                
        hitTorpedo = pygame.sprite.spritecollide(ship, torpSprites, False)
        if hitTorpedo:
            ship.sndTorpedo.play()
            scoreboard.lives -= 1
            if scoreboard.lives <= 0:
                keepGoing = False
                ship.sndLife.play()
            for theTorpedo in hitTorpedo:
                theTorpedo.reset()
        
        #clears sprites
        friendSprites.clear(screen, background)
        borgSprites.clear(screen, background)
        torpSprites.clear(screen, background)
        scoreSprite.clear(screen, background)
        
        #updates sprites
        friendSprites.update()
        borgSprites.update()
        torpSprites.update()
        scoreSprite.update()
        
        #draws sprites
        friendSprites.draw(screen)
        borgSprites.draw(screen)
        torpSprites.draw(screen)
        scoreSprite.draw(screen)
        
        pygame.display.flip()
    
    #turn off music
    ship.sndSuspense.stop()
    #show mouse cursor
    pygame.mouse.set_visible(True) 
    return scoreboard.score

#instructions screen and game introduction
def instructions(score):
    #draws background for instructions
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
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
                elif event.key == pygame.K_SPACE:
                    keepGoing = False
                    donePlaying = False
                elif event.key == pygame.K_BACKSPACE:
                    keepGoing = False
                    donePlaying = False
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
    
    #ends background music    
    ship.sndSuspense.stop()
    pygame.mouse.set_visible(True)
    return donePlaying

#allows player to choose difficulty
def difficultyChoose():
    #draws background for difficulty selection screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Ship()
    space = Space()
    
    allSprites = pygame.sprite.OrderedUpdates(space, ship)
    insFont = pygame.font.SysFont(None, 50)

    diffSelect = (
    "",
    "",
    "",
    "",
    "Choose your difficulty:",
    "Red Shirt (EASY) - Mouse Click",
    "Blue Shirt (MEDIUM) - Spacebar",
    "Yellow Shirt (HARD) - Backspace",
    "Admiral (EXTREME) - E key"
    )

    insLabels = []    
    for line in diffSelect:
        tempLabel = insFont.render(line, 1, (255, 255, 255))
        insLabels.append(tempLabel)
 
    #accepts user inputs for difficulty selection
    keepGoing = True
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                difficulty = 1
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    difficulty = 2
                    keepGoing = False
                elif event.key == pygame.K_BACKSPACE:
                    difficulty = 3
                    keepGoing = False
                elif event.key == pygame.K_e:
                    difficulty = 4
                    keepGoing = False
        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
    
    #ends background music    
    ship.sndSuspense.stop()
    pygame.mouse.set_visible(True)
    return difficulty

#game ends and end game screen appears
def tryAgain(score):
    #draws bckground for tryAgain screen
    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    ship = Ship()
    space = Space()
    
    allSprites = pygame.sprite.OrderedUpdates(space, ship)
    insFont = pygame.font.SysFont(None, 50)

    instructions = (
    "",
    "Star Trek.     Last score: %d" % score ,
    "",
    "",
    "",
    "",
    "The Borg collective has destroyed",
    "the Enterprise. They are now free",
    "to assimilate the entire galaxy",
    "Try to stop them again? Click ",
    "down on mouse button.",
    "Give up? Press ESC."
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                keepGoing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    keepGoing = False
                    raise SystemExit

        
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)

        for i in range(len(insLabels)):
            screen.blit(insLabels[i], (50, 30*i))

        pygame.display.flip()
    
    #ends background music    
    ship.sndSuspense.stop()
    pygame.mouse.set_visible(True)

#creates splash screen that appears in front of program
def splash():
    root = tk.Tk()
    #shows no frame
    root.overrideredirect(True)
    #gives dimensions
    width = 1000
    height = 700
    root.geometry('%dx%d+%d+%d' % (width, height, width*0.1, height*0.1))

    #gives vatriable identifier for image file
    image_file = "startrek.gif"
    # use Tkinter's PhotoImage for .gif files
    image = tk.PhotoImage(file=image_file)
    #creates canvas
    canvas = tk.Canvas(root, height=height, width=width, bg="black")
    canvas.create_image(width/2, height/2, image=image)
    canvas.pack()

    # the splash screen is shown for 3 seconds before it is destroyed
    root.after(3000, root.destroy)
    root.mainloop()

#starts program
def main():
    splash()
    donePlaying = False
    score = 0
    while not donePlaying:
        donePlaying = instructions(score)
        if not donePlaying:
            #player chooses difficulty level
            difficulty = difficultyChoose()
            #different game plays depending on which difficulty level is selected
            if difficulty == 1:
                score = game()
                tryAgain(score)
            elif difficulty == 2:
                score = gamem()
                tryAgain(score)
            elif difficulty == 3:
                score = gameh()
                tryAgain(score)
            elif difficulty == 4:
                score = gamek()
                tryAgain(score)

if __name__ == "__main__":
    main()