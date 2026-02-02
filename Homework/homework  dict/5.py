#5) Afiseaza varsta medie a persoanelor din dictionar.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
total_age = sum(people.values())
count = len(people)
average_age = total_age / count
print(f"Varsta medie a persoanelor este: {average_age}")