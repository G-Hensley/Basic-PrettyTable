from prettytable import PrettyTable
table = PrettyTable()
pokemon = ['Pikachu', 'Squirtle', 'Charmander']
types = ["Electric", "Water", "Fire"]
table.add_column("Pokemon Name", pokemon)
table.add_column("Type", types)
table.align = 'l'
print(table)