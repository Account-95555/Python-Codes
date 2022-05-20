print("Rat CHef")
day = 1
lose = 0
#Ratchef alpha v1
#Basic framework, more of a random clicker than a game

print("Ratchef, search for rats everyday and dont run out of money")
print("Controls - Enter")

money = 500
import random

while money > 0:
    print ("day",day)
    actions = random.randint(0,20)
    rat = 0
    income = 0
    if actions == 0:
        print("Today was a bad day, you weren't able to search for rats...")
    while actions > 0:
        action = input("Find rat?")
        if random.randint(0,1) == 1:
            print("Rat found")
            rat += 1
            actions -=1
        else:
            print("No rats found")
            actions -=1
    income = rat * 10
    money += income
    print("you earned",income,"$")
    print("rent of 50 minused off")
    money -= 50
    print("remaining money",money)
    day +=1
print("you survived for",day,"days")
                
            
    
    
