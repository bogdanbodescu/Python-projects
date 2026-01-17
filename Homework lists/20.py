# Scrieti un program care sa genereze un numar aleator intre 1 si 100. Utilizatorul trebuie sa
#ghiceasca numarul, iar programul sa ii ofere indicatii daca numarul introdus este mai mare sau mai mic decat cel generat.
#Programul se termina cand utilizatorul ghiceste numarul corect sau daca introduce cuvantul exit. La final se afiseaza numarul de incercari facute.

import random   
numar_aleator = random.randint(1, 100)
incercari = 0
print("Am generat un numar intre 1 si 100. Incearca sa-l ghicesti! (scrie 'exit' pentru a iesi)")
while True:
    user_input = input("Introdu numarul tau: ")
    if user_input.lower() == 'exit':
        print(f"Ai iesit din joc. Numarul era {numar_aleator}. Numarul de incercari: {incercari}.")
        break
    try:
        ghicire = int(user_input)
    except ValueError:
        print("Te rog sa introduci un numar valid sau 'exit' pentru a iesi.")
        continue
    incercari += 1
    if ghicire < numar_aleator:
        print("Numarul este mai mare.")
    elif ghicire > numar_aleator:
        print("Numarul este mai mic.")
    else:
        print(f"Felicitari! Ai ghicit numarul {numar_aleator} in {incercari} incercari.") #ar trebui sa verific daca incercari == 1 pentru a afisa "incercare" la singular   
        break