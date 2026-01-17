#Primește o listă de la tastatură (elemente separate prin spațiu) și afișează lista inversată.
#Exemplu: input: 1 2 3 4 5 -> output: [5,4,3,2,1]
user_input = input("Introduceti elementele listei separate prin spatiu: ")
elements = user_input.split()
reversed_elements = elements[::-1]
print("Lista inversata:", reversed_elements)