# 33. Primește un text care contine o insiruire de numere și afișează media lor. (Exemplu: "1,2,3,4,5,10" -> 25/6 = 4.1666)
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        text = input("Introdu o insiruire de numere separate prin virgula: ")
        if len(text) == 0:
            print("Te rog introdu o insiruire nenula.")
            number_of_attempts += 1
        else:
            numbers = text.split(',')
            numbers = [float(number) for number in numbers]
            print(f"Media numerlor este: {sum(numbers)/len(numbers)}")
    except ValueError:
        print("Te rog introdu doar numere valide separate prin virgula. Mai ai " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1