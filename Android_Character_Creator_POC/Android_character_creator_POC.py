#Written in gedit
#tested on Kali 64x Linux Distro using Python 3.9.9


import time
import random
import json, glob


#===========================================
# Classes for Stats and charactacter Info  =
#===========================================

class Stats():
	"""docstring for ClassName"""
	
	def __init__(self,Strength,Agility,Empathy,Intelligence,TradeMarksP,TradeMarksN,Andriod,Clone,BioRoid,Cyberware,GMods,SocialStatus,Faction,CriminalRecord,Jobs,Age):
		self.Strength = Strength
		self.Agility = Agility
		self.Empathy = Empathy
		self.Intelligence = Intelligence
		self.TradeMarksP = TradeMarksP
		self.TradeMarksN = TradeMarksN
		self.Android = Andriod
		self.Clone = Clone
		self.BioRoid = BioRoid
		self.Cyberware = Cyberware
		self.GMods = GMods
		self.SocialStatus = SocialStatus
		self.Faction = Faction 
		self.CriminalRecord = CriminalRecord
		self.Jobs = Jobs
		self.Age = Age 


		

class Skills():
	def __init__(self,CloseCombat,Stamina,HvyMachinery,RangedCombat,Mobility,Piloting,Streetwise,Manipulation,Insight,Observation,MedicalAid,Hacking):

		self.CloseCombat = CloseCombat
		self.Stamina = Stamina
		self.HvyMachinery = HvyMachinery 

		self.RangedCombat = RangedCombat
		self.Mobility = Mobility
		self.Piloting = Piloting

		self.Streetwise = Streetwise
		self.Manipulation = Manipulation
		self.Insight = Insight

		self.Observation = Observation
		self.MedicalAid = MedicalAid
		self.Hacking = Hacking
		

#=============
# Basic Info =
#=============


def welcome():
	print("Welcome to the Amazing Character Builder")

def getPlayerName():
	name = input("Please enter your name: ")
	return name



def getCharacterName():
	name = input("Please enter your characters name: ")
	return name

#=========================================
#  Check for Criminal Record Trademark   =
#=========================================

def criminalCheck(chstats):
	
	for i in chstats.TradeMarksN:
		if (i == 'Criminal Record'):
			chstats.CriminalRecord = True

	return chstats


#============================
# Cyberware / G-Mod Chooser =
#============================

def updateMod(chstats,modType):

	file = open(f"mods/{modType}.txt", "r")
	line_count = 0
	for line in file:
	    if line != "\n":
	        line_count += 1
	file.close()

	#print(line_count)


	with open(f"mods/{modType}.txt",encoding='utf-8') as file:
	    quotes = file.readlines()
	    #print(quotes)
	    count = 0

	    for i in range(0,line_count):
	        count +=1
	        print("{}. {}".format(count,quotes[i]))



	choice = 10000
	mLine_count = line_count +1

	while choice not in range(0,mLine_count):

	    choice =int(input("Please select your Modification (enter number)\n"))
	        


	    if choice not in range(1,mLine_count):
	        print("Sorry, that was not a valid choice.")


	if choice in range(1,mLine_count):
	    choice = choice -1
	    if modType == "cyberware":
	    	chstats.Cyberware.append(quotes[choice].strip('\n'))
	    if modType == "g-mod":
	    	chstats.GMods.append(quotes[choice].strip('\n'))



#===============================
# Update Stats (Player Choice) =
#===============================

def updateStats(chstats):
	choice = 0
	
	while choice not in [1,2,3,4]:

		choice =int(input("Please choose a stat to increase (Use the number):\n 1. Strength\n 2. Agility\n 3. Empathy\n 4. Intelligence\n "))
			
		if choice not in [1,2,3,4]:
	 		print("Sorry, that was not a valid choice.")


	if choice == 1:
		chstats.Strength +=1

	if choice == 2:
		chstats.Agility +=1

	if choice == 3:
		chstats.Empathy +=1

	if choice == 4:
		chstats.Intelligence +=1

	return chstats

#===============================
# Update Stats (Random)        =
#===============================

def updateStatsRandom(chstats):
	

	choice = random.randint(1,4)
	
	if choice == 1:
		chstats.Strength +=1

	if choice == 2:
		chstats.Agility +=1

	if choice == 3:
		chstats.Empathy +=1

	if choice == 4:
		chstats.Intelligence +=1

	return chstats

