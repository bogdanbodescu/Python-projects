# Primește o listă de stringuri și construiește o nouă listă cu stringurile care conțin litera 'a'.
#Exemplu: ['ana', 'mere', 'casa', 'masina'] -> ['ana', 'casa', 'masina']
elements = ['ana', 'mere', 'casa', 'masina']
lista_cu_a = [element for element in elements if 'a' in element]
print("Lista cu stringuri care contin litera 'a':", lista_cu_a)