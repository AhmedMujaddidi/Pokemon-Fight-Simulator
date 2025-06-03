# Make a text based pokemon fight simulation.
# Use classes to define moves and Pokemon, and methods to select moves for a player and for the AI.
# You'll need a damage function to compute how much damage an attack does based on stats, types and move strength. 

import random
class Pokemon:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.max_hp = hp
        self.current_hp = hp
        self.attack = attack
        self.defense = defense
    
    def attack_opponent(self, opponent):
        damage = self.attack - opponent.defense
        if damage < 1:
            damage = 1  # Minimum 1 damage
        opponent.current_hp -= damage
        if opponent.current_hp < 0:
            opponent.current_hp = 0
        print(f"{self.name} attacks {opponent.name} for {damage} damage!")
        print(f"{opponent.name} has {opponent.current_hp} HP left")

def battle(player_pokemon, opponent_pokemon):
    print(f"\n=== BATTLE START ===")
    print(f"{player_pokemon.name} ({player_pokemon.current_hp} HP) vs {opponent_pokemon.name} ({opponent_pokemon.current_hp} HP)")
    
    while player_pokemon.current_hp > 0 and opponent_pokemon.current_hp > 0:
        # Player attacks first
        player_pokemon.attack_opponent(opponent_pokemon)
        
        # Check if opponent fainted
        if opponent_pokemon.current_hp <= 0:
            print(f"{opponent_pokemon.name} fainted! You win!")
            break
            
        # Opponent attacks back
        opponent_pokemon.attack_opponent(player_pokemon)
        
        # Check if player fainted
        if player_pokemon.current_hp <= 0:
            print(f"{player_pokemon.name} fainted! You lose!")
            break

# Give each Pokemon different stats to make them unique
pikachu = Pokemon('Pikachu', 90, 30, 15)      # Fast, high attack, low defense
charmander = Pokemon('Charmander', 100, 25, 20)  # Balanced
squirtle = Pokemon('Squirtle', 110, 20, 25)   # Tanky, high defense
bulbasaur = Pokemon('Bulbasaur', 105, 22, 22)  # Well-rounded

# Possible wild opponents
wild_opponents = [
    Pokemon('Wild Rattata', 80, 18, 12),
    Pokemon('Wild Pidgey', 75, 20, 15),
    Pokemon('Wild Geodude', 95, 22, 28),
    Pokemon('Wild Zubat', 70, 16, 10),
    Pokemon('Wild Caterpie', 60, 12, 8)
]

choice = input("Would you like to battle? ")
if choice == "yes":
    print("You have chosen to battle!")
    print("Select a Pokemon: Pikachu, Charmander, Squirtle, Bulbasaur")
    Pick = input("Pick your pokemon: ")
    if Pick.lower() == "pikachu":      
        print("You have chosen Pikachu")
    elif Pick.lower() == "charmander":  
        print("You have chosen Charmander")
    elif Pick.lower() == "squirtle":   
        print("You have chosen Squirtle")
    elif Pick.lower() == "bulbasaur":  
        print("You have chosen Bulbasaur")
    else:
        print("Invalid choice")
        exit()
else:
    print("You have chosen not to battle")
    exit()

# Random opponent appears
opponent = random.choice(wild_opponents)
print(f"A wild {opponent.name} appears!")
print(f"Your {Pick} vs {opponent.name}!")

# Get the player's chosen Pokemon object
if Pick.lower() == "pikachu":
    player_pokemon = pikachu
elif Pick.lower() == "charmander":
    player_pokemon = charmander
elif Pick.lower() == "squirtle":
    player_pokemon = squirtle
elif Pick.lower() == "bulbasaur":
    player_pokemon = bulbasaur

# Start the battle!
battle(player_pokemon, opponent)