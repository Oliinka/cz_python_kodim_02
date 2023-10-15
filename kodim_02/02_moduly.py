# abs, round, len, sum, min, max, sorted, int, float, str, print.
import statistics

school_report = [
    ["Český jazyk", 3],
    ["Anglický jazyk", 1],
    ["Matematika", 1],
    ["Přírodopis", 2],
    ["Dějepis", 1],
    ["Fyzika", 2],
    ["Hudební výchova", 4],
    ["Výtvarná výchova", 2],
    ["Tělesná výchova", 3],
    ["Chemie", 4],
]
# statistics import statistics
print(statistics.mean([1, 2, 3, 4, 5, 6]))

list = 0
new_list = school_report["0:3"] + [school_report[5]]

print(new_list)

for item in new_list:
    if isinstance(item[1], int):
        print(item[1])






