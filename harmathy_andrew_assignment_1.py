#Name: Andrew Harmathy
#Date: May 23, 2013
#Description: This is a choose your own adventure where the user selects chooses
#that affect the story. It will end with on of eight endings

import time

#gives background information about the situation
def displayIntro():
        print ('The zombie apocalypse has begun. Already five billion')
        print ('people have fallen to the walking dead. You are currently')
        print ('in your home prepping your gear to leave at any given')
        print ('notice. Suddenly you hear a thumping at your door.')
        print ('What do you do?')

#########################MAJOR CHOICE PATHWAYS#############################################

#user chooses between the door or window
def thumpChoose():
        door = ''
        while door != 'Door' and door != 'door' and door != 'Window' and door != 'window':
                print ('Do you check the door or escape through the window? (Door or Window)')
                door = raw_input()
        return door

#takes in choice from thumpChoose and activate one of two functions depending on the choice
def escape(thumpChoose):
        if thumpChoose == 'Door' or thumpChoose == 'door': 
                doorChoice()
        elif thumpChoose == 'Window' or thumpChoose == 'window':
                windowChoice()

#########################DOOR PATH#############################################

#user approaches door
def doorChoice():
        print ('You approach the door quietly.')
        time.sleep(1)
        print ('You slowly open the door.')
        time.sleep(1)
        print ('You are pushed back as a zombie barges into your home.')
        time.sleep(1)
        print ('You look around for a weapon to use against him.')
        print ('You see a crowbar and a baseball bat.')
        #value created to store value from weaponChoice()
        weaponType = weaponChoice()
        weaponPick(weaponType)

#user picks one of two weapons
def weaponChoice():
        weapon = ''
        while weapon != 'crowbar' and weapon != 'Crowbar' and weapon != 'bat' and weapon != 'Bat':
                print ('Which do you choose? (Crowbar or Bat)')
                weapon = raw_input()
        return weapon

#takes in choice from weaponChoice() and activates one fo two functions
def weaponPick(weaponChoice):
        if weaponChoice == 'Crowbar' or weaponChoice == 'crowbar' :
                crowbar()
        elif weaponChoice == 'Bat' or weaponChoice == 'bat' :
                bat()

#user picks the crowbar
def crowbar():
        print ('You picked up the crowbar.')
        time.sleep(1)
        print ('You smashed the zombie over the head, knocking it to the ground.')
        time.sleep(1)
        print ('While the zombie is on the ground, you take the opportunity to')
        print ('make sure it is dead by using the crowbar a few more times.')
        time.sleep(1)
        print ('Unfortunately, every nearby zombie has heard you and is now converging')
        print ('on your position. You have two choices.')
        time.sleep(1)
        print ('You could try killing every zombie so you have more time to leave. Or you')
        print ('could try making a run for it and forget your gear.')
        #variable created to store value from survivalChoice()
        survivalType = survivalChoice()
        ending12(survivalType)

#user picks the bat
def bat():
        print ('You picked up the bat.')
        time.sleep(1)
        print ('You smashed the zombie over the head, knocking it to the ground.')
        time.sleep(1)
        print ('While the zombie is on the ground, you take the opportunity to')
        print ('make sure it is dead by using the bat a few more times.')
        time.sleep(1)
        print ('The wooden bat breaks.')
        time.sleep(1)
        print ('Worse yet, every nearby zombie has heard you and is now converging on')
        print ('your position.')
        #variable created to store value from survivalChoice()
        survivalType = survivalChoice()
        ending12(survivalType)

#user picks whether to fight the zombies or run
def survivalChoice():
        survival = ''
        while survival != 'fight' and survival != 'Fight' and survival != 'flight' and survival != 'Flight':
                print ('Which do you choose? (Fight or Flight)')
                survival = raw_input()
        return survival

#takes in choice from survivalChoice() and activates one of two endings (becomes four endings as this can result from the
#different paths from going to the door)
def ending12(survivalChoice):
        if survivalChoice == 'fight' or survivalChoice == 'Fight' :
                print ('You attempted to fight against the zombies, despite the odds.')
                time.sleep(1)
                print ('With absolutely no combat training or movie plot, you were quickly overwhelmed')
                print ('and killed.')
                time.sleep(1)
                print ('What were you thinking?')
        elif survivalChoice == 'flight' or survivalChoice == 'Flight' :
                print ('Deciding you are too outnumbered, you decided to run.')
                time.sleep(1)
                print ('Sadly there are hundreds on zombies on the streets. You managed to jump')
                print ('by a few, but they quickly surrounded you and ate you.')
                time.sleep(1)
                print ('You tried at least.')


#########################WINDOW PATH#############################################

def windowChoice():
        print ('You know exactly what is at the door. You focus on quickly')
        print ('finishing your preparations to the sound of thumping at')
        print ('your door.')
        time.sleep(1)
        print ('You finished.')
        time.sleep(1)
        print ('You quietly go to the back of your home and open a window to')
        print ('escape.')
        time.sleep(1)
        print ('You are outside but you see at least five zombies.')
        time.sleep(1)
        print ('In your inventory you have a 9mm pistol and a crowbar.')
        print ('Seeing as there are so few zombies, do you decided to kill')
        print ('them(reducing their numbers) or get out of there?')
        #value created to store value from feelingChoice()
        feelingType = feelingChoice()
        feelingPick(feelingType)

#user decides whether to stay and fight, or leave
def feelingChoice():
        feeling = ''
        while feeling != 'stay' and feeling != 'Stay' and feeling != 'leave' and feeling != 'Leave':
                print ('Which do you choose? (Stay or Leave)')
                feeling = raw_input()
        return feeling

#takes in choice from weaponChoice() and activates one fo two functions
def feelingPick(feelingChoice):
        if feelingChoice == 'Stay' or feelingChoice == 'stay' :
                print ('Stay')
        elif feelingChoice == 'Leave' or feelingChoice == 'leave' :
                print ('Leave')
        
def main():
        
        
        playAgain = 'yes'
        while playAgain == 'yes' or playAgain == 'y':
                displayIntro()
                escapeChoice = thumpChoose()
                escape(escapeChoice)
        
                print ('Do you want to play again? (yes or no)')
                playAgain = raw_input()


if __name__ == "__main__": main()
