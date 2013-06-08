# Source File Name: slotmachine.py
# Author's Name: Andrew Harmathy
# Last Modified By: Andrew Harmathy
# Date Last Modified: June 8, 2012
#Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
#                        for the user that is an image of a slot machine with Label and Button objects
#                        created through the tkinter module. he results of the machine are based on green
#                        lantern mythos.


"""  Program Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
                        for the user that is an image of a slot machine with Label and Button objects
                        created through the tkinter module. The results of the machine are based on green
                        lantern mythos.

  Version: 0.1 - * Created Back end functions for the slot machine program Reels, pullthehandle, and
                 is_number (a validation function).
                 * Text output provides debugging information to check if the Slot Machine program does
                 what it's supposed to do.
                 * Used research from the internet to set the Reels function to simulate basic slot reels

  Version: 0.2 - *modified outputs to make use of green lantern mythos
                 *modified variable names to reflect the changes of the new outputs

    v 0.3 - *Some of the basic GUI is set up
            *some buttons created for exit, spin and betting
            *image for slot machine is up
            *exit button has function

    v 0.4 - *final betting buttons added
            *reset button added

    v 0.5 - *code from original files added to GUI file
            *reset button added

"""

#import the Tkinter library so that it is available for use
from Tkinter import *
#import random function
import random
#import sys functions
import sys


def Reels():
    """ When this function is called it determines the Bet_Line results
        (based on Green Lantern universe rings).
        e.g. Green Ring - Orange Ring - Yellow Ring """
        
    # [0]Ring, [1]Ring, [2]Ring
    Bet_Line = [" "," "," "]
    Outcome = [0,0,0]
    
    # Spin those reels
    for spin in range(3):
        Outcome[spin] = random.randrange(1,65,1)
        # Spin those Reels!
        if Outcome[spin] >= 1 and Outcome[spin] <=26:   # 40.10% Chance
            Bet_Line[spin] = "Blank"
        if Outcome[spin] >= 27 and Outcome[spin] <=36:  # 16.15% Chance
            Bet_Line[spin] = "Orange Ring"
        if Outcome[spin] >= 37 and Outcome[spin] <=45:  # 13.54% Chance
            Bet_Line[spin] = "Yellow Ring"
        if Outcome[spin] >= 46 and Outcome[spin] <=53:  # 11.98% Chance
            Bet_Line[spin] = "Blue Ring"
        if Outcome[spin] >= 54 and Outcome[spin] <=58:  # 7.29%  Chance
            Bet_Line[spin] = "Red Ring"
        if Outcome[spin] >= 59 and Outcome[spin] <=61:  # 5.73%  Chance
            Bet_Line[spin] = "Sapphire Ring"
        if Outcome[spin] >= 62 and Outcome[spin] <=63:  # 3.65%  Chance
            Bet_Line[spin] = "Indigo Ring"  
        if Outcome[spin] == 64:                         # 1.56%  Chance
            Bet_Line[spin] = "Green Ring"    

    
    return Bet_Line

def is_number(Bet):
    """ This function Checks if the Bet entered by the user is a valid number """
    try:
        int(Bet)
        return True
    except ValueError:
        print("Please enter a valid number or Q to quit")
        return False

