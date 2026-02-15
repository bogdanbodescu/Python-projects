#2. Sa se scrie un program care citeste un fisier text numit "date.txt" si afiseaza numarul de linii, cuvinte si caractere din fisier.

with open("date.txt", "r") as file:
    continut = file.read()
    numar_linii = continut.count("\n") + 1  # Adaugam 1 pentru ultima linie care nu are \n
    numar_cuvinte = len(continut.split())
    numar_caractere = len(continut)
print(f"Numar linii: {numar_linii}")
print(f"Numar cuvinte: {numar_cuvinte}")
print(f"Numar caractere: {numar_caractere}")
file.close()