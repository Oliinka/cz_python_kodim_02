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

names_to_select = ["Český jazyk", "Matematika", "Fyzika","Anglický jazyk", "Chemie"]

# Create a new list containing the pairs with the specified names
new_list = [subject for subject in school_report if subject[0] in names_to_select]
print(new_list)

# Extract the grades and calculate their sum
grades = [pair[1] for pair in new_list]
total_sum = sum(grades)

print(f"Grades: {grades}")
# print("Grades: ", grades)
print("Total Sum:", total_sum)
print(len(grades))
print(f"Average of grades is: {total_sum/len(grades)}")