#===============================
# Update SKill (Player Choice) =
#===============================

def updateSkill(chskills):
	choice = 0
	
	while choice not in range(1,13):

		choice =int(input("Please choose a stat to increase (Use the number):\n 1. Close Combat \n 2. Hvy Machinery\n 3. Stamina\n 4. Ranged Combat\n 5. Mobility\n 6. Piloting\n 7. Streetwise\n 8. Manipulation\n 9. Insight\n 10. Observation\n 11. Medical Aid\n 12. Hacking\n"))
			
		if choice not in range(1,13):
	 		print("Sorry, that was not a valid choice.")


	if choice == 1:
		chskills.CloseCombat +=1

	if choice == 2:
		chskills.HvyMachinery +=1

	if choice == 3:
		chskills.Stamina +=1

	if choice == 4:
		chskills.RangedCombat +=1

	if choice == 5:
		chskills.Mobility +=1

	if choice == 6:
		chskills.Piloting +=1

	if choice == 7:
		chskills.Streetwise +=1

	if choice == 8:
		chskills.Manipulation +=1

	if choice == 9:
		chskills.Insight +=1

	if choice == 10:
		chskills.Observation +=1

	if choice == 11:
		chskills.MedicalAid +=1

	if choice == 12:
		chskills.Hacking +=1

	return chskills



#===============================
#         Clone Choice         =
#===============================


def getCloneChoice(chstats):
	choice = 0
	
	while choice not in [1,2,3,4,5,6]:
		choice =int(input("Please choose a Clone Type (Use the number)\n 1. Desai Tutor Clone\n 2. Henry Labor Clone\n 3. Omoi Security Clone\n 4. Tenma Driver Clone\n 5. Bespoke/Custom Clone\n 6. Rogue Clone\n"))

		if choice not in [1,2,3,4,5,6]:
	 		print("Sorry, that was not a valid choice.")

	if choice == 1:
		chstats.Clone = "Desai"
		chstats.Intelligence +=1
		chstats.Empathy +=1

	if choice == 2:
		chstats.Clone = "Henry"
		chstats.Strength +=1
		chstats.Strength +=1

	if choice == 3:
		chstats.Clone = "Omoi"
		chstats.Agility +=1
		chstats.Strength +=1

	if choice == 4:
		chstats.Clone = "Tenma"
		chstats.Agility +=1
		chstats.Agility +=1

	if choice == 5:
		chstats.Clone = "Bespoke"
		updateStats(chstats)
		updateStats(chstats)


	if choice == 6:
		chstats.Clone = "Rogue"
		chstats.Android = "Rogue"
		updateStats(chstats)
		updateStatsRandom(chstats)
		chstats.TradeMarksN.append("Hunted")


	if choice in range(1,5):
		chstats.TradeMarksP.append("Blend In")
		chstats.TradeMarksN.append("Docile")
		chstats.Faction = "Jinteki"

	return chstats

#===============================
#         BioRoid Choice       =
#===============================


def getBioRoidChoice(chstats):
	choice = 0
	
	while choice not in [1,2,3,4,5,6]:
		choice =int(input("Please choose a Bio-Roid Type (Use the number)\n 1. Adam Industrial Labor BioRoid\n 2. Adonis/Eve Pleasure Model\n 3. Corporate BioRoid\n 4. Rex Search and Rescue BioRoid\n 5. Bespoke/Custom BioRoid\n 6. Rogue BioRoid\n"))

		if choice not in [1,2,3,4,5,6]:
	 		print("Sorry, that was not a valid choice.")

	if choice == 1:
		chstats.BioRoid = "Adam Industrial Labor"
		chstats.Strength += 8
		chstats.Agility += 8

	if choice == 2:
		chstats.BioRoid = "Adonis/Eve Pleasure"
		chstats.Empathy +=8
		chstats.Strength +=8

	if choice == 3:
		chstats.BioRoid = "Corporate"
		chstats.Empathy +=8
		chstats.Intelligence +=8

	if choice == 4:
		chstats.BioRoid = "Rex Search and Rescue"
		chstats.Strength +=8
		chstats.Intelligence +=8

	if choice == 5:
		chstats.BioRoid = "Bespoke"
		updateStats(chstats)
		updateStats(chstats)


	if choice == 6:
		chstats.BioRoid = "Rogue"
		chstats.Android = "Rogue"
		updateStats(chstats)
		updateStatsRandom(chstats)
		chstats.TradeMarksN.append("Hunted")
		chstats.TradeMarksN.append("No Access to Updates")


	if choice in range(1,5):
		chstats.TradeMarksN.append("Guided by the Three Laws")
		chstats.Faction = "Haas-BioRoid"


	
		
	chstats.TradeMarksP.append("No Food,Sleep,Air,or Water required")

	return chstats



