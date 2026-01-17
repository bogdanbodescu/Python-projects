#10) Verifică dacă o listă este palindrom (se citește la fel de la stânga la dreapta și invers).
# Exemplu: [1,2,3,2,1] -> True, [1,2,3,4] -> False
import random
lungime = random.randint(3, 6)
lista = [random.randint(1, 10) for _ in range(lungime)]
print("Lista generata:", lista)
if lista == lista[::-1]:
    print("Lista este palindrom.")
else:
    print("Lista nu este palindrom.")