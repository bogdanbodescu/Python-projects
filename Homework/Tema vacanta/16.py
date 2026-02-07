# 16. Primește un text și afișează doar literele mici din el.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            lower_case_string = ""
            for char in text:
                if char.islower():
                    lower_case_string += char
            print("Stringul format doar din litere mici este:", lower_case_string)
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1