#3) Afiseaza cea mai mare si cea mai mica varsta din dictionar.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
max_age = max(people.values())
min_age = min(people.values())
print(f"Cea mai mare varsta este: {max_age}")
print(f"Cea mai mica varsta este: {min_age}")