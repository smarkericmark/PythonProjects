#Written in gedit
#tested on Kali 64x Linux Distro using Python 3.9.9

from random import shuffle

#Create and randomize list

myList = ['empty','empty','RedBall']
shuffle(myList)


#Get the players guess

def playerGuess():
	
	guess=''
	
	while guess not in ['1','2','3']:	
		guess = input('Find the red ball! Pick any of these three cups!!! 1, 2, or 3 ')
		
	return int(guess) -1 #Adding -1 to align with pick since lists start at zero

guess = playerGuess()

#Compare the guess to the players choice and determine if they've won

def checkGuess(mixedUpList,guess):
	if mixedUpList[guess] == 'RedBall':
		print("Correct!")
	else:
		print("Wrong Cup!")
		print(myList) 

checkGuess(myList, guess)	
