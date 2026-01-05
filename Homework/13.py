# 13. Primește o parolă și verifică dacă are cel puțin 8 caractere și conține o cifră.
number_of_attempts = 0
while number_of_attempts < 3:     
    try:
        password = input("Introdu o parola: ")
        if len(password) < 8:
            print("Parola trebuie sa aiba cel putin 8 caractere.")
            number_of_attempts += 1
            continue
        if not any(char.isdigit() for char in password):
            print("Parola trebuie sa contina cel putin o cifra.")
            number_of_attempts += 1
            continue
        print("Parola este valida.")
        break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1