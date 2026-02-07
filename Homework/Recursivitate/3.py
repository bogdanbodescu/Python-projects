#3) Scrie o functie recursiva care calculeaza cate cifre are un numar dat.
#Ex: pentru 1234 returneaza 4

#Desi rezolvarea pythonica ar fi fost sa transform numarul in string si sa returnez lungimea lui.

def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)