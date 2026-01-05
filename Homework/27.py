# 27. Primește un text și afișează toate caracterele distincte din el.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            distinct_characters = set()
            for char in text:
                distinct_characters.add(char)
            print("Caracterele distincte din text sunt:", ''.join(distinct_characters))
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1