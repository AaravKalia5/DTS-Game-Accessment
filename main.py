import time
import random

knife_random = random.randint(6,15)
ak47_random = random.randint(40,100)
rifle_random = random.randint(30,70)
glock_random = random.randint(40,90)
hammer_random = random.randint(5,10)


money = 0
inv = []
all_wepons = [

    {"Name" : "Knife", "Range" : 1, "Damage" : knife_random},
    {"Name" : "AK47", "Range" : 140, "Damage" : ak47_random},
    {"Name" : "Rifle", "Range" : 180, "Damage" : rifle_random},
    {"Name" : "Glock", "Range" : 50, "Damage" : glock_random},
    {"Name" : "Hammer", "Range" : 2, "Damage" : hammer_random}

]






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
    random_weapon = random.choice(all_wepons)

    print("")
    print("")
    print("You found a", random_weapon["Name"])
    print("")
    print("This deals", random_weapon["Damage"], "damage")
    print("")
    print("You can use this up to", random_weapon["Range"], "meters")
    print("")
    print("----------------------------------------------------------")
    print("")

    inv.append(random_weapon)
    print("Inventory:")
    print("")
    print("")
    for item in inv:
        print("Name:", item["Name"])
        print("Range:", item["Range"])
        print("Damage:", item["Damage"])
        print("")

    print("")
    print("You can press 'E' at anytime when we ask for input to show your inventory.")
    print("")
    print("")



#MAIN
intro()
