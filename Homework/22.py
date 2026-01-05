# 22. Primește o propoziție și numără câte cuvinte conține.
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        sentence = input("Introdu o propozitie: ")
        if len(sentence) == 0:
            print("Te rog introdu o propozitie nenula.")
            number_of_attempts += 1
        else:
            words = sentence.split()
            print(f"Propozitia contine {len(words)} cuvinte.")
            break
    except Exception as e:
        print("A aparut o eroare: ", e)
        number_of_attempts += 1