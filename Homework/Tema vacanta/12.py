# 12. Primește un text și verifică dacă este palindrom.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            if text.lower() == text[::-1].lower():
                print("Textul este palindrom.")
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1