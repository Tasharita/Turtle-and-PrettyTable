from prettytable import PrettyTable

table1 = PrettyTable()

#adding column by column
table1.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table1.add_column("Type", ["Electric","Water","Fire"])

print(table1)

table2 = PrettyTable()
#adding by rows
table2.field_names = ["Pokemon Name","Type"]
table2.add_rows(
    [["Pikachu","Electric"],["Squirtle","Water"],["Charmander","Fire"]])

table2.align = "l" #aligns table contents to the left

print(table2)