#1) Scrie o funcție recursivă care calculează factorialul unui număr.
#Ex: pentru n = 5, 5 x 4 x 3 x 2 x 1 = 120
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1) 