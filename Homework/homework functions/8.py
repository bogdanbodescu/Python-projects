#8) Scrie o funcție care primește doua liste de numere si returneaza o lista cu numerele comune celor doua liste.
def get_common_numbers(list1, list2):
    common = []
    for num in list1:
        if num in list2 and num not in common:
            common.append(num)
    return common

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]
print(get_common_numbers(list_a, list_b))  # Afisează [3, 4, 5]