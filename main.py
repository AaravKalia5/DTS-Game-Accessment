import random # import random is used to use the random function such as random.randint or random.choice
import time #import time is used to import the time function and i use it for time.sleep

# this is a hash which is used to store multiple variables in a single index of a list, here I use it to store the wepons and their attributes
all_weapons = [
    {"Name": "Knife", "Range": 1, "Damage": random.randint(6, 15)},
    {"Name": "AK47", "Range": 140, "Damage": random.randint(40, 100)},
    {"Name": "Rifle", "Range": 180, "Damage": random.randint(30, 70)},
    {"Name": "Glock", "Range": 50, "Damage": random.randint(40, 90)},
    {"Name": "Hammer", "Range": 2, "Damage": random.randint(5, 10)}
]

# these hashes are for attackes for each enemy
lacelle_attacks_hash = [
    {"Name": "Python Program", "Damage": random.randint(5, 15), "Rewards": 50, "Range": 1},
    {"Name": "Godot Throw", "Damage": random.randint(15, 25), "Rewards": 50, "Range": 40},
    {"Name": "Rant", "Damage": random.randint(25, 40), "Rewards": 50, "Range": 60}
]

denham_attacks_hash = [
    {"Name": "Basketball", "Damage": random.randint(25, 40), "Rewards": 100, "Range": 150},
    {"Name": "Podium Chuck", "Damage": random.randint(30, 50), "Rewards": 100, "Range": 100},
    {"Name": "''Stop Vaping Boys''", "Damage": random.randint(50, 80), "Rewards": 100, "Range": 70}
]

corliss_attacks_hash = [
    {"Name": "Homework", "Damage": random.randint(5, 10), "Rewards": 50, "Range": 60},
    {"Name": "Complex Equation", "Damage": random.randint(15, 25), "Rewards": 50, "Range": 80},
    {"Name": "Problem", "Damage": random.randint(25, 30), "Rewards": 50, "Range": 100}
]

zajko_attacks_hash = [
    {"Name": "Yell", "Damage": random.randint(10, 60), "Rewards": 100, "Range": 60},
    {"Name": "Intimidation", "Damage": random.randint(20, 80), "Rewards": 100, "Range": 80},
    {"Name": "Stare", "Damage": random.randint(25, 30), "Rewards": 100, "Range": 100}
]

bergin_attacks_hash = [
    {"Name": "After Assembly Speech", "Damage": random.randint(10, 20), "Rewards": 50, "Range": 70},
    {"Name": "Park Your Mopeds Correctly", "Damage": random.randint(20, 40), "Rewards": 50, "Range": 20},
    {"Name": "Detention", "Damage": random.randint(25, 50), "Rewards": 50, "Range": 70}
]

enemy_hash = [
    {"Name": "Mr. Lacelles", "Level": 1, "Attacks": lacelle_attacks_hash,
     "Health": random.randint(20, 100)},
    {"Name": "Mr. Denham", "Level": 2, "Attacks": denham_attacks_hash,
     "Health": random.randint(20, 100)},
    {"Name": "Mr. Corliss", "Level": 1, "Attacks": corliss_attacks_hash,
     "Health": random.randint(20, 100)},
    {"Name": "Mr. Zajko", "Level": 2, "Attacks": zajko_attacks_hash,
     "Health": random.randint(20, 100)},
    {"Name": "Mr. Bergin", "Level": 1, "Attacks": bergin_attacks_hash,
     "Health": random.randint(20, 100)}
]


# these are variables which are used to store one piece of information, here I use these variables to store simple player stats
player_health = 0
money = 0

# this is a list which is used to store multiple pieces of information, here I use it as an inventory
inventory = []


#this is a function which is used to run a specific fucntion at anytime, here I use it to reset all of the player stats for when the player desides to reset the game
def reset_game():
    global player_health, money, inventory
    player_health = 0
    money = 0
    inventory = []


def player_setup():
    global player_health # global is used to globalize the variable in the function, here I use it to globalize player_health
    print("Welcome to Te-Papa Wellington!") #print is used to print a line of human language
    print("")
    player_name = input("What would you like to name your player? : ").capitalize() #input is used to take input from the user and store it in the variable that it is in, here I use it to store the player name
    print("")                                                                       #.capatalize is used to capatalise anything, here I use it to capatalize the plaer name
    player_age = int(input("How old is your in-game player? : ")) #an int input is a normal input but only for full numbers and it will be stored as an int not srt
    print("")
    if player_age < 10: # an if statement is to add conditions or determine things according to other things in the program, here I use if statement to determine the player health accordint to age.
        player_health = 30
    elif player_age < 20:
        player_health = 60
    elif player_age < 30:
        player_health = 100
    elif player_age < 40:
        player_health = 90
    elif player_age < 50:
        player_health = 50
    elif player_age > 60:
        player_health = 20
    print("")
    print("Your player is called", player_name, "and has", player_health, "health.")
    print("")


