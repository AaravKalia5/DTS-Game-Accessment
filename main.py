import random
import time

# Generate random attributes for weapons
all_weapons = [
    {"Name": "Knife", "Range": 1, "Damage": random.randint(6, 15)},
    {"Name": "AK47", "Range": 140, "Damage": random.randint(40, 100)},
    {"Name": "Rifle", "Range": 180, "Damage": random.randint(30, 70)},
    {"Name": "Glock", "Range": 50, "Damage": random.randint(40, 90)},
    {"Name": "Hammer", "Range": 2, "Damage": random.randint(5, 10)}
]

# Generate random attacks for enemies
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

# Define enemy types with their attributes
enemy_hash = [
    {"Name": "Mr. Lacelles", "Type": "Computer", "Level": 1, "Attacks": lacelle_attacks_hash,
     "Health": random.randint(20, 100)},
    {"Name": "Mr. Denham", "Type": "Boss", "Level": 2, "Attacks": denham_attacks_hash,
     "Health": random.randint(20, 100)},
    {"Name": "Mr. Corliss", "Type": "Math", "Level": 1, "Attacks": corliss_attacks_hash,
     "Health": random.randint(20, 100)}
]

# Initialize player's attributes
player_health = 0
money = 0
inventory = []

# Define functions

def player_setup():
    global player_health
    print("Welcome to Te-Papa Wellington!")
    print("")
    player_name = input("What would you like to name your player? : ")
    print("")
    player_age = int(input("How old is your in-game player? : "))
    print("")
    if player_age < 10:
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
    print("")
    print("Your player is called", player_name, "and has", player_health, "health.")
    print("")

def find_weapons():
    print("")
    print("")
    print("You found 3 unique weapons:")
    print("")
    time.sleep(1)
    for _ in range(3):
        weapon = random.choice(all_weapons)
        while weapon in inventory:  # Ensure uniqueness of weapons
            weapon = random.choice(all_weapons)
        inventory.append(weapon)
        print("")
        print("")
        print("Name:", weapon["Name"])
        print("Range:", weapon["Range"])
        print("Damage:", weapon["Damage"])
        print("")
        time.sleep(1)

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
            money += enemy["Attacks"][0]["Rewards"]  # Assume all attacks have the same reward
            print("Total $", money)
            print("")
            print("")
            time.sleep(1)
            return True
        else:
            print("")
            print(enemy["Name"], "has", enemy["Health"], "health left.")
            print("")

            time.sleep(1)
            return False
    else:
        print("")
        print("Enemy is out of range!")
        print("")
        time.sleep(1)
        return False

def run_away():
    print("")
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
        print("")
        skip = input("Press 'S' to skip intro or press 'A' to continue : ").upper()
        print("")
        if skip == "S":
            map()
            break
        elif skip == "A":
            context()
            break
        else:
            print("")
            print("Please use 'A' or 'S'")
            print("")
            time.sleep(1)

def context():
    print("")
    print("")
    print("Welcome to Te-Papa Wellington!")
    print("")
    time.sleep(1)
    print("A huge tornado hit Wellington last week.")
    print("")
    time.sleep(1)
    print("Te-Papa has been crushed by the tornado.")
    print("")
    time.sleep(1)
    print("To rebuild Te-Papa, you will have to earn $100,000.")
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
    print("You are currently standing at Te-Papa, and there are 5 mini-games in total.")
    print("")
    print("")
    print("")
    time.sleep(1)
    while True:
        print("")
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
        else:
            print("")
            print("Please use 'R' or 'A'")
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
        print("")
        user_input = input("What area would you like to go to? : ").upper()
        print("")
        print("")
        if user_input == "A":
            rpg()
            break

        elif user_input == "B":
            quiz()
            break

        else:
            print("")
            print("Invalid area!")
            print("")
            time.sleep(1)

def rpg():
    print("")
    print("")
    print("Welcome to the RPG Shooter")
    print("")
    time.sleep(1)
    print("Each battle is worth $50")
    print("")
    time.sleep(1)
    print("")
    time.sleep(1)
    while True:
        print("")
        user_input = input("Press 'A' to start: ").upper()
        print("")
        if user_input == "A":
            find_weapons()
            rpg_real_fights()
            break
        else:
            print("")
            print("Please Enter 'A' to Start")
            print("")
            time.sleep(1)