def pullthehandle(Bet, Player_Money, Jack_Pot):
    """ This function takes the Player's Bet, Player's Money and Current JackPot as inputs.
        It then calls the Reels function which generates the random Bet Line results.
        It calculates if the player wins or loses the spin.
        It returns the Player's Money and the Current Jackpot to the main function """
    Player_Money -= Bet
    Jack_Pot += (int(Bet*.15)) # 15% of the player's bet goes to the jackpot
    win = False
    Ring_Reel = Reels()
    Rings = Ring_Reel[0] + " - " + Ring_Reel[1] + " - " + Ring_Reel[2]
    
    # Match 3
    if Ring_Reel.count("Orange Ring") == 3:
        winnings,win = Bet*20,True
    elif Ring_Reel.count("Yellow Ring") == 3:
        winnings,win = Bet*30,True
    elif Ring_Reel.count("Blue Ring") == 3:
        winnings,win = Bet*40,True
    elif Ring_Reel.count("Red Ring") == 3:
        winnings,win = Bet*100,True
    elif Ring_Reel.count("Sapphire Ring") == 3:
        winnings,win = Bet*200,True
    elif Ring_Reel.count("Indigo Ring") == 3:
        winnings,win = Bet*300,True
    elif Ring_Reel.count("Green Ring") == 3:
        print("Lucky Seven!!!")
        winnings,win = Bet*1000,True
    # Match 2
    elif Ring_Reel.count("Blank") == 0:
        if Ring_Reel.count("Grapes") == 2:
            winnings,win = Bet*2,True
        if Ring_Reel.count("Banana") == 2:
            winnings,win = Bet*2,True
        elif Ring_Reel.count("Orange") == 2:
            winnings,win = Bet*3,True
        elif Ring_Reel.count("Cherry") == 2:
            winnings,win = Bet*4,True
        elif Ring_Reel.count("Bar") == 2:
            winnings,win = Bet*5,True
        elif Ring_Reel.count("Bell") == 2:
            winnings,win = Bet*10,True
        elif Ring_Reel.count("Seven") == 2:
            winnings,win = Bet*20,True
    
        # Match Lucky Seven
        elif Ring_Reel.count("Seven") == 1:
            winnings, win = Bet*10,True
            
        else:
            winnings, win = Bet*2,True
    if win:    
        print(Rings + "\n" + "You Won $ " + str(int(winnings)) + " !!! \n")
        Player_Money += int(winnings)
    
        # Jackpot 1 in 450 chance of winning
        jackpot_try = random.randrange(1,51,1)
        jackpot_win = random.randrange(1,51,1)
        if  jackpot_try  == jackpot_win:
            print ("You Won The Jackpot !!!\nHere is your $ " + str(Jack_Pot) + "prize! \n")
            Jack_Pot = 500
        elif jackpot_try != jackpot_win:
            print ("You did not win the Jackpot this time. \nPlease try again ! \n")
    # No win
    else:
        print(Rings + "\nPlease try again. \n")
    
    return Player_Money, Jack_Pot, win



#creates the window
#create a top-level window
root = Tk()
#window attributes
root.title("Slot Machine by Andrew Harmathy")
root.geometry("700x550+200+200")
root.configure(background="white")

#create the MyApp Class
class MyApp:
    #define the attributes of the class
    def __init__(self, parent):


        self.myParent = parent
        #creates a frame whose parent is root
        self.myContainer1 = Frame(parent)
        #pack the frame - show it on the screen
        self.myContainer1.pack()

        #image label attributes
        self.myimage = PhotoImage(file="slotmachine.gif")
        self.labelSlotMachine = Label(self.myContainer1)
        self.labelSlotMachine.configure(image = self.myimage)
        self.labelSlotMachine.pack()

        #the tenButton attributes
        self.tenButton = Button(self.myContainer1)
        self.tenButton.configure(text="$10", background="Yellow")
        #display tenButton
        self.tenButton.pack(side=LEFT)
        #Bind tenButton with buttonSpinClick
        self.tenButton.bind("<Button-1>", self.buttonTenClick)

        #the fiftyButton attributes
        self.fiftyButton = Button(self.myContainer1)
        self.fiftyButton.configure(text="$50", background="Yellow")
        #display fiftyButton
        self.fiftyButton.pack(side=LEFT)
        #Bind fiftyButton with buttonFiftyClick
        self.fiftyButton.bind("<Button-1>", self.buttonFiftyClick)

        #the hundredButton attributes
        self.hundredButton = Button(self.myContainer1)
        self.hundredButton.configure(text="$100", background="Yellow")
        #display hundredButton
        self.hundredButton.pack(side=LEFT)
        #Bind hundredButton with buttonHundredClick
        self.hundredButton.bind("<Button-1>", self.buttonHundredClick)

        #the fiveHundButton attributes
        self.fiveHundButton = Button(self.myContainer1)
        self.fiveHundButton.configure(text="$500", background="Yellow")
        #display fiveHundButton
        self.fiveHundButton.pack(side=LEFT)
        #Bind fiveHundButton with buttonfHundClick
        self.fiveHundButton.bind("<Button-1>", self.buttonfHundClick)

        #the thousButton attributes
        self.thousButton = Button(self.myContainer1)
        self.thousButton.configure(text="$1000", background="Yellow")
        #display thousButton
        self.thousButton.pack(side=LEFT)
        #Bind thousButton with buttonthousClick
        self.thousButton.bind("<Button-1>", self.buttonThousClick)

        #the spinButton attributes
        self.spinButton = Button(self.myContainer1)
        self.spinButton.configure(text="Spin", background="green")
        #display spinButton
        self.spinButton.pack(side=RIGHT)
        #Bind spinButton with buttonSpinClick
        self.spinButton.bind("<Button-1>", self.buttonSpinClick)

        #the exitButton attributes
        self.exitButton = Button(self.myContainer1)
        self.exitButton.configure(text="Exit", background="red")
        #display exitButton
        self.exitButton.pack(side=RIGHT)
        #Bind exitButton with buttonExitClick
        self.exitButton.bind("<Button-2>", self.buttonExitClick)

        #the resetButton attributes
        self.resetButton = Button(self.myContainer1)
        self.resetButton.configure(text="Reset", background="Blue")
        #display resetButton
        self.resetButton.pack(side=RIGHT)
        #Bind resetButton with buttonResetClick
        self.resetButton.bind("<Button-2>", self.buttonResetClick)

    #change bet label to reflect the gambler's bet of $10
    def buttonTenClick():
        Bet = 10
        tenBet = ("Bet: " + str(Bet))
        #change betting label to reflect bet
        labelBet.set(tenBet)

    #change bet label to reflect the gambler's bet of $50
    def buttonFiftyClick():
        Bet = 50
        fiftyBet = ("Bet: " + str(Bet))
        #change betting label to reflect bet
        labelBet.set(fiftyBet)

    #change bet label to reflect the gambler's bet of $100
    def buttonHundredClick():
        Bet = 100
        hundredBet = ("Bet: " + str(Bet))
        #change betting label to reflect bet
        labelBet.set(hundredBet)

    #change bet label to reflect the gambler's bet of $500
    def buttonfHundClick():
        Bet = 500
        fhundredBet = ("Bet: " + str(Bet))
        #change betting label to reflect bet
        labelBet.set(fhundredBet)

    #change bet label to reflect the gambler's bet of $1000
    def buttonThousClick():
        Bet = 1000
        thousBet = ("Bet: " + str(Bet))
        #change betting label to reflect bet
        labelBet.set(thousBet)

    #close GUI
    def buttonExitClick(self, event):
        self.myParent.destroy()

    #spin slot machine
    def buttonSpinClick(self, event):
        self.myParent.destroy()

    #close GUI
    def buttonResetClick(self, event):
        self.myParent.destroy()



