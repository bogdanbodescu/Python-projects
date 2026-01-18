# Sa se numere de cate ori apare un element intr-o lista incluzand si listele imbricate.
# Exemplu: [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]] si elementul 1 -> apare de 4 ori

""" def numara_element(lista, element_cautat):
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
print(f"Elementul {element_cautat} apare de {aparitii} ori in lista.") """


lista = [1, 2, [3, 1, 4], 7, [1, 2, [1, 5]]]
element_cautat = 1
stiva = [(lista, 0)]
count = 0
while stiva:
    current_list, index = stiva.pop()
    while index < len(current_list):
        item = current_list[index]
        index += 1
        if isinstance(item,list):
            stiva.append((current_list,index))
            current_list = item
            index = 0
        elif item == element_cautat:
            count += 1
print(f"Elementul {element_cautat} apare de {count} ori in lista.")