# 14. Primește un text și construiește un nou string numai cu vocalele din el.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu un text: ")
        if len(text) == 0:
            print("Te rog introdu un text nenul.")
            number_of_attempts += 1
        else:
            vowels = "aeiouAEIOU"
            vowel_string = ""
            for char in text:
                if char in vowels:
                    vowel_string += char
            print("Stringul format doar din vocale este:", vowel_string)
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1