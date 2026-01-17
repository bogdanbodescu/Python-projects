#Afișează toate elementele de pe poziții impare dintr-o listă dată.
#Exemplu: [10,20,30,40,50,60] -> 20,40,60
import random
lungime = random.randint(5, 20)
lista = [random.randint(1, 100) for _ in range(lungime)]
print("Lista generata:", lista)
print("Elementele de pe pozitii impare:")
for i in range(1, len(lista), 2):
    print(lista[i])