#13) Scrie o functie care primeste o lista de numere si returneaza un dictionar cu frecventa fiecarui numar in lista (cheia este numarul, valoarea este frecventa).
def get_frequency_dict(numbers_list):
    frequency_dict = {}
    for num in numbers_list:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1
    return frequency_dict

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(get_frequency_dict(numbers))  # Afisează {1: 1, 2: 2, 3: 3, 4: 4}