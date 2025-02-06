students = {"Harini": 95, "Elakiya": 92, "Shameera": 91, "Manju": 90, "Haseeba": 85, "Deepa":89, "Sherin": 90}
print("Ascending:", dict(sorted(students.items(), key=lambda x: x[1])))
print("Descending:", dict(sorted(students.items(), key=lambda x: x[1], reverse=True)))
print("Top 3:", dict(sorted(students.items(), key=lambda x: x[1], reverse=True)[:3]))
print("Alphabetical:", dict(sorted(students.items())))
#2
players = [("Messi", 30), ("Ronaldo", 25), ("Xavi", 20), ("Iniesta", 28), ("Falcao", 22)]
print("Goals Ascending:", sorted(players, key=lambda x: x[1]))
print("Goals Descending:", sorted(players, key=lambda x: x[1], reverse=True))
print("Top 3 Scorers:", sorted(players, key=lambda x: x[1], reverse=True)[:3])
print("Alphabetical Order:", sorted(players, key=lambda x: x[0]))
