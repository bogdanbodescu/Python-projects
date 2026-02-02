#18) Afiseaza persoanele sortate dupa varsta, de la cea mai mica la cea mai mare. (Utilizati functia sorted pentru a rezolva acest exercitiu).
 #  (Folositi functia sorted() si pentru cheia de sortare (key) accesati valorile dictionarului).
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}

def sort_key(item):
    return item[1]   # vârsta

sorted_by_age = sorted(people.items(), key=sort_key)

print("Persoanele sortate dupa varsta, de la cea mai mica la cea mai mare:")
for name, age in sorted_by_age:
    print(f"Nume: {name}, Varsta: {age}")