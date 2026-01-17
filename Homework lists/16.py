# Primește o listă de liste (matrice) și calculează suma elementelor de pe diagonala principală (doar dacă matricea este pătratică).
# Exemplu: [[1,2,3],[4,5,6],[7,8,9]] -> 15 (1+5+9)

#generare matrice aleatoare
import random
n = random.randint(2, 5)  # Numar linii
m = random.randint(2, 5)  # Număr coloane
matrice = [[random.randint(1, 10) for _ in range(m)] for _ in range(n)]
print("Matricea generata:")
for row in matrice:
    print(row)

#verificare daca matricea este patrata
flag = True
for _ in range(n):
    if len(matrice[_]) != n:
        print("Matricea nu este patrata. Nu se poate calcula suma diagonalei principale.")
        flag = False
        break
#Daca este patrata, calculam suma diagonalei principale
if flag:
    suma_diagonala = 0
    for _ in range(n):
        suma_diagonala += matrice[_][_]
    print("Suma elementelor de pe diagonala principala:", suma_diagonala)

#nu am verificat daca n == m, am vrut sa verific fiecare linie in parte (pentru ca am usurat generarea matricei insa nu m-am folosit de acest lucru ca sa pastrez algoritmul sa mearga pe orice matrice introdusa)