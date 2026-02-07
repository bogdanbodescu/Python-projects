# 3. Primește un nume de la tastatură și afișează-l cu litere mari.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        name = input("Introdu un nume: ")
        if len(name) == 0:
            print("Te rog introdu un nume nenul.")
            number_of_attempts += 1
        else:
            print("Numele cu litere mari este:", name.upper())
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1