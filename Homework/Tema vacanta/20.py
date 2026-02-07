# 20. Primește un text și verifică dacă toate caracterele sunt litere mici.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            if text.islower():
                print("Toate caracterele sunt litere mici.")
            else:
                print("Nu toate caracterele sunt litere mici.")
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1