#===============================
#       Background Choice      =
#===============================


def getBackground():
	choice = 0
	
	while choice not in [1,2,3,4,5,6]:
		choice =int(input("Please choose a background (Use the number)\n 1. Human\n 2. Loonie\n 3. G-Mod\n 4. Clone\n 5. Bio-Roid\n 6. Cyborg\n"))

		if choice not in [1,2,3,4,5,6]:
	 		print("Sorry, that was not a valid choice.")

	if choice == 1:
		return 'Human'

	if choice == 2:
		return 'Loonie'

	if choice == 3:
		return 'G-Mod'

	if choice == 4:
		return 'Clone'

	if choice == 5:
		return 'Bio-Roid'

	if choice == 6:
		return 'Cyborg'

def setStats(statstoupdate):
	return Stats(0,0,0,0)


def BackgroundStats(statstoupdate):

	if Background == 'Human':
		updateStatsRandom(statstoupdate)
		updateStatsRandom(statstoupdate)
		

	if Background == 'Loonie':
		statstoupdate.Agility +=1
		updateStats(statstoupdate)
		statstoupdate.TradeMarksP.append("Tall and Spindliy")
		statstoupdate.TradeMarksN.append("Usual Suspect")

	if Background == 'G-Mod':
		updateStats(statstoupdate)
		updateStats(statstoupdate)
		updateMod(statstoupdate,"g-mod") 


	if Background == 'Clone':
		getCloneChoice(statstoupdate)

	if Background == 'Cyborg':
		updateStatsRandom(statstoupdate)
		updateStats(statstoupdate)
		updateMod(statstoupdate,"cyberware")
		updateMod(statstoupdate,"cyberware")
		updateMod(statstoupdate,"cyberware")
		statstoupdate.TradeMarksN.append("Obvious Cyberware")

	if Background == 'Bio-Roid':
		getBioRoidChoice(statstoupdate)


	return statstoupdate

#================
#  Get Faction  =
#================

def getFaction(chstats):

	choice = 0
	
	if (chstats.CriminalRecord == True) or (chstats.Android == "Rogue"):
		while choice not in range(7,11):
			choice =int(input(" 1. Unavailible\n 2. Unavailible\n 3.Unavailible\n 4. Unavailible\n 5. Unavailible\n 6. Unavailible\n 7. OrgCrime\n 8. Loonies\n 9. Street Gangs\n 10. Activist/Terrorist Group\n"))

			if choice not in range(1,11):
	 			print("Sorry, that was not a valid choice.")


	else:

		while choice not in range(1,11):
			choice =int(input(" 1. Haas-BioRoid\n 2. Jinteki\n 3. Weyland Consortium\n 4. NBN\n 5. Globalsec\n 6. NAPD\n 7. OrgCrime\n 8. Loonies\n 9. Street Gangs\n 10. Activist/Terrorist Group\n"))

			if choice not in range(1,11):
	 			print("Sorry, that was not a valid choice.")


	if choice == 1:
		chstats.Faction = "Haas-BioRoid"
	if choice == 2:
		chstats.Faction ="Jinteki"
	if choice == 3:
		chstats.Faction ="Weyland Consortium"
	if choice == 4:
		chstats.Faction ="NBN"
	if choice == 5:
		chstats.Faction ="Globalsec"
	if choice == 6:
		chstats.Faction ="NAPD"
	if choice == 7:
		chstats.Faction ="OrgCrime"
	if choice == 8:
		chstats.Faction ="Loonies"
	if choice == 9:
		chstats.Faction ="Street Gangs"
	if choice == 10:
		chstats.Faction ="Activist/Terrorist Group"

	return chstats



#============================
#  Starting Faction Choice  =
#============================

