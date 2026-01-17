# Creează o listă cu 7 numere întregi, apoi afișează suma și media elementelor fara a utiliza functiile sum() si avg().
#Exemplu: [1,2,3,4,5,6,7] -> suma=28, media=4.0

import random
numbers = [random.randint(1, 100) for _ in range(7)]
total = 0   
for num in numbers:
    total += num
average = total / len(numbers)
print(f"Lista generata: {numbers}")
print(f"Suma elementelor: {total}")
print(f"Media elementelor: {average:.2f}")