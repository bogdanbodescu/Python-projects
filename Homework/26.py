# 26. Primește un text și verifică dacă începe și se termină cu aceeași literă.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            if text[0].lower() == text[-1].lower():
                print("Textul începe și se termină cu aceeași literă.")
            else:
                print("Textul nu începe și nu se termină cu aceeași literă.")
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1