def getFirstFaction(chstats,chskills):
	
	if chstats.Android == "Rogue":
		print("Who is helping you evade capture")
	else:
		print("Which MegaCorp or Group had the Biggest Impact on you growing up?")

	getFaction(chstats)

	# Corps

	if chstats.Faction == "Haas-BioRoid":
		chstats.TradeMarksP.append("Accounting")
		chskills.Observation += 1

	if chstats.Faction == "Jinteki":
		chstats.TradeMarksP.append("Biology Expert")
		chskills.MedicalAid += 1

	if chstats.Faction == "Weyland Consortium":
		chstats.TradeMarksP.append("Business Savvy")
		chskills.Manipulation += 1

	if chstats.Faction == "NBN":
		chstats.TradeMarksP.append("Lifesytle Expert")
		chskills.Insight += 1

	#The Rest

	if chstats.Faction == "Globalsec":
		chstats.TradeMarksP.append("Gamble")
		chskills.RangedCombat += 1

	if chstats.Faction == "NAPD":
		chstats.TradeMarksP.append("Quick Witted")
		chskills.Streetwise += 1

	if chstats.Faction == "OrgCrime":
		if chstats.Android != "Rogue":
			chstats.TradeMarksP.append("I Know a Guy")
			chskills.CloseCombat += 1

	if chstats.Faction == "Loonies":
		if chstats.Android != "Rogue":
			chstats.TradeMarksP.append("Tunnel Navigator")
			chskills.Hacking += 1

	if chstats.Faction == "Street Gangs":
		if chstats.Android != "Rogue":
			chstats.TradeMarksP.append("Thievery")
			chskills.Mobility += 1

	if chstats.Faction == "Activist/Terrorist Group":
		if chstats.Android != "Rogue":
			chstats.TradeMarksP.append("Explosive Expert")
			chskills.Stamina += 1


	return chstats,chskills


#==============================
#    Starting Social Status   =
#==============================

def getStartingSocialStatus(chstats, Background):
	
	choice = 0

	if Background == "Human":

		while choice not in range(1,7):
			choice =int(input("What was your social status growing up?(Use the number)\n 1. Disenfrancisto\n 2. Criminal\n 3. Lower Class\n 4. Middle Class\n 5. Upper Class\n 6. Ristie\n"))

			if choice not in range(1,7):
	 			print("Sorry, that was not a valid choice.")

	if Background == "Loonie":

		while choice not in range(2,6):
			choice =int(input("What was your social status growing up (Use the number)\n 1. Unavailible\n 2. Criminal\n 3. Lower Class\n 4. Middle Class\n 5. Upper Class\n 6. Unavailible\n"))

			if choice not in range(2,6):
	 			print("Sorry, that was not a valid choice.")

	if Background == "G-Mod":

		while choice not in [2,4,5,6]:
			choice =int(input("What was your social status growing up (Use the number)\n 1. Unavailible\n 2. Criminal\n 3. Unavailible\n 4. Middle Class\n 5. Upper Class\n 6. Ristie\n"))

			if choice not in [2,4,5,6]:
	 			print("Sorry, that was not a valid choice.")

	if Background == "Cyborg":

		while choice not in range(1,4):
			choice =int(input("What was your social status growing up (Use the number)\n 1. Disenfrancisto\n 2. Criminal\n 3. Lower Class\n 4. Unavailible\n 5. Unavailible\n 6. Unavailible\n"))

			if choice not in range(1,4):
	 			print("Sorry, that was not a valid choice.")



	if choice == 1:
		chstats.SocialStatus = "Disenfrancisto"
		chstats.Strength += 1
		chstats.TradeMarksP.append("Off-The Grid")

	if choice == 2:
		chstats.SocialStatus = "Criminal"
		chstats.Strength += 1
		chstats.TradeMarksP.append("Intimidating")
		chstats.CriminalRecord = True

	if choice == 3:
		chstats.SocialStatus = "Lower Class"
		chstats.Empathy += 1
		chstats.TradeMarksP.append("Ignored")

	if choice == 4:
		chstats.SocialStatus = "Middle Class"
		chstats.Agility += 1
		chstats.TradeMarksP.append("Style Expert")

	if choice == 5:
		chstats.SocialStatus = "Upper Class"
		chstats.Empathy += 1
		chstats.TradeMarksP.append("Finance Expert")

	if choice == 6:
		chstats.SocialStatus = "Ristie"
		chstats.Intelligence += 1
		chstats.TradeMarksP.append("Well-Connected")

	return chstats

