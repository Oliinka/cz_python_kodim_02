import random

word = ["w", "o", "r", "d"]
random.shuffle(word)
print(word)

# word2 = "word"
# random.shuffle(word2)
# print(word2)

muj_retezec = "ahoj"
muj_retezec = muj_retezec[0].upper() + muj_retezec[1:].lower()
# muj_retezec[0].upper() vrati novy retezec "A", 
# muj_retezec[1:].lower() vrati novy retezec "hoj"
# a pak ji slozime a zapiseme novy retezec "Ahoj" do muj_retezec
