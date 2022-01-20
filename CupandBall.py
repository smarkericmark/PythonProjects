from random import shuffle

myList = ['empty','empty','RedBall']
shuffle(myList)

#print(myList)


def playerGuess():
	
	guess=''
	
	while guess not in ['1','2','3']:	
		guess = input('Find the red ball! Pick any of these three cups!!! 1, 2, or 3 ')
		
	return int(guess)


guess = playerGuess()

def checkGuess(mixedUpList,guess):
	if mixedUpList[guess] == 'RedBall':
		print("Correct!")
	else:
		print("Wrong Cup!")
		print(myList) 

checkGuess(myList, guess-1)	
