#FASTQ to FASTA
#This program converts a FASTQ file to a FASTA file
#A program by Tyler Serio
#Python 3.7.4
#Circa late October 2019

#IMPORT RELEVANT TOOLS
import os.path
from os import path

#DEFINE FUNCTIONS
def convert():
    opening = 1

    #open the fastq file
    while opening == 1:
        print("Which file would you like to open?")
        print("Example: 'ancient_sequences.fastq'")
        print("Please type the name of the file exactly.")
        fastqfile = input ("or type [0] to return to menu. ")
        print("")
        if fastqfile == "0":
            break

        #check to see if the file exists
        path.exists(fastqfile)
        if path.exists(fastqfile) == True:
            print("I will retrieve your file.")
            print("I have found your file.")
            print("")
            fastqfile = open(fastqfile, "r")
            opening = 2
            break

        #if the file does not exist ask the user for a new one
        if path.exists(fastqfile) == False:
            print("I will retrieve your file.")
            print("I cannot find this file. Make sure to type the file name exactly.")
            print("Try again, or type [0] to return to the menu.")
            print("")
            opening = 1       

    #define important variables
    #this variable holds the sequence ID
    sID = []
    #this variable holds the sequence
    s = []
    #this variable creates the output file
    fastafile = open("fasta_output.fasta", "w")
    
    #go through the fastq file and take out the relevant information
    line_place = 0
    for line in fastqfile:
        line_place += 1
        if line_place == 1:
            sID = line
        if line_place == 2:
            s = line
        if line_place >= 4:
            fastafile.write(sID)
            fastafile.write(s)
            line_place = 0

    #tell the user something has happened
    print("Done.")
    print("The file has been converted.")
    print("")

    #close the files
    fastqfile.close()
    fastafile.close()

#Begin the program
running = 1
print("")

#display the menu
print("Hello.")
while running == 1:
    print("What would you like to do?")
    print("")
    print("[1] - Convert a FASTQ file to a FASTA file.")
    print("[0] - Exit.")
    print("")
    selecting = 1

    #make a selection
    while selecting == 1:
        selection = 0
        selection = input("Which do you choose? ")
        print("")
        if (selection != "1" and selection != "0"):
            if selection == "":
                selection == ("Nothing")
            print("You have chosen [" + selection + "].")
            print("That is not a proper selection.")
            print("Please choose from the list of selections.")
        else:
            selecting = 0

    #handle exit selection
    if selection == "0":
        print("Goodbye.")
        selecting = 2

        #make sure they really want to exit
        while selecting == 2:
            print("Are you sure you want to exit?")
            print("")
            print("[y] - Yes.")
            print("[n] - No.")
            print("")
            selection = input("Which do you choose? ")
            print("")
            if (selection != "y" and selection != "n"):
                if selection == "":
                    selection == ("Nothing")
                print("You have chosen [" + selection + "].")
                print("That is not a proper selection.")
                print("Please choose from the list of selections.")
            if selection == "y":
                exit()
            if selection == "n":
                print("Oops. Nevermind then.")
                selecting = 0

    #run the program
    if selection == "1":
        convert()

