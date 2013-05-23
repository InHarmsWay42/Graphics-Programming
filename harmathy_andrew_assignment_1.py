#Name: Andrew Harmathy
#Date: May 23, 2013
#Last modified: May 23, 2013
#Version: 1.0
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
        while door != 'Door' and door != 'door' and door != 'Window' and door != 'window' :
                print ('Do you check the door or escape through the window? (Door or Window)')
                door = raw_input()
        return door

#takes in choice from thumpChoose() and activate one of two functions depending on the choice
def escape(thumpChoose):
        if thumpChoose == 'Door' or thumpChoose == 'door': 
                doorChoice()
        elif thumpChoose == 'Window' or thumpChoose == 'window':
                windowChoice()

#################################DOOR PATH#############################################

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
        print ('You could try killing every zombie so you have more time to leave.')
        print ('Or you could try making a run for it and forget your gear.')
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
        print ('Worse yet, every nearby zombie has heard you and is now')
        print ('converging on your position.')
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
                print ('You attempted to fight against the zombies, despite the')
                print ('odds.')
                time.sleep(1)
                print ('With absolutely no combat training or movie plot, you were')
                print ('quickly overwhelmed and killed.')
                time.sleep(2)
                print ('What were you thinking?')
        elif survivalChoice == 'flight' or survivalChoice == 'Flight' :
                print ('Deciding you are too outnumbered, you decided to run.')
                time.sleep(1)
                print ('Sadly there are hundreds on zombies on the streets.')
                print ('You managed to jump by a few, but they quickly surrounded')
                print ('you and ate you.')
                time.sleep(2)
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
                stay()
        elif feelingChoice == 'Leave' or feelingChoice == 'leave' :
                leave()

#user chooses to stay and fight the few zombies
def stay():
        print ('You chose to stay and kill the few zombies in your yard.')
        time.sleep(1)
        print ('You take out your crowbar and smash in the head of the first')
        print ('zombies near you.')
        time.sleep(1)
        print ('The zombies are now aware of you and start moving towards you.')
        time.sleep(1)
        print ('You are so focused on killing the zombies that you do not see')
        print ('the crawler on the ground moving towards you.')
        time.sleep(1)
        print ('The crawler grabs you and bites your leg.')
        time.sleep(1)
        print ('You are now infected.')
        time.sleep(1)
        print ('You are a dead man. Even so, you have a choice.')
        time.sleep(1)
        print ('You can keep fighting and take down as many ghouls as you can')
        print ('before your passing.')
        time.sleep(1)
        print ('Or you can take your gun out and make it quick.')
        #variable created to store value from survivalChoice()
        dieType = dieChoice()
        ending34(dieType)

#user picks whether to fight the zombies or run
def dieChoice():
        die = ''
        while die != 'fight' and die != 'Fight' and die != 'die' and die != 'Die':
                print ('Which do you choose? (Fight or Die)')
                die = raw_input()
        return die

#takes in choice from dieChoice() and activates one of two endings
def ending34(dieChoice):
        if dieChoice == 'fight' or dieChoice == 'Fight' :
                print ('You continue to fight, taking down as many zombies')
                print ('as you can.')
                time.sleep(1)
                print ('In the following ten minutes, you took down at least')
                print ('fifty zombies. Sadly they kept coming. You were soon')
                print ('overwhelmed.')
                time.sleep(3)
                print ('You are now a zombie.')

        elif dieChoice == 'die' or dieChoice == 'Die' :
                print ('You take out your 9mm and point it at your head.')
                time.sleep(3)
                print ('You should have left when you had the chance.')     

#user chooses to leave
def leave():
        print ('Fighting zombies now is too risky. Not when you are so close')
        print ('to getting away.')
        time.sleep(1)
        print ('You hop the fence and make your way out of the neighbourhood.')
        time.sleep(1)
        print ('Now where do you go?')
        time.sleep(1)
        print ('Do you head to the city, hoping for supplies or help?')
        time.sleep(1)
        print ('Or do you head to the countryside and get as far away from')
        print ('the population as you can?')
        #variable created to store value from leaveChoice()
        leaveType = leaveChoice()
        ending56(leaveType)

#user picks when to go to the city or the countryside
def leaveChoice():
        leave = ''
        while leave != 'country' and leave != 'Country' and leave != 'city' and leave != 'City':
                print ('Which do you choose? (City or Country)')
                leave = raw_input()
        return leave

#takes in choice from dieChoice() and activates one of two endings (one where the person dies
#going to the city and one where they live going to the country)
def ending56(leaveChoice):
        if leaveChoice == 'City' or leaveChoice == 'city' :
                print ('You decide to try going to the city.')
                time.sleep(1)
                print ('You reach the nearest one and...')
                time.sleep(1)
                print ('...')
                time.sleep(1)
                print ('It is completely swarming.')
                time.sleep(1)
                print ('You are killed by the swarm.')              
                time.sleep(1)
                print ('You do not watch zombie movies, do you?')
                time.sleep(2)
        elif leaveChoice == 'country' or leaveChoice == 'Country' :
                print ('You realize it would be silly to head to a city')
                print ('and so you head to the country.')
                time.sleep(1)
                print ('You run into other like-minded survivors and form a')
                print ('group.')
                time.sleep(1)
                print ('You all made it out and are living peacefully out in the')
                print ('country. You are safe.')
                time.sleep(2)
                print ('For now...')
                time.sleep(2)
        
def main():
        playAgain = 'yes'
        while playAgain == 'yes' or playAgain == 'y':
                displayIntro()
                escapeChoice = thumpChoose()
                escape(escapeChoice)
        
                print ('Do you want to play again? (yes or no)')
                playAgain = raw_input()


if __name__ == "__main__": main()
