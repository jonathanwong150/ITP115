#Jonathan Wong, jzwong@usc.edu
#ITP 115, Fall 2021
#Section: 31856
#Assignment 1
#Description: This program displays two truths and a lie.

def main():
    #Create first and last name variables
    first= "Jonathan"
    last= "Wong"

    #Create 2 true statements and 1 false statement
    statement1="I am left-handed."
    statement2="I play basketball."
    statement3="I live in Virginia."

    #Denote which statements are true and false
    truth1=True
    truth2=True
    truth3=False

    #Create variables with number of siblings and pets
    pets=1
    siblings=0

    #Print a series of statements using the variables
    print("Full name: " + first + " " + last)
    print("Number of pets: " + str(pets))
    print("Number of siblings: " + str(siblings))
    print("Statement 1: " + statement1)
    print("Statement 2: " + statement2)
    print("Statement 3: " + statement3)
    print("Statement 1 is",truth1)
    print("Statement 2 is",truth2)
    print("Statement 3 is",truth3)

main()