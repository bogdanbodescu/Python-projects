#6) Sterge o persoana specificata de utilizator din dictionar.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
name = input("Introdu numele persoanei pe care vrei sa o stergi: ")
if name in people:
    del people[name] # Sau people.pop(name)
    print(f"Persoana {name} a fost stearsa din dictionar.")
else:
    print("Persoana nu este in dictionar.")
print(people)