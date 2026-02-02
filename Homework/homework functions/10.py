#10) Scrie o functie care primeste un dictionar de forma {nume: varsta} si returneaza un dictionar cu persoanele care au varsta peste 18 ani.
def filter_adults(people_dict):
    adults_dict = {}
    for name, age in people_dict.items():
        if age > 18:
            adults_dict[name] = age
    return adults_dict  

people = {
    "Alice": 30,
    "Bob": 17,
    "Charlie": 22,
    "Diana": 15,
    "Ethan": 40
}
adults = filter_adults(people)
print(adults)  # Afisează {'Alice': 30, 'Charlie': 22, 'Ethan': 40}