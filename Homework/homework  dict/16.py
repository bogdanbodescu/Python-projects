#16) Afiseaza toate persoanele grupate dupa decadele varstei (0-9, 10-19, 20-29, etc.).
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
decades = {}
for name, age in people.items():
    decade = (age // 10) * 10
    if decade not in decades:
        decades[decade] = []
    decades[decade].append(name)

for decade in sorted(decades.keys()):
    print(f"Decada {decade}-{decade + 9}: {', '.join(decades[decade])}")