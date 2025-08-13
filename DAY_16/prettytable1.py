from prettytable import PrettyTable


# MODULE            #CLASS

table = PrettyTable()
# OBJ.    #FROM CLASS

table.add_column("crickter", ["virat", "dhoni", "boult"])
table.add_column("type", ["batsman", "wicket keeper", "bowler"])

print(table.align)

print(table)