def find_weapons():
    print("You found 3 unique weapons:")
    print("")
    time.sleep(1) #time.sleep is used to add time gaps in code
    for _ in range(3): #for loops are used to repeat something for a cartain amount of times, here I use for loop to make the player find 3 random wepons
        weapon = random.choice(all_weapons)
        while weapon in inventory: #while loops are used to repeat something forever as long as the conditin is met, here I am using it to repeat the randomization prosess of the wepons until I have 3
            weapon = random.choice(all_weapons) #random.choice is used to pick a random choice from a list or hash, here I use it to pick a random wepon from the all_wepons hash
        inventory.append(weapon) #.append is used to add something to a list or hash, her I use it to add the random wepons to the inventory list
        print("Name:", weapon["Name"])
        print("Range:", weapon["Range"])
        print("Damage:", weapon["Damage"])
        print("")
        time.sleep(1)


#a perhenthesis function is used to add veriables in the function so they can be refered to in the function, here I use it to refer player_wepon, enemy and enemy_distance
def battle(player_weapon, enemy, enemy_distance):
    global money
    print("You attack", enemy["Name"], "with", player_weapon["Name"])
    print("")
    time.sleep(1)
    if player_weapon["Range"] >= enemy_distance:
        print("You dealt", player_weapon["Damage"], "damage!")
        print("")
        time.sleep(1)
        enemy["Health"] -= player_weapon["Damage"]
        if enemy["Health"] <= 0:
            print("You defeated", enemy["Name"])
            print("")
            time.sleep(1)
            money += enemy["Attacks"][0]["Rewards"]
            print("Total $", money)
            print("")
            print("")
            time.sleep(1)
            return True #return True is used to indicate the function a boolean value of True, here I use it to indicate when the player has won the fight
        else:
            print("")
            print(enemy["Name"], "has", enemy["Health"], "health left.")
            print("")
            time.sleep(1)
            return False #return False is used to indicate the function a boolean value of False, here I use it to indicate when the player has not yet won the fight
    else:
        print("")
        print("Enemy is out of range!")
        print("")
        time.sleep(1)
        return False


def run_away():
    print("Booo!, You ran away!! :(")
    print("")
    time.sleep(1)


def intro():
    print("------------------------")
    print("Te-Papa Wellington Games")
    print("------------------------")
    time.sleep(1)
    while True:
        print("")
        skip = input("Press 'S' to skip intro or press 'A' to continue : ").upper()
        print("")
        if skip == "S":
            map()
            break #break is used to break a loop
        elif skip == "A":
            context()
            break
        elif skip == "L":
            reset_game()
            intro()
            break
        else:
            print("Please use 'A', 'S', or 'L'")
            print("")
            time.sleep(1)


def context():
    print("Welcome to Te-Papa Wellington!")
    print("")
    time.sleep(1)
    print("A huge tornado hit Wellington last week.")
    print("")
    time.sleep(1)
    print("Te-Papa has been crushed by the tornado.")
    print("")
    time.sleep(1)
    print("To rebuild Te-Papa, you will have to earn $1000.")
    print("")
    time.sleep(1)
    print("To earn this amount, you will have to complete mini-games.")
    print("")
    time.sleep(1)
    print("These mini-games were placed by Te-Papa before the tornado.")
    print("")
    time.sleep(1)
    print("They are located all over Wellington.")
    print("")
    time.sleep(1)
    print("You are currently standing at Te-Papa, and there are 2 mini-games in total.")
    print("")
    print("")
    print("")
    time.sleep(1)
    while True:
        print("")
        user_input = input("Press 'R' to read again or press 'A' to continue : ").upper()
        print("")
        print("")
        if user_input == "R":
            context()
            break
        elif user_input == "A":
            map()
            break
        elif user_input == "L":
            reset_game()
            intro()
            break
        else:
            print("Please use 'R', 'A', or 'L'")
            print("")
            time.sleep(1)


