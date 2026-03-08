'''1.
a) Creeaza o clasa numita ContBancar care are:
    
atributele private: titular, sold
constructor pentru initializare
b) Adauga metodele:
    
depunere(suma) - adauga bani in cont doar daca suma este pozitiva
retragere(suma) - retrage bani doar daca exista fonduri suficiente
get_sold() - returneaza soldul curent
c) Creeaza doua obiecte de tip ContBancar si testeaza metodele.
d) Incearca sa modifici direct atributul sold din exterior si observa ce se intampla.
e) Explica de ce este util sa avem sold ca atribut privat.
'''

class ContBancar:
    def __init__(self, titular, sold=0):
        self.__titular = titular
        self.__sold = sold

    def depunere(self, suma):
        if suma > 0:
            self.__sold += suma
            print(f"Depunere reușită: {suma} lei. Sold curent: {self.__sold} lei.")
        else:
            print("Suma trebuie să fie pozitivă pentru a depune.")

    def retragere(self, suma):
        if suma > self.__sold:
            print("Fonduri insuficiente pentru retragere.")
        elif suma <= 0:
            print("Suma trebuie să fie pozitivă pentru a retrage.")
        else:
            self.__sold -= suma
            print(f"Retragere reușită: {suma} lei. Sold curent: {self.__sold} lei.")

    def get_sold(self):
        return self.__sold
    
cont1 = ContBancar("Alice", 1000)
cont2 = ContBancar("Bob", 500)
cont1.depunere(200)
cont1.retragere(150)
cont2.depunere(300)
cont2.retragere(100)
print(f"Sold cont1: {cont1.get_sold()} lei.")
print(f"Sold cont2: {cont2.get_sold()} lei.")

# Încercare de modificare directă a soldului (nu va funcționa deoarece este privat)
try:
    cont1.__sold = 5000  # Aceasta linie nu va modifica soldul real
except AttributeError as e:
    print("Eroare la modificarea soldului:", e)
    print(f"Sold cont1 după încercarea de modificare directă: {cont1.get_sold()} lei.")

# Explicație: Atributul sold este privat pentru a proteja integritatea datelor și a preveni modificări necontrolate din exterior. Dacă soldul ar fi public, oricine ar putea modifica direct valoarea acestuia, ceea ce ar putea duce la erori sau abuzuri (de exemplu, cineva ar putea seta soldul la o valoare negativă sau foarte mare fără a respecta regulile de depunere și retragere). Prin menținerea soldului ca atribut privat, putem asigura că toate modificările se fac prin metodele definite (depunere și retragere), care includ validări și reguli deafaceri pentru a menține consistența și corectitudinea datelor.