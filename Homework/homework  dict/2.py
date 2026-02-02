#2) Afiseaza varsta unei persoane specifificate de utilizator.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
name = input("Introdu numele persoanei: ")
if name in people:
    print(f"Varsta lui {name} este {people[name]} ani.")
else:
    print("Persoana nu este in dictionar.")