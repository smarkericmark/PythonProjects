#Written in gedit
#tested on Kali 64x Linux Distro using Python 3.9.9

#Version 1.2 changes
#Added asci art and cleaned up the selection process

import time
from random import shuffle

#Create and randomize list

myList = ['empty','empty','RedBall']
shuffle(myList)


#Get the players guess

def playerGuess():
	
	guess=''
		
	print("   _____       _____       _____  ")
	print("  /     \     /     \     /     \ ")
	print(" /   1   \   /   2   \   /   3   \ ")
	print("/_________\ /_________\ /_________\ ")
	print("")
		
	while guess not in ['1','2','3']:	
		guess = input('Find the red ball! Pick any of these three cups!!! 1, 2, or 3 ')
		
	return int(guess) -1 #Adding -1 to align with pick since lists start at zero

guess = playerGuess()

#Compare the guess to the players choice and determine if they've won

def checkGuess(mixedUpList,guess):
	if mixedUpList[guess] == 'RedBall':
		print("")
		print("Correct!")
		print("")
	else:
		print("")
		print("Wrong Cup!")
		print("")
		#print(myList)
	
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
		
		print("                           _____  ")
		print("                          /     \ ")
		print("                         /   3   \ ")
		print("   _____       _____    /_________\ ")
		print("  /     \     /     \     \033[1;31;40m  XXX ")
		print("\033[0;37;40m /   1   \   /   2   \    \033[1;31;40m XXXXX ")
		print("\033[0;37;40m/_________\ /_________\   \033[1;31;40m  XXX \n")
		

checkGuess(myList, guess)	
