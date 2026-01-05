# 17. Primește două numere și afișează toate numerele între ele (inclusiv), în ordine crescătoare.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        num1 = int(input("Introdu primul numar: "))
        num2 = int(input("Introdu al doilea numar: "))
        if num1 > num2:
            print("Primul numar trebuie sa fie mai mic sau egal cu al doilea.")
            number_of_attempts += 1
        else:
            print(f"Numerele intre {num1} si {num2} sunt:")
            for i in range(num1, num2 + 1):
                print(i)
            break
    except ValueError:
        print("Te rog introdu un numar valid. Mai ai " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1