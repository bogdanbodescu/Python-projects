# 32. Primește un text și afișează-l cu fiecare cuvânt inversat, dar în aceeași ordine. (Exemplu: "Ana are mere" -> "anA era erem")
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            words = text.split()
            reversed_words = [word[::-1] for word in words]
            result = ' '.join(reversed_words)
            print("Textul cu fiecare cuvant inversat este:", result)
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1