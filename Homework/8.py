# 8. Primește un număr și afișează dacă este pozitiv, negativ sau zero.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        number = int(input("Introdu un numar: "))
        if number > 0:
            print("Numarul este pozitiv")
        elif number < 0:
            print("Numarul este negativ")
        else:
            print("Numarul este zero")
        break
    except ValueError:
        print("Te rog introdu un numar valid. Mai ai " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1