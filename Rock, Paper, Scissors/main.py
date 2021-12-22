# ITP 115, Fall 2021
# Section: 31856
# Assignment 7
# Description: Write a program that allows the user to play rock-paper-scissors against the computer.
# Your code will randomly choose an integer from 0 to 2 (inclusive), which will represent
# the computer’s choice with 0 for rock, 1 for paper, and 2 for scissors. The user will enter
# an integer for their choice.

import random

#Function Name: displayMenu
#Input: None
#Return: None
#Side Effect: Prints a series of instructions
#Description: This function tells the uer how to play rock, paper, scissors
def displayMenu():
    print("Let's play Rock Paper Scissors.")
    print("The rules of the game are:")
    print("\tRock smashes Scissors")
    print("\tScissors cut Paper")
    print("\tPaper covers Rock")
    print("\tIf both the choices are the same, it's a tie")

#Function Name: getComputerChoice
#Input: None
#Return: An int of 0, 1, or 2 depending on a random generator
#Side Effect: None
#Description: This function represents the computers choice of rock, paper, or scissors
def getComputerChoice():
    compChoice=random.randint(0,2) #Generate a random numeber
    return compChoice

#Function Name: getPlayerChoice
#Input: None
#Return: An int of 0, 1, or 2, depending on user input
#Side Effect: Prints instructions for what each value represens
#Description: This function asks the user to choose rock,paper,scisors
def getPlayerChoice():
    print("Enter 0 for Rock, 1 for Paper, or 2 for Scissors")
    playChoice = -1 #Placeholder
    while playChoice<0 or playChoice>2: #While invalid choice, keep asking for another input
        playChoice=int(input("> "))
    return playChoice

#Function Name: playRound
#Input: computer's choice and player's choicce
#Return: An int value that represents if player won or lost the round
#Side Effect: None
#Description: This functions represents playing 1 round of rock, paper, scissors
def playRound(computer,player):
    if computer==0:
        if player==0: #Series of comparisons and if statements to determine who wins
            return 0
        elif player==1:
            return 1
        elif player==2:
            return -1
    if computer==1:
        if player==0:
            return -1
        elif player==1:
            return 0
        elif player==2:
            return 1
    if computer==2:
        if player==0:
            return 1
        elif player==1:
            return -1
        elif player==2:
            return 0

#Function Name: continueGame
#Input: None
#Return: True or False boolean
#Side Effect: Prints message asking if user wants to keep playing
#Description: Asks user if they want to continue the game
def continueGame():
    cont=input("Do you want to continue playing (y or n)? ").lower() #Ask for input to keep playing
    if cont=="y":
        return True #Return True if user inputs y or Y
    return False

def main():
    playerWins=0 #Track wins and ties
    computerWins=0
    ties=0
    cont=True
    while cont==True:
        displayMenu() #Display the menu and get user and computer choice
        player=getPlayerChoice()
        computer=getComputerChoice()
        if playRound(computer,player) == 0: #Check who wins and update counts
            ties+=1
            print("You and the computer tied.")
        elif playRound(computer,player) == 1:
            playerWins+=1
            print("You win!")
        elif playRound(computer,player) == -1:
            computerWins+=1
            print("Computer wins.")
        cont=continueGame() #Ask if user wants to continue
        print("") #Newline for formatting
    print("You won",playerWins,"game(s).") #Print how many wins
    print("The computer won",computerWins,"game(s).")
    print("You tied with the computer",ties,"time(s).")

main()