def rpg_real_fights():
    global money
    while money < 1000:

        enemy = random.choice(enemy_hash)
        enemy_distance = random.randint(1, 90)

        enemy["Health"] = random.randint(20, 100)
        print("")
        for attack in enemy["Attacks"]:
            attack["Damage"] = random.randint(5, 15)
            attack["Range"] = random.randint(1, 60)
        print("")
        print("You have spotted", enemy["Name"], "\nAttack :", enemy["Attacks"][0]["Name"], "\nDamage :",
              enemy["Attacks"][0]["Damage"], "\nRange :", enemy["Attacks"][0]["Range"], "\nDistance :",
              enemy_distance)
        print("")
        time.sleep(1)


        print("")
        print("Choose a weapon:")
        print("")
        for index, weapon in enumerate(inventory):
            print(f"{index + 1}: {weapon['Name']} (Range: {weapon['Range']}, Damage: {weapon['Damage']})")
            print("")
            print("")
        weapon_choice = input("Enter the number of the weapon you want to use: ")
        print("")
        try:
            weapon_index = int(weapon_choice) - 1
            if 0 <= weapon_index < len(inventory):
                selected_weapon = inventory[weapon_index]
            else:
                print("")
                print("Invalid weapon choice. Defaulting to the first weapon.")
                print("")
                selected_weapon = inventory[0]
        except ValueError:
            print("")
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
                        print("")
                        print("No weapon with sufficient range to attack. Choose another weapon.")
                        print("")
                else:
                    print("")
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
            else:
                print("")
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
                    print("")
                    print("Invalid weapon choice. Defaulting to the first weapon.")
                    print("")
                    selected_weapon = inventory[0]
            except ValueError:
                print("")
                print("Invalid input. Defaulting to the first weapon.")
                print("")
                selected_weapon = inventory[0]

            if enemy["Health"] <= 0 or user_input == "R":
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
    print("")
    print("----------------------------------------")
    print("")
    print("New Zealand Quiz:")
    print("")
    # Add your New Zealand quiz questions and logic here
    nz_questions = [
        {"question": "What is the capital of New Zealand?", "answer": "wellington"},
        {"question": "What is the largest city in New Zealand?", "answer": "auckland"},
        {"question": "What is the Maori name for New Zealand?", "answer": "aotearoa"},
        {"question": "Which bird is the national symbol of New Zealand?", "answer": "kiwi"},
        {"question": "What is the currency of New Zealand?", "answer": "new zealand dollar"},
        {"question": "What is the national flower of New Zealand?", "answer": "silver fern"},
        {"question": "Who was the first European explorer to reach New Zealand?", "answer": "abel tasman"},
        {"question": "What is the nickname for people from New Zealand?", "answer": "kiwi"},
        {"question": "What is the longest river in New Zealand?", "answer": "waikato river"},
        {"question": "Which New Zealand city hosted the 2011 Rugby World Cup final?", "answer": "auckland"}
    ]
    selected_questions = random.sample(nz_questions, 10)
    run_quiz(selected_questions)

def tepapa():
    print("")
    print("----------------------------------------")
    print("")
    print("Te Papa Quiz:")
    print("")
    # Add your Te Papa quiz questions and logic here
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
        user_answer = input("Enter your answer: ").strip().lower()
        print("")
        if user_answer == q["answer"]:
            print("")
            print("Correct! You win $100.")
            print("")
            money += 100
        else:
            print("Incorrect!")
    print("Total score: $", money)
    print("")
    print("")

def quiz():
    print("")
    print("")
    print("Welcome to The Ultimate Trivia!")
    print("")
    print("You will be asked True or False questions.")
    print("")
    print("Each correct question will result in an award of $100")
    print("")
    while True:
        try:
            user_input = input("Press 'T' for Te Papa Quiz or 'N' for New Zealand Quiz").upper()

            if user_input == "T":
                tepapa()
                break

            elif user_input == "N":
                nz()
                break

            else:
                print("")
                print("Invalid Input!")
                print("")

        except ValueError:
            print("")
            print("Invalid Input!")
            print("")

intro()
