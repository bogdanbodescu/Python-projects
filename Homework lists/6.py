#Înlocuiește toate aparițiile unui element dat cu altă valoare într-o listă.
#Exemplu: [1,2,3,2,4], inlocuieste 2 cu 5 -> [1,5,3,5,4]
import random 
lungime = random.randint(5, 15)
lista = [random.randint(1, 10) for _ in range(lungime)]
print("Lista generata:", lista)
try:
    veche = int(input("Introduceti elementul pe care doriti sa il inlocuiti: "))
    noua = int(input("Introduceti noua valoare: "))
except ValueError:
    print("Va rugam sa introduceti numere intregi valide.")
else:
    for i in range(len(lista)):
        if lista[i] == veche:
            lista[i] = noua
    print("Lista dupa inlocuire:", lista)
    