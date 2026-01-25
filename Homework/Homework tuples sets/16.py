#7) Se da lista: [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]. Eliminati duplicatele din lista,
#   astfel incat fiecare element sa apara o singura data.


lista = [1, 3, 5, 1, 6, 7, 9, 9, 1, 3, 4, 7, 1, 6, 7, 9, 5, 3, 3, 2, 1, 8, 4]
lista_fara_duplicate = list(set(lista)) 
print(lista_fara_duplicate)