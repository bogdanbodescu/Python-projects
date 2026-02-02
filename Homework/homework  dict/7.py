#7) Afiseaza toate persoanele cu varsta peste o valoare specificata de utilizator.
people = {
    "Alice": 30,    
    "Bob": 25,
    "Charlie": 35,
    "Diana": 28,
    "Ethan": 40
}
threshold = int(input("Introdu varsta minima: "))
print("Persoanele cu varsta peste", threshold, "ani sunt:")
for name, age in people.items():
    if age > threshold:
        print(f"{name}: {age} ani")