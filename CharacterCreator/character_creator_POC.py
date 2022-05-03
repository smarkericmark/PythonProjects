#Written in gedit
#tested on Kali 64x Linux Distro using Python 3.9.9


import time
from random import shuffle


class Stats():
	"""docstring for ClassName"""
	
	def __init__(self,Str,Dex,Con,Int,Wis,Cha):
		self.Str = Str
		self.Dex = Dex
		self.Con = Con
		self.Int = Int
		self.Wis = Wis
		self.Cha = Cha

def welcome():
	print("Welcome to the Amazing Character Builder")

def getPlayerName():
	name = input("Please enter your name: ")
	return name



def getCharacterName():
	name = input("Please enter your characters name: ")
	return name

def getBackground():
	choice = 0
	
	while choice not in [1,2,3,4]:
		choice =int(input("Please choose a background (Use the number)\n 1. Human\n 2. Elf\n 3. Dwarf\n 4. Halfing\n"))

		if choice not in [1,2,3,4]:
	 		print("Sorry, that was not a valid choice.")

	if choice == 1:
		return 'Human'

	if choice == 2:
		return 'Elf'

	if choice == 3:
		return 'Dwarf'

	if choice == 4:
		return 'Halfing'



def BackgroundStats(statstoupdate):

	if Background == 'Human':
		return Stats(0,0,0,1,0,1)

	if Background == 'Elf':
		return Stats(0,1,0,0,0,1)

	if Background == 'Dwarf':
		return Stats(1,0,1,0,0,0)

	if Background == 'Halfing':
		return Stats(0,0,0,1,0,1)

def getClass():
	choice = 0
	
	while choice not in [1,2,3,4]:
		choice =int(input("Please choose a class (Use the number)\n 1. Fighter\n 2. Priest\n 3. Mage\n 4. Shadow\n"))

		if choice not in [1,2,3,4]:
	 		print("Sorry, that was not a valid choice.")

	if choice == 1:
		return 'Fighter'

	if choice == 2:
		return 'Priest'

	if choice == 3:
		return 'Mage'

	if choice == 4:
		return 'Shadow'

def getClassAbilities():
	if CharactersClass == 'Fighter':
		return "Gain the Proficiency with all weapons.\nTake 1d4 damage for extra attack each round"

	if CharactersClass == 'Priest':
		return "Channel Divinety Three Times per short and Long rest.\nProfficency with 3 Martial Weapons of Choice1\n Sense Spirits and Perform Exorcisims"


	if CharactersClass == 'Mage':
		return "Gain the Proficiency with all weapons.\nTake 1d4 damage for extra attack each round"
		
	if CharactersClass == 'Shadow':
		return "Channel Divinety Three Times per short and Long rest.\nProfficency with 3 Martial Weapons of Choice"

def getStats(chstats):
	while (chstats.Str + chstats.Dex + chstats.Con + chstats.Int + chstats.Wis + chstats.Cha) < 8:
		print("Your current stats are:\n1.Str {}\n2.Dex {}\n3.Con {}\n4.Int {}\n5.Wis {}\n6.Cha {}".format(chstats.Str,chstats.Dex,chstats.Con,chstats.Int,chstats.Wis,chstats.Cha))
		points = 8 - (chstats.Str + chstats.Dex + chstats.Con + chstats.Int + chstats.Wis + chstats.Cha)
		choice =int(input("You have {} points to spend.\nPlease choose a stat to increase (Use the number)\n".format(points)))		

		if choice not in [1,2,3,4,5,6]:
	 		print("Sorry, that was not a valid choice.")

		if choice == 1:
			chstats.Str +=1

		if choice == 2:
			chstats.Dex +=1

		if choice == 3:
			chstats.Con +=1

		if choice == 4:
			chstats.Int +=1

		if choice == 5:
			chstats.Wis +=1

		if choice == 6:
			chstats.Cha +=1	

	return chstats


def getBuild():
	choice = 'wrong'

	while choice not in ['Y','N','yes','no','y','n']:
	
		choice = input("Do you want to build another character? (Y or N): ")
		
		if choice not in ['Y','N','y','n','yes','no']:
			print("\033[1;36;40mSorry, that was not a valid choice ")
			
	if choice in  ["Y","y","yes"]:
		
		return True
	else:
		return False


#####################
#Running the Program#
#####################

welcome()
build_on = True

while build_on:
	CharactersStats=Stats(0,0,0,0,0,0)
	Playername= "Placeholder"
	Charactername= "Placeholder"
	Background = "Placeholder"
	

	Playername = getPlayerName()
	Charactername = getCharacterName()
	Background = getBackground()
	CharactersStats = BackgroundStats(CharactersStats)
	CharactersClass= getClass()
	ClassAbilities = getClassAbilities()
	CharactersStats= getStats(CharactersStats)
	print(CharactersStats.Str)

	print("==========================================")
	print("\nPlayer Name: {}".format(Playername))
	print("Character Name: {}".format(Charactername))
	print("\nBackground: {}".format(Background))
	print("Class: {}\n".format(CharactersClass))
	print("Str: {} Dex: {} Con: {}".format(CharactersStats.Str,CharactersStats.Dex,CharactersStats.Con))
	print("Int: {} Wis: {} Cha: {}".format(CharactersStats.Int,CharactersStats.Wis,CharactersStats.Cha))
	print("\nClass Abilities:\n {}".format(ClassAbilities))
	print("\n=========================================")

	build_on = getBuild()



