#5/20/2022

#This program randomly guesses a user-given word and counts the attempts made
#Made by Account95555

import random
#this list took up 1/5 of the programming time
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
playagain = True

print("Python code tries to guess the word\n")

while playagain == True:
    word = ""
    attempts = 0
    guess = ""
    valid = False
    auto = ""
    length = 0
    letter = ""
    while valid != True:
        word = input("Please enter a word for the code to guess: ")
        if word.isalpha() == False:
            print("Please enter a word only spelled with the English alphabet.")
        else:
            valid = True
            word = word.lower()
            length = len(word)

    auto = input("Do you want the guesser to run automatically? Enter y if yes (Suggested): ")

    if auto.lower() == "y":
        while guess != word:
            attempts += 1
            guess = ""
            for i in range(length):
                letter = alphabet[random.randint(0,25)]
                guess += letter
            print(guess)
    else:
        while guess != word:
            attempts += 1
            print("Attempt",attempts)
            cont = input("Press enter to continue")
            guess = ""
            for i in range(length):
                letter = alphabet[random.randint(0,25)]
                guess += letter
            print(guess)        

    print("The word:",word + ",was guessed")
    print("It only took",attempts,"attempt(s)!")

    confirm = input("Do you want to do this again? Enter y if yes: ")

    if confirm.lower() == "y":
        playagain = True
        valid = False
    else:
        playagain = False
        print("\nThanks for running this program")






    

        


    



