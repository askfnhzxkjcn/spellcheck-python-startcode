# Spell Check Starter
# This start code creates two lists
# 1: dictionary: a list containing all of the words from "dictionary.txt"
# 2: aliceWords: a list containing all of the words from "AliceInWonderland.txt"

import re  # Needed for splitting text with a regular expression
import time

#linear and binary functions
def linearSearch(list, item):
    for i in range(len(list)):
        if item == list[i]:
            return i
    else:
        return -1

def binarySearch(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        favg = (low + high) // 2
        if item == list[favg]:
            return favg
        elif item < list[favg]:
            high = favg - 1
        else:
            low = favg + 1
    return -1


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
            word = input("Please enter a word: ")

            tStart = time.time()
            i = linearSearch(dictionary, word)
            tEnd = time.time()

            if i == -1:
                print(f"{word} is NOT in the dictionary.", tEnd - tStart, "seconds." )
            else:
                print(f"{word} is in the dictionary at position {i}.", tEnd - tStart, "seconds.")

        #selection 2
        elif selection == "2":

            #input for word
            word = input("Please enter a word: ")


            #timer and set function to i to use returned index
            tStart = time.time()
            i = binarySearch(dictionary, word)
            tEnd = time.time()

            #output
            if i == -1:
                print(f"{word} is NOT in the dictionary.", tEnd - tStart, "seconds."  )
            else:
                print(f"{word} is in the dictionary at position {i}.", tEnd - tStart, "seconds.")


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
    
    dictionary[0:50]
    aliceWords[0:50]
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




