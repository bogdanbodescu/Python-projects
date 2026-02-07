# 23. Primește un text și înlocuiește toate spațiile cu caracterul "_".
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            replaced_text = text.replace(" ", "_")
            print("Textul cu spațiile înlocuite este:", replaced_text)
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1