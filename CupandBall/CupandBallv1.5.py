#Written in gedit
#tested on Kali 64x Linux Distro using Python 3.9.9

#Version 1.5 changes
# Allows betting and tracking of users bet
# When the user runs out of money the program terminates
# To test comment out line 181 to turn off randomizer


#Used to randomize where the red ball is

import time
from random import shuffle


#Intro Text

print("\033[1;36;40mHello! Step right up and play the amazing cup and ball game!")
print("\033[1;36;40mYou have \033[1;32;40m$50")
print("\033[1;36;40mCorrectly guess which cup the red ball is under and triple your bet!")
print("\033[1;36;40mWhat a Deal!\n\n\n")



#pause before starting game
#time.sleep(2)



def getPlayerBet():
	
	bet=0
	print("\033[1;36;40mYou have \033[1;32;40m${} \033[1;36;40mto bet".format(playerMoney))
	while bet > playerMoney or bet <= 0:
		
		bet = int(input("Place your bet:\033[1;32;40m "))
		
		if bet > playerMoney or bet < 1:
			print("Invalid choice you have \033[1;32;40m${} to bet with".format(playerMoney))
			
	return int(bet)


#Get the players guess
			  
def playerGuess():
	
	guess=''
		
	print("\033[0;37;40m   _____       _____       _____  ")
	print("  /     \     /     \     /     \ ")
	print(" /   1   \   /   2   \   /   3   \ ")
	print("/_________\ /_________\ /_________\ ")
	print("")
		
	while guess not in ['1','2','3']:	
		guess = input('\033[1;36;40mFind the red ball! Pick any of these three cups!!! 1, 2, or 3 ')
		
	return int(guess) -1 #Adding -1 to align with pick since lists start at zero



#Display where the Red Ball was

def display(mixedUpList,guess):
	if mixedUpList[0] == 'RedBall':
		
		print("\033[0;37;40m   _____      ")
		print("\033[0;37;40m  /     \     ")
		print("\033[0;37;40m /   1   \    ")
		print("\033[0;37;40m/_________\    _____       _____ ")
		print("\033[1;31;40m    XXX   \033[0;37;40m    /     \     /     \           ")
		print("\033[1;31;40m   XXXXX  \033[0;37;40m   /   2   \   /   3   \           ")
		print("\033[1;31;40m    XXX   \033[0;37;40m  /_________\ /_________\      \n")
		
		
	elif mixedUpList[1] == 'RedBall':
		
		
		print("\033[0;37;40m               _____     ")
		print("\033[0;37;40m              /     \    ")
		print("\033[0;37;40m             /   2   \    ")
		print("\033[0;37;40m   _____    /_________\    _____     ")  
		print("\033[0;37;40m  /     \ \033[1;31;40m      XXX   \033[0;37;40m    /     \ ")
		print("\033[0;37;40m /   1   \ \033[1;31;40m    XXXXX  \033[0;37;40m   /   3   \          ")
		print("\033[0;37;40m/_________\ \033[1;31;40m    XXX   \033[0;37;40m  /_________\           \n")
		
		
	elif mixedUpList[2] == 'RedBall':
		
		print("\033[0;37;40m                           _____  ")
		print("                          /     \ ")
		print("                         /   3   \ ")
		print("   _____       _____    /_________\ ")
		print("  /     \     /     \     \033[1;31;40m  XXX ")
		print("\033[0;37;40m /   1   \   /   2   \    \033[1;31;40m XXXXX ")
		print("\033[0;37;40m/_________\ /_________\   \033[1;31;40m  XXX \n")
		

		
		
		 



#Compare the guess to the players choice and determine if they've won and adjust their money

def checkGuess(mixedUpList,guess):
	
	#newValue = 0
	
	if mixedUpList[guess] == 'RedBall':
		winnings = bet *3 
		playersMoney = playerMoney + winnings
		
		print("")
		print("\033[1;36;40m Correct! You Just Made \033[1;32;40m${}!".format(winnings))
		print("\033[1;36;40m You now have \033[1;32;40m${}!".format(playersMoney))
		print("")
		newValue = playerMoney	
	else:
		playersMoney = playerMoney- bet
		print("")
		print("\033[1;36;40mWrong Cup! You Lost! You have ${}".format(playersMoney))
		print("")
		


def value(mixedUpList):
	newValue = 0
	
	if mixedUpList[guess] == 'RedBall':
		newValue = bet *3
	else:
		newValue = 0 - bet
	
	return int(newValue)

#Make Sure They Still Have Cash to Play

def cashCheck():
	
	if playerMoney <= 0:
		print("\033[1;36;40mLooks like you're broke, Goodbye")
		time.sleep(1)
		return False
	else:
		return True
	
	
#See if they want to keep playing

def GameOn_choice():
	
	choice = 'wrong'
	
	while choice not in ['Y','N','yes','no','y','n']:
	
		choice = input("\033[1;36;40mdo you want to keep playing (Y or N): ")
		
		if choice not in ['Y','N','y','n','yes','no']:
			print("\033[1;36;40mSorry, that was not a valid choice ")
			
	if choice in  ["Y","y","yes"]:
		return True
	else:
		return False
		
		
		
#Running the program in order

game_on = True
playerMoney = 50


while game_on:
	
	myList = ['empty','empty','RedBall']
	
	shuffle(myList)
	
	bet = getPlayerBet()
	
	guess = playerGuess()
			
	display(myList,guess)
	
	checkGuess(myList,guess)
	
	playerMoney = playerMoney + value(myList)
	
	if playerMoney <= 0:
		print("Looks like you're broke, Goodbye")
		time.sleep(1)
		break 	
	
	game_on = GameOn_choice()
