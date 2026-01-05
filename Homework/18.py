# 18. Primește un text și afișează fiecare cuvânt pe o linie nouă.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            words = text.split()
            for word in words:
                print(word)
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1