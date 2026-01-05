# 25. Primește un text și afișează doar caracterele care sunt cifre.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            digit_string = ""
            for char in text:
                if char.isdigit():
                    digit_string += char
            print("Stringul format doar din cifre este:", digit_string)
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1