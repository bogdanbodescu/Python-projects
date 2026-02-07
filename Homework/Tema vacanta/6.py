# 6. Primește un text și un caracter, afișează de câte ori apare caracterul în text.
number_of_attempts = 0
while number_of_attempts < 3:
     try:
         text = input("Introdu un text: ")
         char = input("Introdu un caracter: ")
         if len(char) != 1:
             print("Te rog introdu un singur caracter.")
             number_of_attempts += 1
         else:
             count = text.count(char)
             print(f"Caracterul '{char}' apare de {count} ori in text.")
             break
     except Exception as e:
         print("A aparut o eroare: ", e)
         number_of_attempts += 1
