# 24. Primește un număr și afișează suma cifrelor sale.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        number = int(input("Introdu un numar: "))
        suma_cifrelor = sum(int(cifra) for cifra in str(abs(number)))
        print(f"Suma cifrelor numarului {number} este: {suma_cifrelor}")
        break
    except ValueError:
        print("Te rog introdu un numar valid. Mai ai " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1