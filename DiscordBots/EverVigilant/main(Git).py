'''
Python 3.9.9
Coded on Kali Linux using gedit
Tested and confirmed to work on discord!
'''
import discord
import os
import random

client = discord.Client()




@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	

	if message.author == client.user:
		return


### This message is to test to make sure the bot is working

	if message.content.startswith('$hello'):
		await message.channel.send('Hello!')

		
	if message.content.startswith('$roll'):
	
		fresult= 'blank'
	
		await message.channel.send("How Many Dice do you need to Roll?")
		roll = await client.wait_for("message", check=None) 
		
		iroll = int(float(roll.content))
		sroll = str(roll.content)
		
		await message.channel.send("What is the target range for success?: ")
		Target = await client.wait_for("message", check=None) 
		
		itarget = int(float(Target.content))
		starget = str(Target.content)
		

		###If the Players target is less then five we need to determine if 
		###a Fatigue check is required
		
		if itarget <= 4:
			scheck=''
		
			while scheck not in ['Yes','YES','yes','y','Y','No','NO','no','n','N']:

				await message.channel.send("Will you require a fatigue check?")
				check = await client.wait_for("message", check=None) 

				scheck = str(check.content)
			
			if scheck in ['Yes','YES','yes','y','Y']:
				ifatigue = -1
				iphysique = 0 
				fsucesses = 0
			
			
				### If the Characters physique score is greater then the characters current
				### Fatique no roll is required. If it is equal to or greater then the player
				### Will need to complete a fatiuge check.
			
			
				while ifatigue not in range(0,31):	
					
					await message.channel.send("How Much Fatigue Do You Currently Have?")
					fatigue = await client.wait_for("message", check=None) 
					ifatigue = int(float(fatigue.content))
				
				while iphysique not in range (1,9):
					
					await message.channel.send("What is your Physique score?")
					physique = await client.wait_for("message", check=None) 
					iphysique = int(float(physique.content))
		
				if iphysique > ifatigue:
					#print('No Fatigue Roll Required!')
					await message.channel.send("No Fatigue Roll Required!")
		
				elif iphysique <= ifatigue:    
					fdie = [1,2,3,4,5,6]
					fDieResults = []
					
				###Fatigue checks only succeed on a 5 or 6
				
					for n in range(ifatigue):
						random.shuffle(fdie)
						fDieResults.append(fdie[0])
						if fdie[0] >= 5:
							fsucesses += 1
					
				
					if fsucesses > iphysique:
						fresult = 'You Are Exhausted'
						
					else:
						fresult = 'You Are Fine'

				
		###End of Fatigue Check
		### Regular roll resumes
			
				
		
		die = [1,2,3,4,5,6]
		DieResults = []
		sucesses = 0
		
		for n in range(iroll):
			random.shuffle(die)
			DieResults.append(die[0])
			if die[0] >= itarget:
				sucesses += 1
		
		### End of Regular ROll
	
		### Final Output		
		
		await message.channel.send("Roll Results")
		await message.channel.send('Successes: {}'.format(sucesses))	
		await message.channel.send(DieResults)
		
		### Only show fatigue roll information if a fatigue roll was made
		
		if fresult != 'blank':
			await message.channel.send("===============")
			await message.channel.send("Fatigue Check")
			await message.channel.send('Successes: {}'.format(fsucesses))
			await message.channel.send(fDieResults)
			await message.channel.send(fresult)

client.run('REDACTED')