def map():
    print("This is the map:")
    print("")
    print("-------")
    print("|  A  |  Area 'A' is an 'RPG Fighter'")
    print("-------")
    print("")
    print("-------")
    print("|  B  |  Area 'B' is a 'Trivia'")
    print("-------")
    print("")
    time.sleep(1)
    while True:
        print("")
        user_input = input("What area would you like to go to? : ").upper() #.upper is used to make everything in a variable uppercase, here I use it to make the user_input uppercase so I can add conditions with if statements
        print("")
        print("")
        if user_input == "A":
            rpg()
            break
        elif user_input == "B":
            quiz()
            break
        elif user_input == "L":
            reset_game()
            intro()
            break
        else:
            print("Invalid area!")
            print("")
            time.sleep(1)


def rpg():
    print("Welcome to the RPG Shooter")
    print("")
    time.sleep(1)
    print("Each battle is worth $50")
    print("")
    time.sleep(1)
    print("")
    print("A level 2 boss will reward you $100, but they are mysterious")
    time.sleep(1)
    while True:
        print("")
        user_input = input("Press 'A' to start: ").upper()
        print("")
        if user_input == "A":
            find_weapons()
            rpg_real_fights()
            break
        elif user_input == "L":
            reset_game()
            intro()
            break
        else:
            print("Please Enter 'A' to Start")
            print("")
            time.sleep(1)


def rpg_real_fights():
    global money
    while money < 1000:
        enemy = random.choice(enemy_hash)
        enemy_distance = random.randint(1, 90)
        enemy["Health"] = random.randint(20,100)
        print("")
        for attack in enemy["Attacks"]:
            attack["Damage"] = random.randint(5, 15)
            attack["Range"] = random.randint(1, 60)
        print("")
        print("You have spotted", enemy["Name"], "\nAttack :", enemy["Attacks"][0]["Name"], "\nDamage :",  #\n is used to carry the print to a new line
              enemy["Attacks"][0]["Damage"], "\nRange :", enemy["Attacks"][0]["Range"], "\nDistance :",
              enemy_distance, "\nHealth :", enemy["Health"])
        print("")
        time.sleep(1)

        print("")
        print("Choose a weapon:")
        print("")
        for index, weapon in enumerate(inventory): #enumerate is used to loop over a collection (like a list or tuple) and keep track of the index of the current item, here I use it to loop the 3 wepons and to keep track of their index values
            print(f"{index + 1}: {weapon['Name']} (Range: {weapon['Range']}, Damage: {weapon['Damage']})") #f is used to add variables to a print line without adding the commas.
            print("")                                                                                      # index + 1 is used to show the corresponding number for each wepon
            print("")
        weapon_choice = input("Enter the number of the weapon you want to use: ")
        print("")
        try: #try and except is used to check for user input error and to make sure the user enters the correct type eg, srt, here I use it to make sure they use the correct type of input eg, str
            weapon_index = int(weapon_choice) - 1
            if 0 <= weapon_index < len(inventory): #len is used to find the length of an object, here I use it to make sure that the user has enterd a valid choice which is within the given options
                selected_weapon = inventory[weapon_index]
            else:
                print("Invalid weapon choice. Defaulting to the first weapon.")
                print("")
                selected_weapon = inventory[0]
        except ValueError:
            print("Invalid input. Defaulting to the first weapon.")
            print("")
            selected_weapon = inventory[0]

        while True:
            print("")
            user_input = input("Press 'F' to fight\nPress 'R' to run away\nPress 'E' to view inventory: ").upper()
            print("")
            print("")
            if user_input == "F":
                if selected_weapon["Range"] >= enemy_distance:
                    if battle(selected_weapon, enemy, enemy_distance):
                        break
                    else:
                        print("No weapon with sufficient range to attack. Choose another weapon.")
                        print("")
                else:
                    print("Selected weapon is out of range. Choose another weapon.")
                    print("")
            elif user_input == "R":
                run_away()
                break
            elif user_input == "E":
                print("----------------------------------------------------------")
                print("Inventory:")
                print("")
                for item in inventory:
                    print("Name:", item["Name"])
                    print("Range:", item["Range"])
                    print("Damage:", item["Damage"])
                    print("")
                print("----------------------------------------------------------")
                time.sleep(1)
            elif user_input == "L":
                reset_game()
                intro()
                break
            else:
                print("Invalid input! Use the given keys.")
                print("")
                time.sleep(1)
                continue

            print("")
            print("Choose another weapon:")
            print("")
            for index, weapon in enumerate(inventory):
                print(f"{index + 1}: {weapon['Name']} (Range: {weapon['Range']}, Damage: {weapon['Damage']})")
                print("")
            weapon_choice = input("Enter the number of the weapon you want to use: ")
            print("")
            try:
                weapon_index = int(weapon_choice) - 1
                if 0 <= weapon_index < len(inventory):
                    selected_weapon = inventory[weapon_index]
                else:
                    print("Invalid weapon choice. Defaulting to the first weapon.")
                    print("")
                    selected_weapon = inventory[0]
            except ValueError:
                print("Invalid input. Defaulting to the first weapon.")
                print("")
                selected_weapon = inventory[0]

            if enemy["Health"] <= 0 or user_input == "R": #or is used to add multiple conditions to an if statement, here I use it to make sure that if the player is dead or they decide to run away that the loop is broken
                break

    if money >= 1000:
        print("")
        print("")
        print("")
        print("Congratulations! You earned $1000. You Win!")
        print("")
        print("")
        print("")


