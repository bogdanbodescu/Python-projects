# Primește o listă de numere și grupează elementele în două liste: una cu numere negative, alta cu numere pozitive și zero.
# Exemplu: [10,-1,2,-3,0,4,-5] -> negative: [-1,-3,-5], pozitive_si_zero: [10,2,0,4]
import random
lungime = random.randint(10, 20)
lista = [random.randint(-10, 10) for _ in range(lungime)]
print("Lista generata:", lista)
lista_negative = []
lista_pozitive_si_zero = []
for numar in lista:
    if numar < 0:
        lista_negative.append(numar)
    else:
        lista_pozitive_si_zero.append(numar)
print("Lista cu numere negative:", lista_negative)
print("Lista cu numere pozitive si zero:", lista_pozitive_si_zero)