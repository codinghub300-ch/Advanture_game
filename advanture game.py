import random

# Define data for different locations
locations = {
    "haunted forest": {
        "enemies": ["ghost", "werewolf", "witch"],
        "weapons": ["silver sword", "crossbow", "magic light"],
        "treasures": ["enchanted ring", "glowing gem", "ancient spellbook"]
    },
    "abandoned castle": {
        "enemies": ["skeleton knight", "dark mage", "giant rat"],
        "weapons": ["flaming axe", "holy spear", "bow and arrow"],
        "treasures": ["gold crown", "royal scepter", "hidden gold chest"]
    },
    "mysterious cave": {
        "enemies": ["bat swarm", "stone golem", "lava serpent"],
        "weapons": ["torch", "pickaxe", "ice spell"],
        "treasures": ["crystal shards", "fossil relic", "diamond cluster"]
    },
    "enchanted valley": {
        "enemies": ["evil fairy", "forest spirit", "wild unicorn"],
        "weapons": ["net trap", "singing flute", "spirit orb"],
        "treasures": ["blessed flower", "star dust", "rainbow crystal"]
    }
}

# Ask the player to choose a difficulty level
def choose_difficulty():
    print("🎮 Choose your difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    while True:
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            return "Easy", (1, 6)
        elif choice == "2":
            return "Medium", (4, 8)
        elif choice == "3":
            return "Hard", (6, 10)
        else:
            print("Invalid input. Please select 1, 2, or 3.")

# Display a welcome message
def welcome_message():
    print("\n🌟 Welcome to the Multi-World Adventure Game! 🌟")
    print("Explore mysterious places, fight enemies, and collect treasures to gain points.\n")

# Let the user choose a location to explore
def choose_location():
    print("Where would you like to go?")
    for index, place in enumerate(locations.keys(), start=1):
        print(f"{index}. {place.title()}")

    while True:
        try:
            choice = int(input("\nEnter the number of the location: "))
            place = list(locations.keys())[choice - 1]
            print(f"\n🧭 You are heading into the {place.title()}...\n")
            return place
        except (ValueError, IndexError):
            print("Invalid choice. Please enter a valid number.")

# Explore the selected location based on difficulty and return the earned score
def explore_location(place, difficulty_range):
    enemies = locations[place]["enemies"]
    weapons = locations[place]["weapons"]
    treasures = locations[place]["treasures"]

    enemy = random.choice(enemies)
    weapon = random.choice(weapons)
    treasure = random.choice(treasures)


    print(f"As you explore the {place}, a wild {enemy} appears!")
    print(f"You grab {weapon} to defend yourself.")

    action = input(f"Do you want to fight the {enemy}? (yes/no): ").lower()

    round_score = 0  # Initialize score for this round

    if action == "yes":
        player_strength = random.randint(1, 10)
        enemy_strength = random.randint(*difficulty_range)

        print(f"\nYou attack with {weapon}.")
        print(f"The {enemy} strikes back!")
        print(f"Your strength: {player_strength}")
        print(f"{enemy.capitalize()}'s strength: {enemy_strength}")

        if player_strength >= enemy_strength:
            print(f"\n🎉 Victory! You defeated the {enemy} and found {treasure}!\n")
            round_score += 10
        else:
            print(f"\n💀 You were defeated by the {enemy}. No points this round.\n")
    elif action == "no":
        print(f"\nYou ran away from the {enemy}. No points earned.\n")
    else:
        print("\nInvalid response. You hesitated and lost your chance.\n")

    return round_score

# Main game loop
def play_game():
    total_score = 0
    welcome_message()

    difficulty_name, difficulty_range = choose_difficulty()
    print(f"\n🛡 Difficulty set to {difficulty_name}. Good luck!\n")

    while True:
        selected_place = choose_location()
        earned = explore_location(selected_place, difficulty_range)
        total_score += earned

        print(f"Your current total score: {total_score} 🎯\n")

        again = input("Would you like to explore another place? (yes/no): ").lower()
        if again != "yes":
            print(f"\n🏁 Game Over! Your final score: {total_score} 🏆")
            print("Thanks for playing! 👋\n")
            break

# Start the game
play_game()
