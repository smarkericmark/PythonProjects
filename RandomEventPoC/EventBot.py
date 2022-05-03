import json, glob
import random

def getEventNumber():
    choice = 0
    while choice not in range(1,10):
        choice =int(input("Adolesent Event\n Please select your characters Social Status (Use the number)\n 1. Disenfrancisto\n 2. Criminal\n 3. Lower\n 4. Middle\n 5. Upper\n 6. Ristie\n 7. Loonie\n 8. Android\n 9. Rogue Android\n"))
        
        if choice not in range(1,10):
            print("\nSorry, that was not a valid choice.\n")

    if choice == 1:
        return 'Disenfrancisto'
    
    if choice == 2:
        return 'Criminal'

    if choice == 3:
        return 'Low'
    
    if choice == 4:
        return 'Middle'
    
    if choice == 5:
        return 'Upper'

    if choice == 6:
        return 'Ristie'

    if choice == 7:
        return 'Loonie'
    
    if choice == 8:
        return 'Android'

    if choice == 9:
        return 'RogueAndroid'



def getEvent(numberr):
    with open(f"Aevents/{numberr}Event.txt",encoding='utf-8') as file:
                quotes = file.readlines()
                #print(quotes)
                AdEvent= random.choice(quotes)
                print(AdEvent)

eventNum = getEventNumber()
getEvent(eventNum)