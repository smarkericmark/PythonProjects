"""
Ever Vigielent Dice Roller
Version 1.0
"""

import discord
import time
import os
from random import shuffle

def getNumberofDice():
	
	NumberofDice = 0
	
	while NumberofDice not in range(1,31):
		NumberofDice = int(input('How Many Dice Are You Rolling?: '))
	
	return int(NumberofDice)

#getNumberofDice()
	
def getTarget():
	Target = 0
	
	while Target not in range(1,31):
		Target = int(input('What is the target range for success?: '))
	
	return int(Target) 

#getTarget()

def fatigue(Target):
	if Target <= 4:
		check=''
		
		while check not in ['Yes','YES','yes','y','Y','No','NO','no','n','N']:

			check = input("Will you require a fatigue check?")
			
		if check in ['Yes','YES','yes','y','Y']:
			return True
			
		else:
			return False 
			
	else:
		return False

def diceRoll(num1,num2=5):
	
	die = [1,2,3,4,5,6]
	DieResults = []
	sucesses = 0
	
	for n in range(num1):
		shuffle(die)
		DieResults.append(die[0])
		if die[0] >= num2:
			sucesses += 1
	print("Successes: {}".format(sucesses))	
	print(DieResults)

#diceRoll(3)

def fatigueRoll():
	
	fatigue = -1
	physique = 0 
	sucesses = 0
	
	while fatigue not in range(0,31):	
		fatigue = int(input('How Much Fatigue Do You Currently Have?: '))
				
	while physique not in range (1,9):
		physique = int(input('What is your Physique score?: '))
		
	if physique > fatigue:
		print('No Fatigue Roll Required!')
		
	elif physique <= fatigue:    
		die = [1,2,3,4,5,6]
		DieResults = []
		
		for n in range(fatigue):
			shuffle(die)
			DieResults.append(die[0])
			if die[0] >= 5:
				sucesses += 1
	
		print("Successes: {}".format(sucesses))	
		print(DieResults)
		if sucesses > physique:
			print('You Are Exhausted')
		else:
			print('You Are Fine')
			
#fatigueRoll()	
#print(len(range(0,5)))	

#'''
#####################
#Running the Program#
#####################

fatigue_Check = False

dice_rolled = getNumberofDice()

target = getTarget()

fatigue_Check = fatigue(target)

diceRoll(dice_rolled,target)

if fatigue_Check == True:
	fatigueRoll()
	
#'''


