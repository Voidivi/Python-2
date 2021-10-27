# !/usr/bin/env python3
# Assignment Week 6 - OOP Card Program
# Author: Lyssette  Williams

#importing random to use for the dealer
import random

#card class to store cards and create the string about the cards as they are dealt
class Card:
	def __init__ (self,rank,suit):
		self.rank = rank
		self.suit = suit

	def getStr(self):
		return str(self.rank) + ' of ' + str(self.suit)


#class to create the 52 cards making up a deck 
class Deck:
	def __init__(self):
		self.__deck = []
		ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
		suits = ['Clubs', 'Spades', 'Hearts', 'Diamonds']
		for rank in ranks:
			for suit in suits:
				self.__deck.append(Card(rank,suit))


	def shuffle(self): #shuffles the deck
		random.shuffle(self.__deck)

	def rainman(self): #counts cards as well as Dustin Hoffman
		return len(self.__deck)

	def deal(self): #deals cards by 'popping' them off the deck
		return self.__deck.pop()		

#basic program display
def display():
	print('Card Dealer')
	print('=' * 35)	

#interaction with the program's 'dealer'
def dealer():
	dealHand = int(input('How many cards would you like?: '))
	print(' ')
	return dealHand	

#runs the main program - first and second time it ran through I thought random was broken because I pulled the exact same card (chose 1 to start) hahaha

def main():
	display()
	deck = Deck()
	deck.shuffle()
	print('I have shuffled a deck of', str(deck.rainman()), 'cards.')
	print(' ')
	numcards = dealer()
	print('Here are your cards:')
	print(' ')
	for i in range(numcards):
		card = deck.deal()
		print(card.getStr())
		print(' ')
	print('There are', str(deck.rainman()) ,"cards left in the deck.")
	print(' ')
	print('Good luck!')

if __name__ == "__main__":
  main() 