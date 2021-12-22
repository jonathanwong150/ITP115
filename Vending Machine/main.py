# Jonathan Wong, jzwong@usc.edu
# ITP 115, Fall 2021
# Section: 31856
# Assignment 3
# Description: This program creates a Harry Potter vending machine.
# It determines the change and gives a discount.

#1 knut = 1 knut
#1 sickle = 29 knuts
#1 galleon = 17 sickles = 493 knuts
def main():
    print("Please select an item from the vending machine:") #Prints out the menu
    print("\ta) Assortment of Candy for 11 sickles and 7 knuts")
    print("\tb) Butterbeer for 2 sickles")
    print("\tc) Quill for 6 sickles")
    print("\td) Daily Prophet for 5 knuts")
    choice= input("Choice: ") #Asks user for their choice
    if choice.lower()=="a": #Series if statements to find which item user wants
        item="Assortment of Candy" #Sets the item name and cost
        cost=(11*29)+7
    elif choice.lower()=="b":
        item="Butterbeer"
        cost=2*29
    elif choice.lower()=="c":
        item="Quill"
        cost=6*29
    elif choice.lower()=="d":
        item="Daily Prophet"
        cost=5
    else:
        print("You entered an invalid choice, thus the item selected is the Quill") #If user picks something invalid
        item="Quill" #Give them a quill
        cost=6*29
    print("\nPlease pay by entering the number of each coin")
    galleons=int(input("Number of galleons: ")) #Asks user to pay with galleons, sickles, and knuts
    sickles =int(input("Number of sickles: "))
    knuts = int(input("Number of knuts: "))
    print("\nCost in knuts: " + str(cost)) #Print the cost
    payment = galleons*493+sickles*29+knuts #Calculate the payment
    print("Payment in knuts: " + str(payment))
    if(payment<cost): #Check if user has enough money to buy the item
        print("You did not enter enough money and will not receive the " + item)
    else:
        change=payment-cost #Find change
        print("\nYou purchased the " + item) #Order summary
        print("Your change is " + str(change))
        print("You will be given")
        numGall=change//493 #Find how many galleons user will get
        print("\tGalleons: " + str(numGall))
        change-=(numGall*493) #Update change amount
        numSick=change//29 #Find how many sickles
        print("\tSickles: " + str(numSick))
        change-=(numSick*29) #Update change amount
        print("\tKnuts: " + str(change))

main()