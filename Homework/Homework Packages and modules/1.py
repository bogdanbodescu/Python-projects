#1. Sa se creeze un modul numit "operations" care sa contina functii pentru adunare, scadere, inmultire si impartire a doua numere.
#   Din fisierul principal, sa se importe modulul si sa se execute fiecare operatie cu doua numere generate aleatoriu.

import random
import operations

if __name__ == "__main__":
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    print(f"Numere generate: {num1} si {num2}")
    print(f"Adunare: {operations.adunare(num1, num2)}")
    print(f"Scadere: {operations.scadere(num1, num2)}")
    print(f"Inmultire: {operations.inmultire(num1, num2)}")
    print(f"Impartire: {operations.impartire(num1, num2)}")

