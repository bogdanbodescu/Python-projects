#14) Scrie o functie care primeste o lista de numere si returneaza o lista care contine numerele fara duplicate.
def remove_duplicates(numbers_list):
    unique_numbers = []
    for num in numbers_list:
        if num not in unique_numbers:
            unique_numbers.append(num)
    return unique_numbers

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(remove_duplicates(numbers))  # Afisează [1, 2, 3, 4]