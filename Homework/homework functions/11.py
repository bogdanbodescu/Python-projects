#11) Scrie o functie care primeste o lista de numere si un numar n, si returneaza o lista cu numerele mai mici decat n.
def get_numbers_less_than(numbers_list, n):
    less_than_list = []
    for num in numbers_list:
        if num < n:
            less_than_list.append(num)
    return less_than_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 5
print(get_numbers_less_than(numbers, n))  # Afisează [1, 2, 3, 4]