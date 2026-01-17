#Primește o listă de numere și elimină toate elementele care apar de mai mult de o dată (păstrează doar elementele unice).
#Fara a folosi set(). - fun police detected
# Exemplu: [1,2,2,3,4,4,5] -> [1,3,5]

import random
lungime = random.randint(10, 20)
lista = [random.randint(1, 10) for _ in range(lungime)]
print("Lista generata:", lista)
lista_unice = []
for numar in lista:
    if lista.count(numar) == 1:
        lista_unice.append(numar)
print("Lista cu elemente unice:", lista_unice)