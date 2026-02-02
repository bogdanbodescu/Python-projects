#17) Afiseaza persoanele sortate alfabetic dupa nume din dictionar. (Utilizati functia sorted pentru a rezolva acest exercitiu).
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
sorted_names = sorted(people.keys())
print("Persoanele sortate alfabetic dupa nume:")
for name in sorted_names:
    print(name)