#=====================
#  Home Environment  =
#=====================

def getHomeEnvironment (chstats,chskills):
	choice = 0

	if (chstats.SocialStatus == "Disenfrancisto") or (chstats.SocialStatus == "Criminal") or (chstats.SocialStatus == "Lower Class") or (chstats.SocialStatus == "Middle Class"):

		while choice not in range(1,5):
			choice =int(input("What was your home environment like growing up?(Use the number)\n 1. Violent\n 2. Difficult\n 3. Rebellious\n 4. Happy Home\n 5. Unavailible\n 6. Unavailible\n"))

			if choice not in range(1,5):
	 			print("Sorry, that was not a valid choice.")

	if (chstats.SocialStatus == "Upper Class") or (chstats.SocialStatus == "Ristie"):

		while choice not in range(1,7):
			choice =int(input("What was your home environment like growing up?(Use the number)\n 1. Violent\n 2. Difficult\n 3. Rebellious\n 4. Happy Home\n 5. Academic\n 6. High Society\n"))

			if choice not in range(1,7):
	 			print("Sorry, that was not a valid choice.")


	if choice == 1:
		chskills.CloseCombat += 1

	if choice == 2:
		chskills.Stamina += 1

	if choice == 3:
		chskills.Piloting += 1

	if choice == 4:
		chskills.Mobility += 1

	if choice == 5:
		chskills.Insight += 1

	if choice == 6:
		chskills.Manipulation += 1

	return chskills

#==============
#  Education  =
#==============

def getEducation(chstats,chskills,Background):

	choice = 0

	if Background == "Loonie":
		chstats.Intelligence +=1
		chstats.TradeMarksN.append("Blunt")
		chskills.Hacking +=1

	else:

		if (chstats.SocialStatus == "Disenfrancisto") or (chstats.SocialStatus == "Criminal"):

			while choice not in range(1,4):
				choice =int(input("What kind of education did you recieve?(Use the number)\n 1. Grew Up on the Streets\n 2. Technical Education\n 3. Military Training\n 4. Unavailible\n 5. Unavailible\n 6. Unavailible\n"))

				if choice not in range(1,4):
	 				print("Sorry, that was not a valid choice.")

		if (chstats.SocialStatus == "Lower Class") or (chstats.SocialStatus == "Middle Class"):
			while choice not in range(2,5):
	 			choice =int(input("What kind of education did you recieve?(Use the number)\n 1. Unavailible\n 2. Technical Education\n 3. Military Training\n 4. Basic Education\n 5. Unavailible\n 6. Unavailible\n"))

	 			if choice not in range(2,5):
	 				print("Sorry, that was not a valid choice.")

		if (chstats.SocialStatus == "Upper Class") or (chstats.SocialStatus == "Ristie"):
			while choice not in range(4,7):
				choice =int(input("What kind of education did you recieve?(Use the number)\n 1. Unavailible\n 2. Technical Education\n 3. Military Training\n 4. Basic Education\n 5. Private School Education\n 6. Scientific Education\n"))

				if choice not in range(4,7):
	 				print("Sorry, that was not a valid choice.")

		if choice == 1:
			chstats.Agility +=1
			chstats.TradeMarksN.append("Mean Streak")
			chskills.Mobility +=1

		if choice == 2:
			chstats.Strength +=1
			chstats.TradeMarksN.append("Always Dirty")
			chskills.HvyMachinery +=1

		if choice == 3:
			chstats.Agility +=1
			chstats.TradeMarksN.append("Overconfident")
			chskills.RangedCombat +=1

		if choice == 4:
			chstats.Strength +=1
			chstats.TradeMarksN.append("Close Minded")
			chskills.Stamina += 1

		if choice == 5:
			chstats.Empathy +=1
			chstats.TradeMarksN.append("Elitist")
			chskills.Manipulation += 1			

		if choice == 6:
			chstats.Intelligence +=1
			chstats.TradeMarksN.append("Awkward")
			chskills.Observation += 1


	return chskills, chstats


#===========================
#   Criminal Record Choice =
#===========================

