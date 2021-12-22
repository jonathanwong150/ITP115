# ITP 115, Fall 2021
# Section: 31856
# Assignment 9
# Description: Write a language translator program that translates English words to another language
# using data from a CSV file.

#Function Name: getLanguages
#Input: fileName is a string containing the name of a CSV file to read from and it has a default value of "languages.csv"
#Return: a list of strings representing the languages in the header row
#Side Effect: None
#Description: Open the CSV file and get the header row with the languages and put it into a list
def getLanguages(fileName):
    languages=[] #Create empty languages list
    fileIn=open(fileName, "r") #Open the file
    header=fileIn.readline().split(",") #Take the first line and split up the languages
    for lang in range(len(header)): #For each language in the first line, add to the list
        languages.append(header[lang].lower())
    fileIn.close()
    return languages

# Function Name: getTranslationLanguage
# Input: langList is a list of the languages
# Return: a string for the language to translate words into
# Side Effect: Prints a menu and error message if language is not in list
# Description: Display to the user the languages that are available for translation
def getTranslationLanguage(langList):
    print("Translate English words to one of the following languages: \nDanish Dutch Finnish French German Indonesian \nItalian Japanese Latin Norwegian Portuguese Spanish Swahili Swedish")
    langInput=input("Enter a language: ") # Print menu and ask for a language
    while langInput.lower() not in langList: # Keep asking until the language exists in our list
        print("This program does not support",langInput)
        langInput = input("Enter a language: ")
    print("")
    return langInput.title()

# Function Name: readFile
# Input: list of the languages, langStr is a string of containing the name of a language and it has a default value of "English",
# fileName is a string containing the name of a CSV file to read from and it has a default value of "languages.csv"
# Return: a list of words in the language identified by the langStr parameter
# Side Effect: None
# Description: Reads a file for a language and returns a list of all words
def readFile(langList, langStr, fileName):
    words=[] # Create empty words list
    fileIn=open(fileName, "r") # Open file
    header=fileIn.readline() # Ignore first line
    index=langList.index(langStr.lower()) #  Find the index of our desired language
    for line in fileIn: # For each line in the file
        currLine=line.strip().split(",") # Split the line and add the word at desired languages index
        words.append(currLine[index])
    fileIn.close()
    return words

# Function Name: createResultsFile
# Input: language is a string containing the name of the language for translation
# Return: None
# Side Effect: Creates a new output file and prints text in it
# Description: Create a result file such that any existing info will be overwritten and print a message in it
def createResultsFile(language):
    file = language + ".txt"  # Create the name of output file
    fileOut = open(file, "w") # Open in write mode
    print("Words translated from English to",language, file=fileOut)  # Print a message
    fileOut.close()

#Function Name: translateWords
#Input: englishList is a list of words in English, translationList is a list of words in another language (not English)
#language is a string containing the language of the words in the translationList
#Return: None
#Side Effect: Prints to output and into result file
#Description: Ask user for a word, translates it, and append to results file
def translateWords(englishList, translationList, language):
    file = language + ".txt"
    fileOut=open(file,"a") #Open output file
    again = "y"
    while again=="y": #Create do-while loop
        word=input("Enter a word to translate: ") #Ask the user for a word
        if word not in englishList:
            print(word,"is not in the list") #If it doesnt exist, print error message
        else:
            index=englishList.index(word) #Find the index of the english word
            transWord=translationList[index] #Find translated word at same index of other language list
            if transWord=="-":
                print(word,"did not have a translation") #Check if doesn't have a translation
            else:
                print(word,"is translated to",transWord) #If it does, output to screen and file
                print(word,"=",transWord, file=fileOut)
        again=input("Another word (y or n)? ").lower() #Ask for another word
        print("")
    print("Translated words have been saved to",file)
    fileOut.close()

def main():
    print("Language Translator")
    langList=getLanguages("languages.csv") #Get header of languages
    lang=getTranslationLanguage(langList) #Get desired language
    createResultsFile(lang)  # Create an output file
    engList=readFile(langList,"English","languages.csv") #Get list of English words
    transList=readFile(langList,lang,"languages.csv") #Get list of desired words
    translateWords(engList,transList,lang) #Translate

main()