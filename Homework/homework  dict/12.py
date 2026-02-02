#12) Creeaza o lista cu toate numele persoanelor din dictionar si afiseaza-le.   
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
names_list = list(people.keys())
print("Numele persoanelor din dictionar sunt:")
for name in names_list:
    print(name)