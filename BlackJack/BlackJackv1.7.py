"""
Version 1.7
Black Jack Card Game

Now With Black Jack!!!

Coded in gedit on Kali Linux dsitro 
Python Version 3.9.9 

Added Double Down Option
Program will only ask if the player has enough money to double their bet and does not have black jack

"""

import random
import time



#############
#HARD VALUES#
#############

# Values required to build card deck

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
            

#Intro
print("\033[1;33;40mWelcome to the Black Jack Table")
print("")

def rules():
	print("\033[1;32;40mRULES:")
	print("\033[1;37;40m=>Beat the Dealers Hand Value Without Going Over 21")
	print("=>Don't go bust! (over 21)")
	print("=>Cards 2 - 10 have face value")
	print("=>Jacks, Queens, Kings have a vlue of 10")
	print("=>Aces can be 1 or 11")
	#print("Ace and a face card are an automatic win") 
	print("=>Ties go to dealer")
	print("\n\n")

print("You have \033[1;32;40m$100 \033[1;33;40mDollars to bet with!\n\n")

#########
#CLASSES#
#########

#Deck and Card Classes for building deak and drawing cards

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


###########
#FUNCTIONS#
###########

### Player Bet Function
#Get their bet and make sure it is <= to their Money



def getPlayerBet():
	
	bet=0
	print("\033[1;36;40mYou have \033[1;32;40m${} \033[1;36;40mto bet".format(players_money))
	while bet > players_money or bet <= 0:
		
		bet = int(input("Place your bet:\033[1;32;40m"))
		
		if bet > players_money or bet < 1:
			print("Invalid choice you have \033[1;32;40m${} to bet with".format(players_money))
			
	return int(bet)


#Get the total value of the cards and display their full names
#Added an extra step that will check and reduce an aces value to 1
#if the total is above 21. 

def getSum(cardlist,name):
	total = 0
	print("\n\033[1;33;40m{} Cards are: \033[1;37;40m".format(name))
	for n in range(len(cardlist)):
		time.sleep(.5)
		print(cardlist[n])
		
		total += cardlist[n].value
		
	for n in range(len(cardlist)):
		if total > 21 and cardlist[n].value == 11:
			total -= 10
	
	time.sleep(1)	
	print("{} current total is: {}\n".format(name,total))
	time.sleep(1)
	return int(total)


###Double Down Ask?
def doubleDown(bet,playersSum):
	
	if bet * 2 <= players_money and playersSum < 21:
	
		ask = ''
	
		while ask not in ['Y','N','yes','no','y','n']:
			ask = input("\033[1;36;40mDo you want to Double Down?")
		
			if ask in ['Y','yes','y']:
				print("Your bet is now:  \033[1;32;40m${}".format(bet *2))
				return int(bet * 2)
			
	else:
		return bet 
	



###Function to check if the player or dealer busts
	
def checkSum(number,name):
	if int(number) > 21 and name == 'player':
		print("\033[1;31;40m Oh No! A Bust!!!\n")
		#print("The Dealer Wins!")
		return True
	
	elif int(number) > 21 and name == 'dealer':
		print("\033[1;31;40mThe Dealer Busts!\n")
		return False


#Dealers logic:
#  Check if dealers total is less then the players. 
#  The dealer will draw cards until they bust or meet/exceed the players value  

def dealers_logic(pSum,dealersSum):
	
	while int(dealersSum) < int(pSum) and playerBust == False:
		print("\033[1;34;40m*The Dealer Hits!!!*")
		dealers_cards.append(new_deck.deal_one())
		dealersSum=getSum(dealers_cards,"The Dealer's")
		
		if checkSum(dealersSum,'dealer') == False:
			return False
		
				
		
	if int(pSum) > 21 or int(dealersSum) >= int(pSum) or playerBust == True :
		return True

#See if the player wants to keep playing
		
