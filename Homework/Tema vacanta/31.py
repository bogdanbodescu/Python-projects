# 31. Fizz Buzz: Primește un număr n și afișează numerele de la 1 la n. Pentru multiplii de 3, afișează "Fizz", pentru multiplii de 5, afișează "Buzz", iar pentru multiplii de ambele, afișează "FizzBuzz".
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        n = int(input("Introdu un numar: "))
        if n <= 0:
            print("Te rog introdu un numar pozitiv.")
            number_of_attempts += 1
        else:
            for i in range(1, n + 1):
                if i % 3 == 0 and i % 5 == 0:
                    print("FizzBuzz")
                elif i % 3 == 0:
                    print("Fizz")
                elif i % 5 == 0:
                    print("Buzz")
                else:
                    print(i)
            break
    except ValueError:
        print("Te rog introdu un numar intreg.")
        number_of_attempts += 1
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1