'''
DOCSTRING
Adventure Game
Author: Swornim Lamsal
Version: 1.0
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
'''


# Player class to store player info and game state
class Player:
    # initializer - constructor
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

# Function: welcome_player

def welcome_player():
    # Welcome message and introduction
    print("Welcome to the Adventure Game!")  
    print('Your journey begins here... ')

    # Ask for the player's name
    name = input("What is your name, adventurer? ")
    player = Player(name)

    # Use an f-string to display the same message in a more readable way
    print(f"Welcome, {player.name}! Your journey begins now.")

    return player

# Function: describe_area
def describe_area():
    # Describe the starting area
    print("""
    You find yourself in a dark forest
    The sound of rustling leaves fills the air
    A faint path lies ahead, leading deeper into the
    unknown... """)

# Function: add_to_inventory
def add_to_inventory(player, item):
    player.inventory.append(item)
    print(f"You picked up a {item}!")


# Function to handle the player's choice to stay still
def stay_still(player):
    print("You stay still, but the cold saps your energy.")
    player.health -= 10
    print(f"Your health is now {player.health}.")

def explore_cave(player):
    print("You enter a dark cave, the air is damp and stale.")
    print("You find a treasure chest!")
    add_to_inventory(player, "treasure")
    # If player doesn't have a lantern, -10 health
    if not player.has_lantern:
        print("It's too dark to see!")
        player.health -= 10
        print(f"Your health is now {player.health}.")
    else:
        print("You can see the treasure clearly!")
        # You found rare item add to inventory
        add_to_inventory(player, "rare gem")

def check_lose(player):
    return player.health <= 0

def check_win(player):
    return "treasure" in player.inventory and "rare gem" in player.inventory


def explore_hidden_valley(player):
    print("You discover a hidden valley filled with beautiful flowers.")
    print("You feel a sense of peace and tranquility.")
    player.health += 10
    print(f"Your health is now {player.health}.")
    add_to_inventory(player, "flower")


player = welcome_player()
describe_area()


# Main game loop
while True:
    print("\nYou see paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Stay where you are.")
    print("\t4. Explore the hidden valley.")
    print("\t5. Stay still and listen to the forest.")
    print("\t6. Explore the nearby cave.")
    print("\tType 'i' to view your inventory.")
    print(f"Current Health: {player.health}")

    decision = input("What will you do (1-6 or i): ").lower()

    if decision == 'i':
        print("Inventory:", player.inventory)
        continue

    if decision == "1":
        print(f"{player.name}, you step into the dark woods. The trees whisper as you walk deeper.")
        add_to_inventory(player, "lantern")
        player.has_lantern = True

    elif decision == "2":
        print(f"{player.name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
        add_to_inventory(player, "map")
        player.has_map = True
        
    elif decision == "3":
        print("You stay still, listening to the distant sounds of the forest")
        
    elif decision == "4":
        explore_hidden_valley(player)

    elif decision == "5":
        stay_still(player)
        
    elif decision == "6":
        explore_cave(player)
        
    else: 
        print("Invalid choice. Please choose 1, 2, 3, 4, 5, 6, or i.")
    

    # Check if the player has won
    if check_win(player):
        print(f"Congratulations {player.name}, you have found the treasure and rare gem!")
        print("You are the winner!")
        print("You have conquered the forest!")
        print("You feel a sense of accomplishment.")
        break # Exit the loop and end the game

    # Check if the player has lost
    if check_lose(player):
        print(f"{player.name}, you have lost all your health!")
        print("Game Over.")
        break # Exit the loop and end the game

    # Ask if they want to continue
    play_again = input("Do you want to continue exploring? (yes or no): ").lower()
    if play_again != "yes":
        print(f"Thanks for playing, {player.name}. See you next time.")
        break # Exit the loop and end the game