def GameOn_choice():
	
	choice = 'wrong'
	
	while choice not in ['Y','N','yes','no','y','n']:
	
		choice = input("\033[1;36;40mDo you want to keep playing (Y or N): ")
		
		if choice not in ['Y','N','y','n','yes','no']:
			print("\033[1;36;40mSorry, that was not a valid choice ")
			
	if choice in  ["Y","y","yes"]:
		
		return True
	else:
		
		if players_money > 100:
			wins = players_money - 100
			print("Goodbye! You Made \033[1;32;40m${}".format(wins))
		
		elif players_money < 100:
			loss = 100 - players_money
			print("Comeback anytime! You lost \033[1;32;40m${}".format(loss))
		time.sleep(2)	
		return False	
		
#Game Setup


#####################
#Running the Program#
#####################

#Starting perameters

rules()
game_on = True
players_money = 100

while game_on:

	playerBust = False #reset players bust status
	new_deck = Deck()  #Get a Fresh Deck
	new_deck.shuffle() #Deck Needs to Reshuffle Everytime	
	players_cards =[]
	dealers_cards =[]

###Get Bet the palyers bet

	bet = getPlayerBet()

### Deal Cards first two cards for Player and Dealer and show totals

#Players starting cards
	players_cards.append(new_deck.deal_one())
	players_cards.append(new_deck.deal_one())
	playersSum=getSum(players_cards,"Your")
	print("\n")

#Dealers Starting cards 
	dealers_cards.append(new_deck.deal_one())
	dealers_cards.append(new_deck.deal_one())
	print("\033[1;33;40mThe Dealers First Card is a:")
	time.sleep(.5)
	print("\033[1;37;40m{}".format(dealers_cards[0]))
	print("\n")
	time.sleep(1)



#Double Down? 
	bet = doubleDown(bet,playersSum)

### Hit or Stay and check for Bust. Adjust the players sum if they hit
### and confirm if they bust.

	
	choice = 'wrong'


	while choice not in ['s','S','Stay','stay','STAY'] and playerBust == False:
		choice = input("\033[1;36;40mDo you want to Hit or Stay?")
		
		if choice not in ['s','S','Stay','stay','STAY','h','H','Hit','hit','HIT']:
			print("\033[1;36;40mSorry, that was not a valid choice ")
	
		elif choice in ['h','H','Hit','hit','HIT']:
			players_cards.append(new_deck.deal_one())
			playersSum = getSum(players_cards,"Your")
			if checkSum(playersSum,'player') == True:
				playerBust = True



#Show the Dealers Cards if the player didn't bust
	
	if playersSum <= 21:
		dealersSum=getSum(dealers_cards,"The Dealer's")
			
	else:
		dealersSum = 1 #Random Filler to keep the program 
			       #moving if the palyer busts
	
### Dealer Turn and check for Black Jack
### Check if they've already beat the player or Draw cards until they doS

	if len(dealers_cards) == 2 and dealersSum == 21:
		print("\033[1;33;40mThe Dealer Gets Black Jack and Wins")
		print("\033[1;32;40mYou Lost \033[1;31;40m${}".format(bet))
		players_money -= bet
		
		
	#Check if player has a Black Jack
	
	elif len(players_cards) == 2 and playersSum == 21:
		print("\033[1;33;40mYou Got Black Jack!")
		print("\033[1;32;40mYou Made \033[1;32;40m${}".format(bet))
		players_money += bet

	
	#Check if the Dealer or the player won
		
	elif dealers_logic(playersSum,dealersSum) == True or playerBust == True:
		print("\033[1;33;40mThe Dealer Wins")
		print("\033[1;32;40mYou Lost \033[1;31;40m${}".format(bet))
		players_money -= bet
	
	else:
		print("\033[1;33;40mYou Won!")
		print("\033[1;32;40mYou Made \033[1;32;40m${}".format(bet))
		players_money += bet

### Check if player still has money

	if players_money <= 0:
		print("Looks like you're broke, Goodbye")
		time.sleep(2)
		break

### Would you like to keep playing?

	game_on = GameOn_choice()

