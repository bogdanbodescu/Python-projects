#9) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza numele persoanei cu cea mai mica varsta.
def get_youngest_person(people_dict):
    min_age = float('inf')
    youngest_person = None
    for name, age in people_dict.items():
        if age < min_age:
            min_age = age
            youngest_person = name
    return youngest_person

people = {"Alice": 30, "Bob": 25, "Charlie": 35}
print(get_youngest_person(people))  # Afisează "Bob"