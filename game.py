'''
Adventure Game – Final Version
Author: Swornim Lamsal
Version: 1.1
'''

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []
        self.has_map = False
        self.has_lantern = False

def add_to_inventory(player, item):
    if item not in player.inventory:
        player.inventory.append(item)
        print(f"You picked up: {item}")

def show_inventory(player):
    print("Inventory:", player.inventory)

def check_win(player):
    if "treasure" in player.inventory and "rare herbs" in player.inventory:
        print(f"\nCongratulations, {player.name}! You found the treasure and rare herbs.")
        print("You have completed the adventure successfully.")
        return True
    return False

def check_lose(player):
    if player.health <= 0:
        print(f"\n{player.name}, you have lost all your health.")
        print("Game Over.")
        return True
    return False

def explore_dark_woods(player):
    print("You step into the dark woods. The trees whisper as you walk deeper.")
    add_to_inventory(player, "lantern")
    player.has_lantern = True

def explore_mountain_pass(player):
    print("You hike through the mountain pass. The cold wind bites at your skin.")
    add_to_inventory(player, "map")
    player.has_map = True

def stay_still(player):
    print("You stay still. The cold drains your energy.")
    player.health -= 10
    print(f"Health: {player.health}")

def explore_cave(player):
    print("You approach a dark cave...")
    if player.has_lantern:
        print("You light your lantern and carefully explore inside.")
        add_to_inventory(player, "treasure")
    else:
        print("It's too dark to enter safely.")
        player.health -= 10
        print(f"You stumble and hurt yourself. Health: {player.health}")

def explore_hidden_valley(player):
    print("You try to find the hidden valley...")
    if player.has_map:
        print("Using the map, you find a peaceful hidden valley.")
        add_to_inventory(player, "rare herbs")
    else:
        print("Without a map, you get lost in the forest.")
        player.health -= 10
        print(f"You wander for hours. Health: {player.health}")

def welcome_player():
    print("Welcome to the Adventure Game!")
    name = input("What is your name, adventurer? ")
    player = Player(name)
    print(f"Welcome, {player.name}! Your journey begins now.")
    return player

def describe_area():
    print("""
You find yourself in a mysterious forest.
The sound of rustling leaves surrounds you.
Paths lead in several directions...
""")

def main():
    player = welcome_player()
    describe_area()

    while True:
        print("\nWhat will you do next?")
        print("1. Explore the dark woods")
        print("2. Explore the mountain pass")
        print("3. Stay where you are")
        print("4. Search for a hidden valley")
        print("5. Stay still and listen to the forest")
        print("6. Explore a nearby cave")
        print("i. Check inventory")
        print(f"Health: {player.health}")

        choice = input("Choose an action (1-6 or i): ").lower()

        if choice == "1":
            explore_dark_woods(player)
        elif choice == "2":
            explore_mountain_pass(player)
        elif choice == "3":
            print("You wait and listen to the sounds around you.")
        elif choice == "4":
            explore_hidden_valley(player)
        elif choice == "5":
            stay_still(player)
        elif choice == "6":
            explore_cave(player)
        elif choice == "i":
            show_inventory(player)
        else:
            print("Invalid input. Please choose a number from 1 to 6 or 'i'.")

        if check_win(player) or check_lose(player):
            break

        cont = input("Do you want to continue exploring? (yes or no): ").lower()
        if cont != "yes":
            print(f"Thanks for playing, {player.name}.")
            break

if __name__ == "__main__":
    main()
