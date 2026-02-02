#14) Creeaza o lista care contine toate varstele din dictionar, fara duplicate, si afiseaz-o.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
ages_list = list(set(people.values()))
print("Varstele din dictionar, fara duplicate:")
for age in ages_list:
    print(age)