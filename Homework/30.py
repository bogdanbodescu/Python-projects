number_of_attempts = 0

while number_of_attempts < 3:
    text = input("Introdu un text: ")

    if not text:
        print("Te rog introdu un text nenul.")
        number_of_attempts += 1
        continue

    has_upper = any(char.isupper() for char in text)
    has_lower = any(char.islower() for char in text)
    has_digit = any(char.isdigit() for char in text)

    if has_upper and has_lower and has_digit:
        print("Textul are cel puțin o literă mare, una mică și o cifră.")
    else:
        print("Textul nu are cel puțin o literă mare, una mică și o cifră.")

    break