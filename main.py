import time
import random


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
            na()
            break

        elif skip == "A":
            print("")
            context()
            print("")
            break

        else:
            print("")
            print("Please use 'A' or 'S'")
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
    user_input = input("Press 'R' to read again or press 'A' to continue :  ")


def na():
    print("**Other thing go here**")


intro()
