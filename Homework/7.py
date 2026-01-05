# 7. Afișează ultimul caracter dintr-un string introdus de la tastatură.

number_of_attempts = 0
while True and number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            print(f"Ultimul caracter din text este: '{text[-1]}'")
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1