def getCriminalChoice(chstats):
	choice=''

	while choice not in ['Yes','YES','yes','y','Y','No','NO','no','n','N']:
		choice =input("Warning! You are about to fall off the bottom rung of society and become a Disenfrancisto. You can choose to continue and lose everything or resort to becoming a criminal.\nUpward mobility is very difficult once you become a Disenfrancisto, but resorting to crime will result in a Criminal Record if you don't already have one, and prevent certain career opportunities and make you known to authorities.\n Do you resort to a life of crime to prevent this fate? (Yes or No)\n")

	if choice in ['Yes','YES','yes','y','Y']:
		chstats.SocialStatus = 'Criminal'
		chstats.TradeMarksN.append("Criminal Record")
		chstats.CriminalRecord = True

	if choice in ['No','NO','no','n','N']:
		chstats.SocialStatus = 'Disenfrancisto'

	return chstats


#===========================
#  Social Status Up / Down =
#===========================

def socialStatusChangeUp(chstats):
	
	if chstats.SocialStatus == 'Upper Class':
		chstats.SocialStatus = 'Ristie'

	if chstats.SocialStatus == 'Middle Class':
		chstats.SocialStatus = 'Upper Class'


	if chstats.SocialStatus == 'Lower Class':
		chstats.SocialStatus = 'Middle Class'

	if chstats.SocialStatus == 'Disenfrancisto':
		chstats.SocialStatus = 'Lower Class'

	if chstats.SocialStatus == 'Criminal':
		chstats.SocialStatus = 'Middle'
	
	return chstats


def socialStatusChangeDown(chstats):
	#Consider adding a choice to take a criminal record
	
	if chstats.SocialStatus == 'Criminal':
		chstats.SocialStatus = 'Disenfrancisto'

	if chstats.SocialStatus == 'Lower Class':
		getCriminalChoice(chstats)

	if chstats.SocialStatus == 'Middle Class':
		chstats.SocialStatus = 'Lower Class'

	if chstats.SocialStatus == 'Upper Class':
		chstats.SocialStatus = 'Middle Class'

	if chstats.SocialStatus == 'Ristie':
		chstats.SocialStatus = 'Upper Class'

	

	return chstats



##==================#	
#  Get Event        #
##==================#

def getEvent(chstats,switch):

	Holder = ''
	P = "Trademark(+)"
	N = "Trademark(-)"
	fire = "are fired"
	newGmod = "Gain a G-Mod"
	newCyber= "Gain a new piece of cyberware"

	Increase = 'Increase your social status by 1'
	Decrease = 'Decrease your social status by 1'
	Increase2 = 'Increase your social status by 2'
	Decrease2 = 'Decrease your social status by 2'

	if switch == "Aevents":
		Holder = chstats.SocialStatus
	
	if switch =="Cevents":
		Holder = "MasterList"


	with open(f"{switch}/{Holder}.txt",encoding='utf-8') as file:
		quotes = file.readlines()
		#print(quotes)
		event= random.choice(quotes)
		print("\nMajor Adolescent Event\n")
		print(event)
		input("\nPress Enter to Continue\n")


		if P in event:
			TMP=event.split(':')
			chstats.TradeMarksP.append(TMP[1].strip('\n'))

		if N in event:
			TMN=event.split(':')
			chstats.TradeMarksN.append(TMN[1].strip('\n'))


		#==================================#
		# Check for social status change   #
		#==================================#

		if Increase in event:
			socialStatusChangeUp(chstats)

		if Decrease in event:
			socialStatusChangeDown(chstats)

		if Increase2 in event:
			socialStatusChangeUp(chstats)
			socialStatusChangeUp(chstats)

		if Decrease2 in event:
			socialStatusChangeDown(chstats)
			socialStatusChangeDown(chstats)

		#=====================================
		# Check for new Cyberware and G-mods =
		#=====================================

		if newGmod in event:
			updateMod(chstats,"g-mod")

		if newCyber in event:
			updateMod(chstats,"cyberware")

		#======================================
		#  Check to see if Character is fired =
		#======================================

		if fire in event:
			socialStatusChangeDown(chstats)

		#=============================
		#  Check for Criminal Record #
		#=============================
		criminalCheck(chstats)


#===============================#
#    Age & Career Trademark(+)  #
#===============================#

