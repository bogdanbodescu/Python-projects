#3) Scrie o funcție care primește două numere și returnează suma, diferența și produsul lor (returnează un tuple).
def calculate_operations(a, b):
    return (a + b, a - b, a * b)

result = calculate_operations(10, 5)
print("Suma:", result[0])
print("Diferența:", result[1])
print("Produsul:", result[2])