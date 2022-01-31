"""
Version 1.0
Script simulates the card game War between two computer oppenents
coded in gedit on Kali Linux dsitro 

Python Version 3.9.9 
"""
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}



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

# Uncomment below to test Deck class		

#new_deck = Deck()
#new_deck.shuffle()
#bottom_card = new_deck.all_cards[-1]
#print(bottom_card)

class Player:
	def __init__(self,name):
	
		self.name = name
		self.all_cards = []
	
	def remove_one(self):
		return self.all_cards.pop(0)
		
	def add_cards(self,new_cards):
	
		#for a list of cards getting added to the deck
		if type(new_cards) == type([]):
			self.all_cards.extend(new_cards)
		
		#for a single card getting added to player deck
		else:
			self.all_cards.append(new_cards)	
		
		
	def __str__(self):
		return f'Player {self.name} has {len(self.all_cards)} cards.'
	
#Uncomment to test Player class. Requires Deck class tests to be uncommented
#new_player = Player("Jose")
#print(new_player)
#new_player.add_cards(bottom_card)	
#print(new_player)
#new_player.add_cards([bottom_card,bottom_card,bottom_card])
#print(new_player)	
#new_player.remove_one()
#print(new_player)



#Game Setup

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()


# split the 52 card deck in half and give 26 cards to each player

for x in range (26):
	player_one.add_cards(new_deck.deal_one())
	player_two.add_cards(new_deck.deal_one())
	
#uncomment lines below to test/confirm deck split
#print(len(player_one.all_cards))
#print(player_one.all_cards[0])

game_on = True

round_num = 0

#Game loop

while game_on:
	
	round_num += 1
	print(f"Round Number: {round_num}")
	
	#Check if players are out of cards and game is over
	
	if len(player_one.all_cards) <= 0:
		print("Player One is out of cards")
		print("Player Two Wins!")
		game_on= False
		break
		
	if len(player_two.all_cards) <= 0:
		print("Player Two is out of cards")
		print("Player One Wins!")
		game_on= False
		break
	
	#Start the round
	
	player_one_cards = [] # think of these as face up played cards
	player_one_cards.append(player_one.remove_one())
	
	player_two_cards = []
	player_two_cards.append(player_two.remove_one())
	

	at_war = True
	
	while at_war:
	
		if player_one_cards[-1].value > player_two_cards[-1].value:
		
			player_one.add_cards(player_one_cards)
			player_one.add_cards(player_two_cards)
		
			at_war = False
		
		elif player_two_cards[-1].value > player_one_cards[-1].value:
		
			player_two.add_cards(player_two_cards)
			player_two.add_cards(player_one_cards)
			
			at_war = False

		else:
			print("WAR!!!")
			
			if len(player_one.all_cards) < 5:
				print("Player One Unable to Declare War!")
				print("Player Two Wins!")
				game_on = False
				break
				
			elif len(player_two.all_cards) < 5:
				print("Player Two Unable to Declare War!")
				print("Player One Wins!")
				game_on = False
				break 
				
			else:
				for num in range(5):
					player_one_cards.append(player_one.remove_one())
					player_two_cards.append(player_two.remove_one())
					















