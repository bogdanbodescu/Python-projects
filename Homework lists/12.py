#Creează o listă de liste [index, valoare] pentru fiecare element dintr-o listă dată.
# Exemplu: [10,20,30] -> [[0,10],[1,20],[2,30]]

import random
lungime = random.randint(5, 15)
lista = [random.randint(1, 100) for _ in range(lungime)]
print("Lista generata:", lista)
lista_index_valoare = []
for index, valoare in enumerate(lista):
    lista_index_valoare.append([index, valoare])
print("Lista de liste [index, valoare]:", lista_index_valoare)