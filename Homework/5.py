# 5. Verifică dacă un număr este par sau impar.
number_of_attempts = 0
while True and number_of_attempts < 3:
    try:
        number = int(input("Introdu un numar: "))
        print("Numarul este par" if not number % 2 else "Numarul este impar")
        break
    except ValueError:
        print("Te rog introdu un numar valid. Mai ai " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1