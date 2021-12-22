# Jonathan Wong, jzwong@usc.edu
# ITP 115, Fall 2021
# Section: 31856
# Assignment 5
# Description: Program that allows the user to enter a sentence and then uses looping to print
# an asterisk (*) to show the character distribution.

def main():
    alphabet="abcdefghijklmnopqrstuvwxyz" #Create alphabet variable
    runTimes=int(input("Enter the number of times to run: ")) #Ask user for times to run
    print(" ") #Print a newline

    for i in range(runTimes): #Use outer for loop to run the amount of times user inputted
        str= input("Enter a sentence: ")
        chars=0 #Number of normal characters to track number of special characters
        str=str.replace(" ", "") #Get rid of all of the spaces in string
        for x in str:
            if x.isalpha()==True: #Check if string is just letters and increment normal char. count
                chars+=1
        numSpecial = len(str) - chars  #Number of special characters is the length-number of normal characters
        if(numSpecial==0): #Print number of special characters
            print("Special Characters: NONE")
        else:
            print("Special Characters: " + "*" * numSpecial)
        for letter in alphabet: #loop through each letter in the alphabet
            count=0 #Initalize a count variable every time the outer loop runs
            for character in str: #Loop through each character in the string
                if(letter==character.lower()): #If the variables match, increment count and number of normal characters
                    count=count+1
            if(count==0): #Print none if the letter of outer loop got no matches
                print(letter + ": NONE")
            else:
                print(letter + ": " + "*" * count) #Print amount of times letter appears
        print(" ")

main()