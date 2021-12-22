# Jonathan Wong, jzwong@usc.edu
# ITP 115, Fall 2021
# Section: 31856
# Assignment 6
# Description: Write a program that displays a jumbled word to the user. Have the user guess the
# word and continue guessing until they get it correct. The user will have a choice to
# display a hint. After the user correctly enters the word, display the number of guesses it
# took for them to enter the correct word.

import random

def main():
    words= ["basketball","california","python","traveler"] #Create list of words and hints
    hints= ["Sport with hoop","State where USC resides.","Type of snake and programming language","USC Mascot"]

    index= random.randrange(0,len(words)) #Generate a random number in the bounds of list
    randWord=words[index] #Find corresponding word and hint for random index
    randHint=hints[index]
    l1=list(randWord) #Turn random word into a list
    length=len(l1) #Create a length variable to use in while loop
    jumbledWord="" #Create an empty string and count variable
    count=0
    while count<length: #Loop through entire list
        char=random.choice(l1) #Find random char
        jumbledWord+=char #Add to empty string
        l1.remove(char) #Remove from list
        count=count+1 #Increment count
    print("The jumbled word is","\"" + jumbledWord + "\"")

    numGuesses=1 #Ask user for guess and track attempts
    guess = input("Enter your guess: ").lower()
    while guess!=randWord: #As long as answer is wrong, keep running
        print("That is not correct")
        hint= input("Do you want a hint (y or n)? ").lower() #Ask user if they want a hint
        if(hint=="y"): #If yes, output the hint
            print("The hint is","\""+ randHint + "\"")
        numGuesses+=1 #Incremenet number of guesses
        guess = input("Enter your guess: ").lower()
    print("You got it!")
    print("It took you",numGuesses,"guesses")

main()