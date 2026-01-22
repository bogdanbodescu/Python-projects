# Sa se afiseze toate puterile lui 2 aflate intre un interval dat de utilizator.
# Exemplu: 10, 50 -> 16, 32

while True:
    try:
        start = int(input("Introduceti limita inferioara a intervalului: "))
        end = int(input("Introduceti limita superioara a intervalului: "))
    except ValueError:
        print("Va rugam sa introduceti numere intregi valide.")
        break
    if end < 0:
        print("Limita superioara trebuie sa fie un numar pozitiv.")
        break
    if start >= end:
        print("Limita inferioara trebuie sa fie mai mica decat limita superioara.")
        break 
    print(f"Puterile lui 2 intre {start} si {end} sunt:")
    power = 1   
    while power < start:
        power *= 2
    while power <= end:
        print(power)
        power *= 2
    break           