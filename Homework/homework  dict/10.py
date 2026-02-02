#10) Actualizeaza varsta unei persoane specificate de utilizator.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
name = input("Introdu numele persoanei pe care vrei sa o verifici: ")
if name in people:
    try:
        new_age = int(input(f"Introdu noua varsta pentru {name}: "))
    except ValueError:
        print("Varsta trebuie sa fie un numar intreg.")
        exit()
    people[name] = new_age
    print(f"Varsta lui {name} a fost actualizata la {new_age} ani.")    
else:
    print(f"Persoana {name} nu exista in dictionar.")