def nz():
    print("----------------------------------------")
    print("")
    print("New Zealand Quiz:")
    print("")
    time.sleep(1)

    nz_questions = [
        {"question": "What is the capital of New Zealand?", "answer": "wellington"},
        {"question": "What is the largest city in New Zealand?", "answer": "auckland"},
        {"question": "What is the Maori name for New Zealand?", "answer": "aotearoa"},
        {"question": "Which bird is the national symbol of New Zealand?", "answer": "kiwi"},
        {"question": "What is the currency of New Zealand eg.USD, CAD?", "answer": "nzd"},
        {"question": "What is the national flower of New Zealand?", "answer": "silver fern"},
        {"question": "Who was the first European explorer to reach New Zealand?", "answer": "abel tasman"},
        {"question": "What is the nickname for people from New Zealand?", "answer": "kiwi"},
        {"question": "What is the longest river in New Zealand?", "answer": "waikato river"},
        {"question": "Which New Zealand city hosted the 2011 Rugby World Cup final?", "answer": "auckland"}
    ]
    selected_questions = random.sample(nz_questions, 10)
    run_quiz(selected_questions)

def tepapa():
    print("----------------------------------------")
    print("")
    print("Te Papa Quiz:")
    print("")
    time.sleep(1)

    tepapa_questions = [
        {"question": "Te papa was built in 1983", "answer": "false"},
        {"question": "Te papa is located in Wellington", "answer": "true"},
        {"question": "Te Papa museum opened in 1998", "answer": "true"},
        {"question": "Te Papa's collections include artifacts from ancient Egypt", "answer": "true"},
        {"question": "Entry to Te Papa is always free for visitors", "answer": "true"},
        {"question": "Te Papa has live animals in their exhibits", "answer": "false"},
        {"question": "Te papa is also in Auckland?", "answer": "false"},
        {"question": "Te Papa has an earthquake simulator", "answer": "true"},
        {"question": "Te Papa has 7 floors", "answer": "false"},
        {"question": "Te Papa has a war exhibit", "answer": "true"}
    ]
    selected_questions = random.sample(tepapa_questions, 10)
    run_quiz(selected_questions)

def run_quiz(questions):
    global money
    money = 0
    for q in questions:
        print("")
        print(q["question"])
        print("")
        time.sleep(1)
        user_answer = input("Enter your answer: ").strip().lower()
        print("")
        time.sleep(1)
        if user_answer == q["answer"]:
            print("Correct! You win $100.")
            print("")
            money += 100
        else:
            print("Incorrect!")
            time.sleep(1)
    print("Total score: $", money)
    print("")
    print("")

def quiz():
    print("")
    print("")
    print("Welcome to The Ultimate Trivia!")
    print("")
    time.sleep(1)
    print("You will be asked True or False questions for Tepapa and normal questions for NZ.")
    print("")
    time.sleep(1)
    print("Each correct question will result in an award of $100")
    print("")
    time.sleep(1)
    while True:
        try:
            user_input = input("Press 'T' for Te Papa Quiz or 'N' for New Zealand Quiz").upper()
            time.sleep(1)

            if user_input == "T":
                tepapa()
                break

            elif user_input == "N":
                nz()
                break

            elif user_input == "L":
                reset_game()
                intro()
                break

            else:
                print("Invalid Input!")
                print("")
                time.sleep(1)

        except ValueError:
            print("Invalid Input!")
            print("")
            time.sleep(1)

intro() #this is used to call the intro function
