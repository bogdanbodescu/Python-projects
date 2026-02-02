#15) Scrie o functie care primeste o lista de numere si returneaza o lista doar cu numerele prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(numbers_list):
    primes_list = []
    for num in numbers_list:
        if is_prime(num):
            primes_list.append(num)
    return primes_list

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(get_primes(numbers))  # Afisează [2, 3, 5, 7, 11]