# 29. Primește un număr n și afișează toți divizorii săi.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        n = int(input("Introdu un număr: "))
        if n <= 0:
            print("Te rog introdu un număr pozitiv.")
            number_of_attempts += 1
        else:
            divisors = []
            for i in range(1, n//2 + 1):
                if not n % i:
                    divisors.append(i)
            divisors.append(n)
            print(f"Divizorii lui {n} sunt: {divisors}")
            break
    except ValueError:
        print("Te rog introdu un număr întreg.")
        number_of_attempts += 1
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1