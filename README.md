Pokémon Fight Simulation
A simple text-based Pokémon battle game built in Python where you can choose your Pokémon and battle against random wild opponents.
Features

Choose from 4 starter Pokémon: Pikachu, Charmander, Squirtle, or Bulbasaur
Each Pokémon has unique stats (HP, Attack, Defense)
Battle against random wild Pokémon opponents
Turn-based combat system
Real-time HP tracking during battles

How to Play

Run the Python script
Choose "yes" when asked if you want to battle
Select your Pokémon from the available options
A random wild Pokémon will appear as your opponent
Watch the automatic turn-based battle unfold
Win by defeating your opponent before they defeat you!

Pokémon Stats
Player Pokémon

Pikachu: 90 HP, 30 Attack, 15 Defense (Fast attacker)
Charmander: 100 HP, 25 Attack, 20 Defense (Balanced)
Squirtle: 110 HP, 20 Attack, 25 Defense (Defensive tank)
Bulbasaur: 105 HP, 22 Attack, 22 Defense (Well-rounded)

Wild Opponents

Wild Rattata: 80 HP, 18 Attack, 12 Defense
Wild Pidgey: 75 HP, 20 Attack, 15 Defense
Wild Geodude: 95 HP, 22 Attack, 28 Defense
Wild Zubat: 70 HP, 16 Attack, 10 Defense
Wild Caterpie: 60 HP, 12 Attack, 8 Defense

Game Mechanics
Battle System

Turn-based combat where player attacks first
Damage calculation: Attacker's Attack - Defender's Defense
Minimum damage is always 1 (even if defense is higher than attack)
Battle continues until one Pokémon's HP reaches 0

Combat Flow

Player's Pokémon attacks opponent
Check if opponent fainted
Opponent attacks back (if still alive)
Check if player's Pokémon fainted
Repeat until winner is determined

Future Enhancements
Potential features to add:

 Multiple moves per Pokémon
 Type effectiveness system (Fire beats Grass, etc.)
 Critical hit chances
 Status effects (poison, sleep, paralysis)
 Pokémon levels and experience
 Multiple battles in a row
 Save/load game progress
 GUI interface

Code Structure

Pokemon class: Handles Pokémon attributes and attack methods
battle() function: Manages the turn-based combat system
Main game loop: Handles user input and game flow
Random opponent selection using Python's random module

Contributing
This is a beginner-friendly project! Feel free to:

Add new features
Improve the battle system
Add more Pokémon
Enhance the user interface
Fix bugs or optimize code
