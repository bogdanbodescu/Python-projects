# 11. Primește trei numere și afișează cel mai mic dintre ele.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        num1 = float(input("Introdu primul numar: "))
        num2 = float(input("Introdu al doilea numar: "))
        num3 = float(input("Introdu al treilea numar: "))
        smallest = min(num1, num2, num3)
        print(f"Cel mai mic numar este: {smallest}")
        break
    except ValueError:
        print("Te rog introdu un numar valid. Mai ai " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1