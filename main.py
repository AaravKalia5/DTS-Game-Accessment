import time
import random

knife_random = random.randint(6,15)
ak47_random = random.randint(40,100)
rifle_random = random.randint(30,70)
glock_random = random.randint(40,90)
hammer_random = random.randint(5,10)


normal_battle = 50
level_two_battle = 100
player_health = 0
money = 0
inv = []
all_wepons = [

    {"Name" : "Knife",
     "Range" : 1,
     "Damage" : knife_random
     },


    {"Name" : "AK47",
     "Range" : 140,
     "Damage" : ak47_random
     },


    {"Name" : "Rifle",
     "Range" : 180,
     "Damage" : rifle_random
     },


    {"Name" : "Glock",
     "Range" : 50,
     "Damage" : glock_random
     },

    {"Name" : "Hammer",
     "Range" : 2,
     "Damage" : hammer_random
     }

]


lacelle_attacks_hash = [

    {"Name" : "Python Program", "Damage" : random.randint(5, 15), "Rewards" : normal_battle},
    {"Name" : "Godot Throw", "Damage" : random.randint(15, 25), "Rewards" : normal_battle},
    {"Name" : "Rant", "Damage" : random.randint(25, 40), "Rewards" : normal_battle}

]

denham_attacks_hash = [

    {"Name": "Basketball", "Damage": random.randint(25, 40), "Rewards": level_two_battle},
    {"Name": "Podium Chuck", "Damage": random.randint(30, 50), "Rewards": level_two_battle},
    {"Name": "Stop Vaping Boys", "Damage": random.randint(50, 80), "Rewards": level_two_battle}

]

corliss_attacks_hash = [

    {"Name": "Homework", "Damage" : random.randint(5, 10), "Rewards": normal_battle},
    {"Name": "Complex Equation", "Damage": random.randint(15, 25), "Rewards": normal_battle},
    {"Name": "Problem", "Damage" : random.randint(25, 30), "Rewards": normal_battle}

]


lacelle_attacks = random.choice(lacelle_attacks_hash)
denham_attacks = random.choice(denham_attacks_hash)
corliss_attacks = random.choice(corliss_attacks_hash)
def player():
    global player_health
    print("")
    player_name = input("What would you like to name your player? :  ")
    print("")
    player_age = int(input("how old is your in game player? :  "))


    if player_age < 10:
        player_health += 30

    elif player_age < 20:
        player_health += 60

    elif player_age < 30:
        player_health += 100

    elif player_age < 40:
        player_health += 90

    elif player_age < 50:
        player_health += 50

    elif player_age > 60:
        player_health += 20

    player_hash = [

        {"Name": player_name,
         "Health": player_health
         }

    ]


    player_usable_name = random.choice(player_hash)
    print("")
    print("")
    print("Your player is called", player_usable_name["Name"], "it has", player_usable_name["Health"], "health.")



def enemy():
    print("")

    enemy_hash = [

        {"Name" : "Mr. Lacelles", "Type" : "Computer", "Level" : 1, "Attack" : lacelle_attacks},
        {"Name" : "Mr. Denham", "Type" : "Boss", "Level" : 2, "Attack" : denham_attacks},
        {"Name" : "Mr. Corliss", "Type" : "Math", "Level" : 1, "Attack" : corliss_attacks}
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
    player()



#MAIN
intro()
