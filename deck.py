"""
File: deck.py

This module defines the Deck class.
"""

import random

class Deck(object):
    """This class represents a deck of cards."""

    def __init__(self):

        self.reset()

    def shuffle(self):
        """Shuffles all the cards in the deck to random positions"""
        random.shuffle(self.deck)

    def deal(self):
        """Returns the value of the top card of the deck then takes it out of the list ."""
        return self.deck.pop(0)

    def reset(self):
        """Creates a new deck with images names corresponding to the 52 cards.
        Standard deck of cards order go, 2 jokers, then spade and diamonds
        Ace through king. Then hearts and clubs, king through ace."""
        self.deck = []
        self.deck.append("j")
        self.deck.append("j")
        for spade in range(1,14):
            self.deck.append(str(spade) + "s")
        for diamond in range(1,14):
            self.deck.append(str(diamond) + "d")

        cardOrder = 13
        for heart in range(1,14):
            self.deck.append(str(cardOrder) + "h")
            cardOrder -= 1
        cardOrder = 13
        for club in range(1,14):
            self.deck.append(str(cardOrder) + "c")
            cardOrder -= 1

    def getName(self,card):
        """ Splits input card to get number and suit of the card.
            Then returns the correct name to that card"""
        cardInfo = card.split(card[-1])
        num = cardInfo[0]
        suit = card[-1]
        suitName = ""

        if num == "1":
            rank = 'Ace'
        elif num == "11":
            rank = 'Jack'
        elif num == "12":
            rank = 'Queen'
        elif num == "13":
            rank = 'King'
        else:
            rank = num

        if suit == "s":
            suitName = "Spades"
        elif suit == "d":
            suitName = "Diamonds"
        elif suit == "h":
            suitName = "Hearts"
        elif suit == "c":
            suitName = "Clubs"
        else:
            suitName = "Joker"

        if suit == "j":
            return "Joker"
        else:
            return str(rank) + ' of ' + suitName

    def __str__(self):
        """Returns the full list of cards in the deck."""
        return str(self.deck)