def main():
    # Initial Values
    Player_Money = 1000
    Jack_Pot = 500
    Turn = 1
    Bet = 0
    Prev_Bet=0
    win_number = 0
    loss_number = 0
    
    #call the MyApp class
    myapp = MyApp(root)


    
    #creates label to display how much money the person has bet
    labelBet = StringVar()
    labelBet.set("Bet: " + str(Bet))
    labelBet = Label(root, textvariable=labelBet, height=1)
    labelBet.pack()

    #creates label to display how much the jackpot is worth
    labelJackpot = StringVar()
    labelJackpot.set("Jackpot: " + str(Jack_Pot))
    labelJackpot = Label(root, textvariable=labelJackpot, height=1)
    labelJackpot.pack()

    #creates label to display how much money the person has
    labelPlayMon = StringVar()
    labelPlayMon.set("Player Money: " + str(Player_Money))
    labelPlayMon = Label(root, textvariable=labelPlayMon, height=1)
    labelPlayMon.pack()

    #execute the mainloop method of the "root" object
    root.mainloop()

    # Flag to initiate the game loop
    KeepGoing = True
    
    while KeepGoing == True:
        win = 0
        # Give the player some money if he goes broke
        if Player_Money <1:
            input("You have no more money. Here is $500 \nPress Enter\n")
            Player_Money = 500
        
        # User Input
        Prompt = raw_input(" Place Your Bet ! \n Jackpot $ " + str(Jack_Pot) + "\n Money $ " + str(Player_Money) + "\n Q = quit \n")
        if Prompt  == "q" or Prompt  == "Q":
            KeepGoing = False
            break
        
        if Prompt == "" and Turn >1:
            Bet = Prev_Bet
            print("Using Previous Bet")
            if Bet > Player_Money:
                print("Sorry, you only have $" + str(Player_Money) + " \n")
            elif Bet <= Player_Money:
                Turn +=1
                Prev_Bet = Bet
                Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        
        elif is_number(Prompt ):
            Bet = int(Prompt )
            # not enough money
            if Bet > Player_Money:
                print("Sorry, you only have $" + str(Player_Money) + " \n")
                
            # Let's Play
            elif Bet <= Player_Money:
                Turn +=1
                Prev_Bet = Bet
                Player_Money, Jack_Pot, win = pullthehandle(Bet, Player_Money, Jack_Pot)
        
        # determine win/loss ratio for debugging purposes
        if win:
            win_number += 1
        else:
            loss_number += 1
        win_ratio = "{:.2%}".format(win_number / Turn)
        print("Wins: " + str(win_number) + "\nLosses: " + str(loss_number) + "\nWin Ratio: " + win_ratio + "\n")           
                
    
    #The End
    print("- Program Terminated -")

if __name__ == "__main__": main()
