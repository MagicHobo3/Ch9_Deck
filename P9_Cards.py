"""________________________________________________________________
-------------------------------------------------------------------
Program:        Text editor
Author:         Tyler Jusczak
Date Modified : 11/06/20
Version :       1.0
Purpose:

    Simulate a deck of cards with images. Deal, shuffle, and get a new deck.

___________________________________________________________________
-------------------------------------------------------------------"""
from breezypythongui import EasyFrame
from tkinter import PhotoImage
from deck import Deck


class CardDemo(EasyFrame):

    def __init__(self):
        """Creates the dice, and sets up the Images and labels
        for the two dice to be displayed, the state label,
        and the two command buttons."""
        EasyFrame.__init__(self, title = "Card Demo")
        self.setSize(220, 200)
        self.mainDeck = Deck()
        self.dealtCard = "b"

        self.cardPanel = self.addPanel(row = 0, column = 0)

        self.deckLabel1 = self.cardPanel.addLabel("", row = 0,
                                       column = 0,
                                       sticky = "NSEW")
        self.stateLabel = self.cardPanel.addLabel("", row = 1, column = 0,
                                        sticky = "NSEW",
                                        columnspan = 2)

        self.buttonPanel = self.addPanel(row = 1, column = 0)
        self.buttonPanel.addButton(row = 2, column = 0,
                       text = "Deal",
                       command = self.deal)
        self.buttonPanel.addButton(row = 2, column = 1,
                       text = "Shuffle",
                       command = self.shuffle)
        self.buttonPanel.addButton(row = 2, column = 2,
                       text = "New deck",
                       command = self.newDeck)

        self.refreshImages()

    def deal(self):
        """Displays the top card and removes it from the deck"""
        self.dealtCard = self.mainDeck.deal()
        self.refreshImages()

    def shuffle(self):
        self.mainDeck.shuffle()
        self.refreshImages()

    def newDeck(self):
        self.mainDeck.reset()
        self.dealtCard = "b"
        self.refreshImages()

    def refreshImages(self):
        """Updates the images in the window."""
        fileName1 = "DECK/" + str(self.dealtCard) + ".gif"
        self.image1 = PhotoImage(file = fileName1)
        self.deckLabel1["image"] = self.image1
        if self.dealtCard != "b":
            print(self.dealtCard)
            self.stateLabel["text"] = self.mainDeck.getName(str(self.dealtCard))

def main():
    CardDemo().mainloop()

if __name__ == "__main__":
    main()
