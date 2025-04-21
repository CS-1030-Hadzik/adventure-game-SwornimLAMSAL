"""
Adventure Game
Author: Swornim Lamsal
Version: 1.1
Description:
This is a text-based adventure game where the player makes choices
to navigate through a mysterious forest.
"""


# Inventory list to store items collected by the player
inventory = []

# Function to welcome the player
def welcome_player():
    print("Welcome to the Adventure Game!")
    print("Your journey begins here...")
    name = input("What is your name, adventurer? ")
    print(f"Welcome, {name}! Your journey begins now.")
    return name

# Function to describe the starting area
def describe_area():
    print("""
You find yourself in a dark forest...
The sound of rustling leaves fills the air.
A faint path lies ahead, leading deeper into the unknown...
""")

# Function to add an item to the inventory and print a message
def add_to_inventory(item):
    if item not in inventory:
        inventory.append(item)
        print(f"You picked up a {item}!")
    else:
        print(f"You already have the {item}.")

# Main function to run the game
def main():
    # Welcome the player and store their name
    player_name = welcome_player()
    
    # Describe the area the player finds themselves in
    describe_area()

    # Start the game loop
    while True:
        # Present the player with options
        print("\nYou see two paths ahead:")
        print("    1. Take the left path into the dark woods.")
        print("    2. Take the right path toward the mountain pass.")
        print("    3. Stay where you are.")
        print("    Type 'i' to view your inventory.")

        choice = input("What will you do (1, 2, 3, or i): ").lower()

        if choice == "1":
            print(f"{player_name}, you step into the dark woods...")
            add_to_inventory("lantern")  # Add a lantern to the inventory
        elif choice == "2":
            print(f"{player_name}, you head toward the mountain pass...")
            add_to_inventory("map")  # Add a map to the inventory
        elif choice == "3":
            print(f"{player_name}, you decide to stay where you are.")
        elif choice == "i":
            # Show the player's inventory
            print(f"Inventory: {inventory}")
        else:
            print("Invalid choice. Please select 1, 2, 3, or i.")

# Run the game
if __name__ == "__main__":
    main()
