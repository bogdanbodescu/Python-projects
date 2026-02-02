#12) Scrie o functie care primeste o lista de numere si returneaza cel mai mic numar, cel mai mare numar si media aritmetica a numerelor din lista.
def get_min_max_avg(numbers_list):
    if not numbers_list:
        return None, None, None
    min_num = min(numbers_list)
    max_num = max(numbers_list)
    avg = sum(numbers_list) / len(numbers_list)
    return min_num, max_num, avg

numbers = [1, 2, 3, 4, 5]
min_val, max_val, avg_val = get_min_max_avg(numbers)
print(f"Min: {min_val}, Max: {max_val}, Average: {avg_val}")