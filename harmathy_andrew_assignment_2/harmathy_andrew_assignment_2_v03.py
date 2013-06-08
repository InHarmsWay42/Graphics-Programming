# Source File Name: slotmachine.py
# Author's Name: Andrew Harmathy
# Last Modified By: Andrew Harmathy
# Date Last Modified: June 7, 2012
#Description:  This program simulates a Casino-Style Slot Machine. It provides an GUI
#                        for the user that is an image of a slot machine with Label and Button objects
#                        created through the tkinter module


""" v 0.3 - *Some of the basic GUI is set up
            *some buttons created for exit, spin and betting
            *image for slot machine is up

"""

#import the Tkinter library so that it is available for use
from Tkinter import *
#import random function
import random
#import sys functions
import sys

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

    #change bet label to reflect the gambler's bet of $10
    def buttonTenClick():
        Bet = 10
        tenBet = ("Bet: " + str(Bet))
        labelBet.set(tenBet)

    #change bet label to reflect the gambler's bet of $50
    def buttonFiftyClick():
        Bet = 50
        fiftyBet = ("Bet: " + str(Bet))
        labelBet.set(fiftyBet)

    #change bet label to reflect the gambler's bet of $100
    def buttonHundredClick():
        Bet = 100
        hundredBet = ("Bet: " + str(Bet))
        labelBet.set(hundredBet)

    #change bet label to reflect the gambler's bet of $500
    def buttonfHundClick():
        Bet = 500
        fhundredBet = ("Bet: " + str(Bet))
        labelBet.set(fhundredBet)

    #close GUI
    def buttonExitClick(self, event):
        self.myParent.destroy()

    #spin slot machine
    def buttonSpinClick(self, event):
        self.myParent.destroy()

#close GUI
def buttonSpinClick():
    sys.exit(0)



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

if __name__ == "__main__": main()
