# Interclasează două liste de aceeași lungime într-o singură listă.
# Exemplu: [1,2], [3,4] => [1,3,2,4]

import random
lungime = random.randint(5, 10)
lista1 = [random.randint(1, 100) for _ in range(lungime)]
lista2 = [random.randint(1, 100) for _ in range(lungime)]
print("Lista 1 generata:", lista1)  
print("Lista 2 generata:", lista2)
lista_interclasata = []
for i in range(lungime):
    lista_interclasata.append(lista1[i])
    lista_interclasata.append(lista2[i])
print("Lista interclasata:", lista_interclasata)