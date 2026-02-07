# 28. Primește un text și afișează literele care apar de exact două ori.
number_of_attempts = 0
while number_of_attempts < 3: 
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            letter_count = {}
            for char in text:
                if char.isalpha():
                    if char in letter_count:
                        letter_count[char] += 1
                    else:
                        letter_count[char] = 1
            letters_twice = [char for char, count in letter_count.items() if count == 2]
            print("Literele care apar de exact două ori sunt:", ''.join(letters_twice))
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1