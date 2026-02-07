# 9. Afișează toate caracterele unui string, câte unul pe linie.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            for char in text:
                print(char)
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1
