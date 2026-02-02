#13) Creeaza un nou dictionar care sa contina doar persoanele cu varsta peste 18 ani.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
adults = {name: age for name, age in people.items() if age > 18}
print("Persoanele cu varsta peste 18 ani:")
for name, age in adults.items():
    print(f"Nume: {name}, Varsta: {age}")