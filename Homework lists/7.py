#Afișează elementul maxim și minim dintr-o listă fără a folosi funcțiile max/min.
#Exemplu: [3,1,4,1,5,9,2] -> max=9, min=1

import random
lungime = random.randint(20, 40)
lista = [random.randint(1, 100) for _ in range(lungime)]
print("Lista generata:", lista)
maxim = lista[0]
minim = lista[0]
for numar in lista[1::]:
    if numar > maxim:
        maxim = numar
    elif numar < minim:
        minim = numar
print("Maxim:", maxim)
print("Minim:", minim)