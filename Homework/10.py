# 10. Primește două numere și afișează cel mai mare dintre ele.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        num1 = float(input("Introdu primul numar: "))
        num2 = float(input("Introdu al doilea numar: "))
        if num1 > num2:
            print(f"Numarul mai mare este: {num1}")
        elif num2 > num1:
            print(f"Numarul mai mare este: {num2}")
        else:
            print("Numerele sunt egale.")
        break
    except ValueError:
        print("Te rog introdu un numar valid. Mai ai " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1