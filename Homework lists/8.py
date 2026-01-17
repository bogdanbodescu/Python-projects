#Elimină toate elementele pare dintr-o listă de numere.
#Exemplu: [1,2,3,4,5,6] -> [1,3,5]
import random
lungime = random.randint(10, 20)
lista = [random.randint(1, 100) for _ in range(lungime)]
print("Lista generata:", lista)
lista_fara_pare = [numar for numar in lista if numar % 2 != 0]
print("Lista dupa eliminarea numerelor pare:", lista_fara_pare)