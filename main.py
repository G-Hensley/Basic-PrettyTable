# Import the PrettyTable class from the prettytable library
from prettytable import PrettyTable

# Create a new PrettyTable instance to hold our data
table = PrettyTable()

# Define the data for the table: Pokémon names and their types
pokemon = ['Pikachu', 'Squirtle', 'Charmander']
types = ["Electric", "Water", "Fire"]

# Add columns to the table using the data
table.add_column("Pokemon Name", pokemon)
table.add_column("Type", types)

# Set the alignment of the table to left for a clean look
table.align = 'l'

# Print the formatted table to the console
print(table)
