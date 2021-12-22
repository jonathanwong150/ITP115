# Jonathan Wong, jzwong@usc.edu
# ITP 115, Fall 2021
# Section: 31856
# Assignment 4
# Description:

def main():
    again="y" #Set a starting true variable for do-while loop
    while (again.lower()=="y"): #Check if user wants to enter another set of numbers
        print("Input an integer greater than or equal to 0 or -1 to quit: ")
        var=int(input("> ")) #Takes user input
        max=var #Sets initial max and min values as well as sum and count
        min=var
        sum=0
        count=0
        while(var!=-1 and var>0): #While the values are valid,
            count+=1 #increment count
            sum+=var #Adjust sum
            if(var>max): #Check if input is greater than current max
                max=var
            if(var<min): #Check if input is less than current min
                min=var
            var=int(input("> ")) #Ask user or input again

        avg=sum/count #Calculate average
        print("The largest number is", max) #Print statements
        print("The smallest number is", min)
        print("The average nummber is", avg)
        print("")
        again=input("Would you like to enter another set of numbers (y/n)?: ") #Ask user if they want to try again
    print("")
    print("Goodbye!")
main()