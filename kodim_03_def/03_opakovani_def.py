
import random

# nahodny generator cisel v zadaném rozsahu

points = random.randint(0, 100)
random_points = points
print(f"You scored {points} points.")

def get_mark(points):
    if points <= 60:
        mark = 5
    elif points <= 70:
        mark = 4
    elif points <= 80:
        mark = 3
    elif points <= 90:
        mark = 2
    else:
        mark = 1
    return mark

# print((f"Your mark is {get_mark(points)}."))

mark = get_mark(points)
if mark == 5:
    points = int(input("Zadej počet bodů v opravném pokusu: "))
    mark = get_mark(points)
print(f"Výsledná známka je {mark}.")