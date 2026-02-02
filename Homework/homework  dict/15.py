#15) Afiseaza persoana cu cea mai apropiata varsta de o valoare specificata de utilizator.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
target_age = int(input("Introdu varsta dorita: "))
closest_person = None
min_diff = float('inf')

for name, age in people.items():
    diff = abs(age - target_age)
    if diff < min_diff:
        min_diff = diff
        closest_person = name

print(f"Persoana cu varsta cea mai apropiata de {target_age} ani este {closest_person} cu varsta de {people[closest_person]} ani.")