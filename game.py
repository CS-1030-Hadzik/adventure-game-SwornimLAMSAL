'''
Adventure Game
Author: Swornim Lamsal
Version: 1.0
Description:
This is a text-based adventure game where the player explores a mysterious forest,
collects items, and makes choices that affect their journey.
'''

# Our player's backpack - starts empty but will fill up as they explore
inventory = []

def welcome_players():
    """Greets the player and gets their name for a personalized adventure"""
    # Friendly welcome messages to set the mood
    print("Welcome to the Adventure Game!")
    print('Your journey begins here... ')
    
    # Ask for the player's name - we'll use this throughout the game
    player_name = input("What is your name, adventurer? ")
    
    # Greet them personally using two different methods (showing programming options)
    print("Welcome, " + player_name + "! Your journey begins now.")  # Traditional concatenation
    print(f"Welcome, {player_name}! Your journey begins now.")      # Modern f-string (cleaner)
    
    return player_name  # Send back the name so we can use it later

def directive_auto():
    """Paints the scene of where the player starts their adventure"""
    # Multi-line string creates a vivid starting location
    starting_area = """
You find yourself in a dark forest
The sound of rustling leaves fills the air
A faint path lies ahead, leading deeper into the
unknown...
"""
    print(starting_area)  # Show this atmospheric description

def add_to_inventory(item):
    """Handles adding found items to the player's collection"""
    # Add the new item to our inventory list
    inventory.append(item)
    
    # Let the player know they successfully picked something up
    print(f"You picked up: {item}")

# ===== MAIN GAME FLOW =====

# Get the player's name and show welcome messages
player_name = welcome_players()

# Set the scene by describing the starting location
directive_auto()

# The core game loop - runs continuously until player chooses to quit
while True:
    # Present the player with their options at each turn
    print("\nYou see two paths ahead:")
    print("\t1. Take the left path into the dark woods.")
    print("\t2. Take the right path toward the mountain pass.")
    print("\t3. Check your inventory.")          # New feature - view collected items
    print("\t4. Stay where you are.")           # Option to pause and observe
    
    # Get the player's choice (will be a string "1", "2", etc.)
    decision = input("What will you do (1,2,3,4): ")

    # Handle each possible choice
    if decision == "1":
        # Left path description and consequence
        print(f"{player_name}, you step into the dark woods. The trees whisper as you walk deeper.")
        add_to_inventory("tester")  # Find a "tester" item in the woods
        
    elif decision == "2":
        # Right path description and consequence
        print(f"{player_name}, you make your way towards the mountain pass, feeling the cold wind against your face.")
        add_to_inventory("may")  # Find a "may" item on the mountain path
        
    elif decision == "3":
        # Show everything the player has collected
        print("Inventory contents:", inventory)
        
    elif decision == "4":
        # Do nothing option - just environmental description
        print("You stay still, listening to the distant sounds of the forest")
        
    else:
        # Handle invalid inputs gracefully
        print("Invalid choice. Please choose 1, 2, 3, or 4.")
   
    # After each action, check if they want to keep playing
    play_again = input("Do you want to continue exploring? (yes or no): ").lower()
    
    # If they say anything other than "yes", end the game
    if play_again != "yes":
        print(f"Thanks for playing, {player_name}. See you next time.")
        break  # Exit the game loop