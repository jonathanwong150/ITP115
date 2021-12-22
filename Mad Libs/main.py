#Jonathan Wong, jzwong@usc.edu
#ITP 115, Fall 2021
#Section: 31856
#Assignment 2
#Description: This program creates a madlib story with input and output.

def main():
    #Read the user inputted strings
    color=input("Enter a color: ")
    object=input("Enter an object: ")
    verb=input("Enter a verb ending with \"ing\": ")
    restaurant=input("Enter a restaurant: ")
    adj=input("Enter an adjective: ")

    #Read the user inputted ints and float
    num1=input("Enter a number: ")
    num2=input("Enter another number: ")
    num3=input("Enter one more number: ")
    float1=input("Enter a decimal: ")

    #Add 2 of the ints together
    add= str(int(num1)+int(num2))

    #Print the story with inputs
    print("Today, I went to the aquarium and I saw \"" + num1 + "\" seals.")
    print("Then, another \"" + num2 + "\" seals came from behind the \"" + object + "\".")
    print("Now there were \"" + add +"\" seals \"" + verb +"\" together in groups of \"" + num3+ "\".")
    print("Watching the seals made me hungry so I went to \"" + restaurant + "\".")
    print("The line was \"" + float1 + "\" minutes long but the food was so \"" + adj+"\" which made it worth the wait.")

main()