def AgeTrade(chstats,Discipline,Job):
	die=[1,2,3,4,5,6]
	shuffle(die)
	chstats.Age += die[0]

	print("You spend {} years working as {}.\n Choose a Trademark(+) that you feel best represents your time in this role\n".formt(die[0],job))


#==================
#  Career Choice  = 
#==================

def getCareerChoice(chstats,Discipline):
	a_file= open(f"jobs/{chstats.SocialStatus}.txt",encoding='utf-8')
	startCount=1
	endCount=0
	jobList=[]
	CriminalStatus = ''
	if chstats.CriminalRecord == True:
		CriminalStatus = 'Criminal'
    
	for number, line in enumerate(a_file):
		if "{}{}Start".format(Discipline,CriminalStatus) in line:
			break
		else:
			startCount +=1


	for number, line in enumerate(a_file):
		if "{}{}End".format(Discipline,CriminalStatus) in line:
			break
		else:
			endCount +=1

	a_file.close()
    
    
	finalCount = startCount + endCount

	with open(f"jobs/{chstats.SocialStatus}.txt",encoding='utf-8') as file:
		quotes = file.readlines()
		for line in quotes[startCount:finalCount]:
			jobList.append(line.strip('\n'))

	choice = 10000
	endRange = len(jobList)+1
	count=-1
	jobCount=0
	Job =''

	for i in jobList:
		count +=1
		jobCount += 1
		print("{}. {}".format(jobCount,jobList[count]))
            
	while choice not in range(1,endRange):
		choice =int(input("Please select your job (enter number)\n"))
			
		if choice not in range(1,endRange):
			print("Sorry, that was not a valid choice.")

	if choice in range(1,endRange):
		choice = choice -1
		Job = jobList[choice]
		chstats.Jobs.append(Job)

	AgeTrade(chstats,Discipline,Job)




#==================#
#  Displine Choice #
#==================#

