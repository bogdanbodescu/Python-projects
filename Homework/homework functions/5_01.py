#5) Scrie o funcție care primește o listă de numere și returnează suma tuturor numerelor.
def sum_numbers(numbers_list):
    total = 0
    for num in numbers_list:
        total += num
    return total

numbers = [1, 2, 3, 4, 5]
print(sum_numbers(numbers))