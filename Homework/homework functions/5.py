#5) Scrie o functie care primeste ca parametru un numar si modifica valoarea unei variabile globale cu valoarea numarului la patrat.
global_var = 0

def modify_global(number):
    global global_var
    global_var = number ** 2

modify_global(5)
print(global_var)  # Afisează 25