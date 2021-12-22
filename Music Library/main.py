# ITP 115, Fall 2021
# Section: 31856
# Assignment 10
# Description: Create a dictionary to manage data. Allow the user to insert, update, and delete data
# from the dictionary.

import MusicLibraryHelper
import random

#Function Name: displayMenu
#Input: None
#Return: None
#Side Effect: Prints statements to output
#Description: Prints a menu
def displayMenu():
    print("Manage Your Music Library")
    print("\ta) Display library")
    print("\tb) Display artists")
    print("\tc) Add an artist/album")
    print("\td) Delete an album")
    print("\te) Delete an artist")
    print("\tf) Generate a random playlist")
    print("\tg) Exit")

#Function Name: displayLibrary
#Input: Dictionary with artists and albums in it
#Return: None
#Side Effect: Prints statements to output
#Description: Prints the entire dictionary's artists and albums
def displayLibrary(dictionary):
    for key in dictionary: #Iterate through the dictionary
        print("Artist:",key) #Print the artist
        print("\tAlbums:")
        for item in range(len(dictionary[key])): #Iterate through the artists album list and print
            print("\t\t"+dictionary[key][item])

#Function Name: displayArtists
#Input: Dictionary with artists and albums in it
#Return: None
#Side Effect: Prints statements to output
#Description: Prints the entire dictionary's artists
def displayArtists(dictionary):
    print("Artists:")
    for key in dictionary: #Iterate through dictionary and print the keys
        print("\t"+key)

#Function Name: addAlbum
#Input: Dictionary with artists and albums in it
#Return: None
#Side Effect: Prints to output and appends to an artists album list in dictionary
#Description: Ask the user for an artist and album, and depending on if artist already exists, append to dictionary
def addAlbum(dictionary):
    artist=input("Enter artist: ").title() #Ask the user for inputs
    album=input("Enter album: ").title()
    list=[]
    if artist in dictionary: #If the artist already exists in dictionary, append to album list
        dictionary[artist].append(album)
    else:
        list.append(album) #If not, create a new list and append the list with artist to the dictionary
        dictionary[artist]=list

#Function Name: deleteAlbum
#Input: Dictionary with artists and albums in it
#Return: A boolean that shows if album was successfully deleted
#Side Effect: Prints statements to output and removes from dictionary
#Description: Finds an album in the dictionary and deletes it
def deleteAlbum(dictionary):
    deleted=False #Set deleted flag to false
    artist=input("Enter artist: ").title() #Ask for inputs
    album=input("Enter album: ").title()
    if artist in dictionary and album in dictionary[artist]: #If the artist and album exist
        dictionary[artist].remove(album) #Remove album from artist list
        deleted=True #Change flag
    return deleted

#Function Name: deleteArtist
#Input: Dictionary with artists and albums in it
#Return: A boolean that shows if artist was successfully deleted
#Side Effect: Prints statements to output and removes from dictionary
#Description: Finds an artist in the dictionary and deletes it and their albums
def deleteArtist(dictionary):
    deleted = False #Set flag to False
    artist = input("Enter artist: ").title() #Ask for input
    if artist in dictionary: #If the artist exists in the dictionary,
        del dictionary[artist] #Delete the artist and its albums
        deleted=True
    return deleted

#Function Name: generateRandomPlaylist
#Input: Dictionary with artists and albums in it
#Return: None
#Side Effect: Prints statements to output
#Description: Picks a random album by each artist and prints to screen
def generateRandomPlaylist(dictionary):
    print("Here is your random playlist:")
    for artist in dictionary: #Loops through each artist
        print("\t",random.choice(dictionary[artist]),"by the",artist) #Pick a random choice from list

def main():
    file="musicLibrary.dat" #Create file variable
    dict=MusicLibraryHelper.loadLibrary(file) #Load the dictionary file
    displayMenu() #Display menu
    choice=input("Choice: ").lower() #Ask user for a true
    while True: #Continue asking the user for a choice until they exist
        if choice == "a": #Series of if statements that dictate what the user wants to do
            displayLibrary(dict)
        elif choice == "b":
            displayArtists(dict)
        elif choice == "c":
            addAlbum(dict)
        elif choice == "d":
            worked=deleteAlbum(dict)
            if worked == True: #If album was successfully deleted, print statement
                print("Delete album success")
            else: #Otherwise, print that it failed
                print("Delete album failed")
        elif choice == "e":
            worked=deleteArtist(dict)
            if worked == True: #If artist was deleted, print
                print("Delete artist success")
            else:
                print("Delete artist failed")
        elif choice == "f":
            generateRandomPlaylist(dict)
        elif choice == "g":
            fileName=input("Enter music library filename: ") #Ask user where they want to save dictionary
            MusicLibraryHelper.saveLibrary(fileName,dict) #Use the helper function
            print("Saved music library to",fileName)
            return #Quit the program
        else:
            print("Invalid choice")
        displayMenu()
        choice = input("Choice: ").lower()

main()