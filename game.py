'''
Adventure Game – Final Version
Author: Swornim Lamsal
Version: 1.2
'''

class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = []
        self.health = 100
        self.has_map = False
        self.has_lantern = False

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

def add_to_inventory(player, item):
    if item not in player.inventory:
        player.inventory.append(item)
        print(f"You picked up: {item}")

def show_inventory(player):
    print("Inventory:", player.inventory)

def check_win(player):
    return "treasure" in player.inventory and "rare herbs" in player.inventory

def check_lose(player):
    return player.health <= 0

# Area Functions
def explore_dark_woods(player):
    print("You step into the dark woods. Shadows stretch between ancient trees.")
    if not player.has_lantern:
        add_to_inventory(player, "lantern")
        player.has_lantern = True
    else:
        print("You’ve already explored here and found the lantern.")

def explore_mountain_pass(player):
    print("You ascend the mountain pass. The view is breathtaking.")
    if not player.has_map:
        add_to_inventory(player, "map")
        player.has_map = True
    else:
        print("You already found the map here earlier.")

def explore_cave(player):
    print("You find a narrow cave entrance hidden behind some rocks.")
    if player.has_lantern:
        print("Using your lantern, you explore the cave.")
        if "treasure" not in player.inventory:
            add_to_inventory(player, "treasure")
        else:
            print("You've already collected the treasure.")
    else:
        print("It's too dark to explore without a lantern.")
        player.health -= 10
        print(f"You stumble and get hurt. Health: {player.health}")

def explore_hidden_valley(player):
    print("You search for a hidden valley said to hold ancient secrets.")
    if player.has_map:
        print("Using your map, you navigate the forest and find the valley.")
        if "rare herbs" not in player.inventory:
            add_to_inventory(player, "rare herbs")
        else:
            print("You've already picked the rare herbs here.")
    else:
        print("You can’t find the valley without a map.")
        player.health -= 10
        print(f"You get lost and tired. Health: {player.health}")

def stay_still(player):
    print("You sit quietly, listening to the forest.")
    player.health -= 10
    print(f"You feel a bit colder and hungrier. Health: {player.health}")

def main():
    player = welcome_player()
    describe_area()

    while True:
        print("\nWhat will you do next?")
        print("1. Explore the dark woods")
        print("2. Explore the mountain pass")
        print("3. Stay still and listen to the forest")
        print("4. Search for a hidden valley")
        print("5. Explore a nearby cave")
        print("i. Check inventory")
        print(f"Health: {player.health}")

        decision = input("Choose an action (1-5 or i): ").lower()

        if decision == "1":
            explore_dark_woods(player)
        elif decision == "2":
            explore_mountain_pass(player)
        elif decision == "3":
            stay_still(player)
        elif decision == "4":
            explore_hidden_valley(player)
        elif decision == "5":
            explore_cave(player)
        elif decision == "i":
            show_inventory(player)
        else:
            print("Invalid choice. Please select a valid option.")

        if check_win(player):
            print(f"\nCongratulations, {player.name}! You've completed your quest.")
            break
        elif check_lose(player):
            print(f"\n{player.name}, you've lost all your health. Game over.")
            break

        cont = input("Do you want to continue? (yes or no): ").lower()
        if cont != "yes":
            print(f"Thanks for playing, {player.name}. Goodbye.")
            break

if __name__ == "__main__":
    main()
