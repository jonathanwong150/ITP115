# ITP 115, Fall 2021
# Section: 31856
# Assignment 8
# Description: Write a program that uses functions to simulate a two-player game of Tic Tac Toe. The
# program will allow the two players to place an "x" or an "o" somewhere on the board
# and determine when someone wins or when a stalemate is reached.

import TicTacToeHelper

#Function Name: isValidMove
#Input: A list with the current board and a user-inputted spot
#Return: boolean
#Side Effect: None
#Description: This function finds if the user has chosen a valid spot on the board
def isValidMove(boardList,spot):
    if spot>8 or spot<0: #Check if move is in bounds
        return False
    if boardList[spot]=="x" or boardList[spot]=="o": #Check if it already has been chosen
        return False
    return True #Return true if valid

#Function Name: updateBoard
#Input: a list with the current board, user-inputted spot, and string representing the player
#Return: None
#Side Effect: Sets a spot on the board to the player's letter
#Description: Updates the game board given the player's choice and letter
def updateBoard(boardList,spot,playerLetter):
    if isValidMove(boardList,spot)==True: #If move is valid
        boardList[spot]=playerLetter #Find spot and replace with the players letter

#Function Name: playGame
#Input: None
#Return: None
#Side Effect: Calls other functions and alters the game board
#Description: This function simulates a game of tic tac toe with other methods
def playGame():
    board=["0","1","2","3","4","5","6","7","8"] #Create a board, print board
    print("Welcome to Tic Tac Toe!")
    TicTacToeHelper.printUglyBoard(board)
    counter=0 #Declare necessary variables
    winner="n"
    player="x"
    move=-1
    while winner=="n": #While winner is still n
        if counter%2==0: #Check who's turn it is
            player="x"
        else:
            player="o"
        statement="Player " + player + " pick a spot: "
        while isValidMove(board,move)==False: #Keep asking for input until valid
            move=int(input(statement))
        updateBoard(board,move,player) #Make the move
        TicTacToeHelper.printUglyBoard(board) #Print board
        counter+=1 #Increment counter and check for winner
        winner=TicTacToeHelper.checkForWinner(board,counter)
    print("Game Over!")
    if winner=="s": #Print results
        print("Stalemate reached!")
    else:
        print("Player",winner,"is the winner!")

def main():
    again="y" #Do-while loop
    while again=="y":
        playGame()
        again=input("Would you like to play another round? (y or n): ").lower()

main()