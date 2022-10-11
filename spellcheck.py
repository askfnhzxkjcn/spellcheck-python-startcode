# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

def main():
    dictionary = loadWordsFromFile("data-files/dictionary.txt")
    aliceWords = loadWordsFromFile("data-files/AliceInWonderLand.txt")

    #start menu loop
    loop = True

    while loop:

        #display
        print("MAIN MENU")
        print("1: Spell Check a Word (Linear Search)")
        print("1: Spell Check a Word (Binary Search)")
        print("1: Spell Check Alice In Wonderland (Linear Search")
        print("4: Spell Check Alice In Wonderland (Binary Search)")
        print("5: Exit")

        #selection 1
        selection = input("Unter menu selection (1-5): ")

        #selection
        if selection == "1":
            print("poop")
        
        #selection 2
        elif selection == "2":
            print("poop")

        #selection 3
        elif selection == "3":
            print("poop")

        #selection 4
        elif selection == "4":
            print("poop")

        #selection 5
        else:
            print("Goodbye")
            loop = False
    
    # Load data files into lists
    

    # Print first 50 values of each list to verify contents
    print(dictionary[0:50])
    print(aliceWords[0:50])
# end main()


def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()


# Call main() to begin program
main()




