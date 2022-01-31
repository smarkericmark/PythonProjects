"""
Version 1.0
Black Jack Card Game
coded in gedit on Kali Linux dsitro 
Python Version 3.9.9 
"""

import random


# Values required to build card deck

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
            

#Intro
print("Welcome to the Black Jack Table")
print("")

def rules():
	print("Rules:")
	print("Beat the Dealers Hand Value Without Going Over 21")
	print("Don't go bust! (over 21)")
	print("Cards 2 - 10 have face value")
	print("Jacks, Queens, Kings have a vlue of 10")
	print("Aces can be 1 or 11")
	#print("Ace and a face card are an automatic win") 
	print("Ties go to dealer")
	print("\n\n\n")

print("You have $100 Dollars to bet with!\n\n\n")


#Deck and Card Classes

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit 
        
class Deck :

	def __init__(self):
		
		self.all_cards = []
		
		for suit in suits:
			for rank in ranks:
				
				created_card = Card(suit,rank)
				self.all_cards.append(created_card)
				
	def shuffle(self):
		
		random.shuffle(self.all_cards)
	
	def deal_one(self):
		return self.all_cards.pop()
		

###Player Class

class Player:
	def __init__(self,name):
	
		self.name = name
		self.all_cards = []
	
	def remove_one(self):
		return self.all_cards.pop(0)
		
	def add_cards(self,new_cards):
	
		self.all_cards.append(new_cards)






### Player Bet Function

def getPlayerBet():
	
	bet=0
	print("\033[1;36;40mYou have \033[1;32;40m${} \033[1;36;40mto bet".format(players_money))
	while bet > players_money or bet <= 0:
		
		bet = int(input("Place your bet:\033[1;32;40m "))
		
		if bet > players_money or bet < 1:
			print("Invalid choice you have \033[1;32;40m${} to bet with".format(players_money))
			
	return int(bet)


#get sum of card values


def getNames(cardlist):
	pass
	

def getSum(cardlist,name):
	total = 0
	print("{} Cards are: ".format(name))
	for n in range(len(cardlist)):
		
		print(cardlist[n])
		
		total += cardlist[n].value
		
	for n in range(len(cardlist)):
		if total > 21 and cardlist[n].value == 11:
			total -= 10
		
	print("{} current total is: {}\n".format(name,total))
	return int(total)
	
def checkSum(number,name):
	if int(number) > 21 and name == 'player':
		print("You Busted!!!\n")
		#print("The Dealer Wins!")
		return True
	
	elif int(number) > 21 and name == 'dealer':
		print("The Dealer Busted!\n")
		return False


def getPlayerChoice(hand):
	pass

def dealers_logic(pSum,dealersSum):
	
	while int(dealersSum) < int(pSum) and playerBust == False:
		dealers_cards.append(new_deck.deal_one())
		dealersSum=getSum(dealers_cards,"The Dealer's")
		if checkSum(dealersSum,'dealer') == False:
			return False
		
	if int(pSum) > 21 or int(dealersSum) >= int(pSum) or playerBust == True :
		#print("The Dealer Wins!")
		return True
		
		
		
	



#Game Setup

player_one = Player("One")
dealer = Player("Dealer")


'''
game_on = True
players_money = 100

while game_on:

	#deck needs to be reshuffled every time
		
	new_deck = Deck()
	new_deck.shuffle()
	
	players_cards =[]
	dealers_cards = []
'''

playerBust = False
new_deck = Deck()
new_deck.shuffle()	
players_cards =[]
dealers_cards =[]

#print(players_cards)

players_cards.append(new_deck.deal_one())
players_cards.append(new_deck.deal_one())
playersSum=getSum(players_cards,"Your")
print("\n\n")
dealers_cards.append(new_deck.deal_one())
dealers_cards.append(new_deck.deal_one())
dealersSum=getSum(dealers_cards,"The Dealer's")

print("\n\n")


choice = 'wrong'


while choice not in ['s','S','Stay','stay','STAY'] and playerBust == False:
	choice = input("\033[1;36;40mdo you want to Hit or Stay?")
		
	if choice not in ['s','S','Stay','stay','STAY','h','H','Hit','hit','HIT']:
		print("\033[1;36;40mSorry, that was not a valid choice ")
	
	elif choice in ['h','H','Hit','hit','HIT']:
		players_cards.append(new_deck.deal_one())
		playersSum = getSum(players_cards,"Your")
		if checkSum(playersSum,'player') == True:
			playerBust = True
	
	#else:
		#playersSum = getSum(players_cards,"Your")
							

if dealers_logic(playersSum,dealersSum) == True or playerBust == True:
	print("The Dealer Wins")
	
else:
	print("You Won!")



####Running the Program

###Get Bet

### Deal Cards

### Hit or Stay

### Double Down?

### Dealer Goes

### Add or subtract money

### Are you Broke?

### Would you like to keep playing
		
