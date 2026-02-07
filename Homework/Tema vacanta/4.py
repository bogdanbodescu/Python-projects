# 4. Afișează lungimea unui string introdus de la tastatură.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            print(f"Lungimea textului este: {len(text)}")
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1
