import time
import random

money = 0
inv = []

def intro():
    print("------------------------")
    print("Te-Papa Wellington Games")
    print("------------------------")
    print("")
    print("")

    while True:
        skip = input("Press 'S' to skip intro or press 'A' to continue :  ").upper()
        print("")
        print("")

        if skip == "S":
            map()
            break

        elif skip == "A":
            print("")
            context()
            print("")
            break

        else:
            print("")
            print("")
            print("---------------------")
            print("Please use 'A' or 'S'")
            print("---------------------")
            print("")
            print("")


def context():
    print("Welcome to Te-Papa Wellington")
    print("")
    print("A huge tornado hit wellington last week.")
    print("")
    print("Te-Papa is has been crushed by the tornado.")
    print("")
    print("To rebuild Te-Papa you will have to earn $100,000.")
    print("")
    print("To earn this amount you will have to complete mini games.")
    print("")
    print("These mini games were placed by Te-Papa before the tornado.")
    print("")
    print("They are located all over Wellington.")
    print("")
    print("You are currently standing at Te-Papa and there are 5 mini games in total.")
    print("")



    while True:
        user_input = input("Press 'R' to read again or press 'A' to continue :  ").upper()

        if user_input == "R":
            context()
            break

        elif user_input == "A":
            map()
            break

        else:
            print("")
            print("")
            print("---------------------")
            print("Please use 'R' or 'A'")
            print("---------------------")
            print("")
            print("")
def map():
    print("")
    print("")
    print("This is the map:")
    print("")
    print("-------")
    print("|  A  |  Area 'A' is an 'RPG Fighter'")
    print("-------")
    print("")
    print("-------")
    print("|  B  |  Area 'B' is ")
    print("-------")
    print("")
    print("-------")
    print("|  C  |  Area 'C' is")
    print("-------")
    print("")
    print("-------")
    print("|  D  |  Area 'D' is")
    print("-------")
    print("")
    print("-------")
    print("|  E  |  Area 'E' is")
    print("-------")


    while True:
        user_input = input("Enter here: ").upper()

        if user_input == "A":
            rpg()
            break

        elif user_input == "B":
            print("")
            print("")


#RPG SHOOTER
def rpg():
    print("")
    print("")
    print("Welcome to the RPG Shooter")
    print("")
    print("Each battle is worth $50")
    print("")
    print("If you defeat a Level 2 Boss You will gain an additional $100")
    print("")

    while True:
        user_input = input("Press A to start: ").upper()

        if user_input == "A":
            rpg_continued()
            break

        else:
            print("")
            print("")
            print("-------------------------")
            print("Please Enter 'A' to Start")
            print("-------------------------")
            print("")
            print("")

def rpg_continued():
    print("")
    print("")
    print("")


#MAIN
intro()