def getDisciplineChoice(chstats,chskills):
	choice = 0
	Discipline = ''

	if chstats.CriminalRecord == True:
		while choice not in range(1,9):
			choice =int(input("Please choose your Career Discipline\n 1. Way of the Listless Wanderer\n 2. Way of the Gun\n 3. Way of the Wheel\n 4. Way of the Wrench\n 5. Way of the Net\n 6. Way of the Leader\n 7. Way of the Healer\n 8. Way of the Enforcer\n 9. Way of the Monolith\n"))

			if choice in range(9,10):
				print("\nCriminal Record Dectected!!! Application Rejected. Please choose again\n")


	elif (chstats.SocialStatus == 'Disenfrancisto') or (chstats.SocialStatus == 'Lower Class') or (chstats.SocialStatus == 'Middle Class'): 
		while choice not in range(1,9):
			choice =int(input("Please choose your Career Discipline\n 1. Way of the Listless Wanderer\n 2. Way of the Gun\n 3. Way of the Wheel\n 4. Way of the Wrench\n 5. Way of the Net\n 6. Way of the Leader\n 7. Way of the Healer\n 8. Way of the Enforcer\n 9. Way of the Monolith\n"))

			if choice in range(9,10):
				print("\nEw, Poor Person Dectected!!! Application Rejected. Please kindly choose again\n")


	else:
		while choice not in range(1,10):
			choice =int(input("Please choose your Career Discipline\n 1. Way of the Listless Wanderer\n 2. Way of the Gun\n 3. Way of the Wheel\n 4. Way of the Wrench\n 5. Way of the Net\n 6. Way of the Leader\n 7. Way of the Healer\n 8. Way of the Enforcer\n 9. Way of the Monolith\n"))


			if choice not in range(1,10):
	 			print("\nSorry, that was not a valid choice.\n")


	if choice == 1:
		print("you work a series unskilled labour and temp jobs between boughts of unemployement\n")
		Discipline = "Unemployed"
		updateStats(chstats)
		updateSkill(chskills)
			
	if choice == 2:
		chstats.Agility += 1
		chskills.RangedCombat +=1
		Discipline = "Soldier"

	if choice == 3:
		chstats.Agility += 1
		chskills.Piloting +=1
		Discipline = "Pilot"
			
	if choice == 4:
		chstats.Strength += 1
		chskills.HvyMachinery +=1
		Discipline = "Roughneck"

	if choice == 5:
		chstats.Intelligence += 1
		chskills.Hacking +=1
		Discipline = "NetRunner"
			
	if choice == 6:
		chstats.Empathy += 1
		chskills.Manipulation +=1
		Discipline = "Leader"
			
	if choice == 7:
		chstats.Intelligence += 1
		chskills.MedicalAid +=1
		Discipline = "Medical"

	if choice == 8:
		chstats.Strength += 1
		chskills.Streetwise +=1
		Discipline = "Law"
			
	if choice == 9:
		chstats.Empathy += 1
		chskills.Insight +=1
		Discipline = "Company"

	getCareerChoice(chstats,Discipline)

	return chstats,chskills
			





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
	CharactersStats=Stats(0,0,0,0,[],[],False,"no","no",[],[],"none","none",False,[],18)
	CharactersSkills=Skills(0,0,0,0,0,0,0,0,0,0,0,0)

	#TradeMarksP =[]
	#TradeMarksN =["Test","OtherTest"]
	Playername= "Placeholder"
	Charactername= "Placeholder"
	Background = "Placeholder"
	

	Playername = getPlayerName()
	Charactername = getCharacterName()
	Background = getBackground()
	CharactersStats = BackgroundStats(CharactersStats)
	if CharactersStats.Faction == 'none':
		getFirstFaction(CharactersStats,CharactersSkills)
	getStartingSocialStatus(CharactersStats,Background)
	getHomeEnvironment(CharactersStats,CharactersSkills)
	getEducation(CharactersStats,CharactersSkills,Background)
	getEvent(CharactersStats,"Aevents")
	getDisciplineChoice(CharactersStats,CharactersSkills)
	getEvent(CharactersStats,"Cevents")
	getDisciplineChoice(CharactersStats,CharactersSkills)
	getEvent(CharactersStats,"Cevents")
	getDisciplineChoice(CharactersStats,CharactersSkills)
	getEvent(CharactersStats,"Cevents")
	#CharactersClass= getClass()
	#ClassAbilities = getClassAbilities()
	#CharactersStats= getStats(CharactersStats)
	#print(CharactersStats.Str)

	print("==========================================")
	print("\nPlayer Name: {}".format(Playername))
	print("Character Name: {}".format(Charactername))
	print("\nBackground: {}".format(Background))
	
	print("Strength: {}".format(CharactersStats.Strength))
	print("  Close Combat: {}  Stamina: {} Hvy Machinery: {}".format(CharactersSkills.CloseCombat,CharactersSkills.Stamina,CharactersSkills.HvyMachinery))
	
	print("Agility: {}".format(CharactersStats.Agility))
	print("  Rng.Combat: {} Mobility: {} Piloting: {}  ".format(CharactersSkills.RangedCombat,CharactersSkills.Mobility,CharactersSkills.Piloting))
	
	print("Empathy: {}".format(CharactersStats.Empathy))
	print("  Streetwise: {} Manipulation: {} Insight: {}  ".format(CharactersSkills.Streetwise,CharactersSkills.Manipulation,CharactersSkills.Insight))
	
	print("Intelligence: {}".format(CharactersStats.Intelligence))
	print("  Observation: {} Medical Aid: {} Hacking: {}  ".format(CharactersSkills.Observation,CharactersSkills.MedicalAid,CharactersSkills.Hacking))

	print("\n Career01: {} \n Career02: {} \n Career03: {} \n ".format(CharactersStats.Jobs[0],CharactersStats.Jobs[1],CharactersStats.Jobs[2]))
	print("\nTrademarks(+):{}".format(CharactersStats.TradeMarksP))
	print("Trademarks(-):{}".format(CharactersStats.TradeMarksN))
	if CharactersStats.Clone != "no":
		print("Clone Type: {}".format(CharactersStats.Clone))
	if CharactersStats.BioRoid != "no":
		print("BioRoid Model: {}".format(CharactersStats.BioRoid))
	if CharactersStats.Cyberware != []:
		print("Cyberware:{}".format(CharactersStats.Cyberware))
	#print("Most Connected Faction: {}".format(CharactersStats.Faction))
	print("Current Social Status: {}".format(CharactersStats.SocialStatus))
	print("\n=========================================")

	build_on = getBuild()



