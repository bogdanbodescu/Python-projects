#9) Verifica daca o persoana specificata de utilizator exista in dictionar.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
name = input("Introdu numele persoanei pe care vrei sa o verifici: ")
if name in people:
    print(f"Persoana {name} exista in dictionar.")
else:
    print(f"Persoana {name} nu exista in dictionar.")