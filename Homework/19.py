# 19. Primește un număr și afișează tabla înmulțirii pentru acel număr (de la 1 la 10).
number_of_attempts = 0
while number_of_attempts < 3:
    try:
        number = int(input("Introdu un numar: "))
        print(f"Tabla inmultirii pentru {number} este:")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
        break
    except ValueError:
        print("Te rog introdu un numar valid. Mai ai " + str(2 - number_of_attempts) + " incercari.")
        number_of_attempts += 1