# 2. Afișează produsul a două numere introduse de la tastatură.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        nr1 = input("Introdu primul numar: ")
        nr2 = input("Introdu al doilea numar: ")

        print(float(nr1) * float(nr2))
        break
    except ValueError:
        print(f"Te rog introdu numere valide. Mai ai  " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1