# 21. Primește un text și afișează-l inversat.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            reversed_text = text[::-1]
            print("Textul inversat este:", reversed_text)
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1