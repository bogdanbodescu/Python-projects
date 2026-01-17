# Sa se scrie un program primeste date in urmatorul format: "Nume: Ionescu Prenume: Ion" pana cand se introduce
#caracterul #. Programul trebuie sa stocheze toate datele citite, iar la final sa le afiseze in ordine alfabetica
#in functie de numele de familie.

date_persoane = []
while True:
    intrare = input("Introduceti datele in formatul 'Nume: Ionescu Prenume: Ion' sau '#' pentru a termina: ")
    if intrare.strip() == '#':
        break
    try:
        parti = intrare.split()
        nume_index = parti.index("Nume:") + 1
        prenume_index = parti.index("Prenume:") + 1
        nume = parti[nume_index][0].upper() + parti[nume_index][1:].lower()
        prenume = parti[prenume_index][0].upper() + parti[prenume_index][1:].lower()
        date_persoane.append((nume, prenume))
    except (ValueError, IndexError):
        print("Format invalid. Va rugam sa respectati formatul 'Nume: Ionescu Prenume: Ion'.")
date_persoane.sort()
for nume, prenume in date_persoane:
    print(f"Nume: {nume}, Prenume: {prenume}")