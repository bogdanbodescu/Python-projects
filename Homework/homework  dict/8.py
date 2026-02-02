#8) Afiseaza toate persoanele din dictionar in urmatorul format: "Nume: <nume_persoana>, Varsta: <varsta_persoana>".
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
for name, age in people.items():
    print(f"Nume: {name}, Varsta: {age}")