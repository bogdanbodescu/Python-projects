#Primește o listă de stringuri și sorteaz-o crescător după numărul de vocale din fiecare string.
#Fara a folosi functia sort() sau sorted().
# Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'mere', 'masina']

def numara_vocale(s):
    vocale = 'aeiouAEIOU'
    return sum(1 for char in s if char in vocale)
elements = ['ana', 'mere', 'casa', 'masina', 'elefant', 'urs', 'iepure']
print("Lista initiala:", elements)
for i in range(len(elements)):
    for j in range(i + 1, len(elements)):
        if numara_vocale(elements[i]) > numara_vocale(elements[j]):
            elements[i], elements[j] = elements[j], elements[i]
print("Lista sortata dupa numarul de vocale:", elements)