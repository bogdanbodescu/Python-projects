# 15. Primește un număr n și afișează toate numerele pare de la 0 la n (inclusiv).
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        n = int(input("Introdu un numar: "))
        if n < 0:
            print("Te rog introdu un numar nenegativ.")
            number_of_attempts += 1
        else:
            print(f"Numerele pare de la 0 la {n} sunt:")
            for i in range(0, n + 1, 2):
                print(i)
            break
    except ValueError:
        print("Te rog introdu un numar valid. Mai ai " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1