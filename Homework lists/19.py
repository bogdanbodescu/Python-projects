# Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori

def numara_element(lista, element_cautat):
    count = 0
    for item in lista:
        if isinstance(item, list):
            count += numara_element(item, element_cautat)
        elif item == element_cautat:
            count += 1
    return count
lista = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
element_cautat = 1
aparitii = numara_element(lista, element_cautat)
print(f"Elementul {element_cautat} apare de {aparitii} ori in lista.")