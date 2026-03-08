'''
3.
a) Creeaza o clasa numita "Persoana" care are atributele "nume", "varsta" si "gen".
b) Creeaza o lista de 5 persoane si afiseaza numele si varsta fiecarei persoane din lista.
c) Adauga o metoda numita "introducere" in clasa "Persoana" care returneaza o introducere a persoanei (ex: "Numele meu este X, am Y ani si sunt de gen Z"). Apeleaza aceasta metoda pentru fiecare persoana din lista.
d) Creeaza o metoda numita "este_major" care returneaza True daca persoana are varsta de 18 ani sau mai mult, si False in caz contrar. Apeleaza aceasta metoda pentru fiecare persoana din lista si afiseaza daca fiecare persoana este major sau nu.
e) Creeaza o metoda numita "schimba_gen" care schimba genul persoanei (ex: daca genul este "masculin", il schimba in "feminin" si invers). Apeleaza aceasta metoda pentru fiecare persoana din lista si afiseaza noul gen al fiecarei persoane.
f) Creeaza o metoda numita "adauga_ani" care adauga un numar specificat de ani la varsta persoanei. Apeleaza aceasta metoda pentru fiecare persoana din lista, adaugand un numar aleator de ani si afiseaza noua varsta a fiecarei persoane.
g) Afiseaza o lista cu toate persoanele care sunt majore.
h) Afiseaza o lista cu toate persoanele care au genul "masculin" si au peste 14 ani.'''

class Persoana:
    def __init__(self, nume, varsta, gen):
        self.nume = nume
        self.varsta = varsta
        self.gen = gen

    def introducere(self):
        return f"Numele meu este {self.nume}, am {self.varsta} ani si sunt de gen {self.gen}."

    def este_major(self):
        return self.varsta >= 18

    def schimba_gen(self):
        if self.gen.lower() == "masculin":
            self.gen = "feminin"
        elif self.gen.lower() == "feminin":
            self.gen = "masculin"

    def adauga_ani(self, ani):
        self.varsta += ani

persoane = [
    Persoana("Alice", 25, "feminin"),
    Persoana("Bob", 17, "masculin"),
    Persoana("Charlie", 30, "masculin"),
    Persoana("Diana", 15, "feminin"),
    Persoana("Eve", 20, "feminin")
]

print("Numele și vârsta fiecărei persoane:")
for persoana in persoane:
    print(f"{persoana.nume} - {persoana.varsta} ani")
print("\nIntroducerea fiecărei persoane:")
for persoana in persoane:
    print(persoana.introducere())
print("\nDacă fiecare persoană este majoră sau nu:")
for persoana in persoane:
    status = "major" if persoana.este_major() else "minor"
    print(f"{persoana.nume} este {status}.")
print("\nSchimbarea genului fiecărei persoane:")
for persoana in persoane:
    persoana.schimba_gen()
    print(f"{persoana.nume} are acum genul {persoana.gen}.")
import random
print("\nAdăugarea unui număr aleator de ani la vârsta fiecărei persoane:")
for persoana in persoane:
    ani_adiționali = random.randint(1, 10)
    persoana.adauga_ani(ani_adiționali)
    print(f"{persoana.nume} are acum {persoana.varsta} ani.")   
print("\nLista cu toate persoanele care sunt majore:")
majore = [persoana for persoana in persoane if persoana.este_major()]
for persoana in majore:
    print(f"{persoana.nume} - {persoana.varsta} ani")
print("\nLista cu toate persoanele care au genul 'masculin' și au peste 14 ani:")
masculini_peste_14 = [persoana for persoana in persoane if persoana.gen.lower() == "masculin" and persoana.varsta > 14]
for persoana in masculini_peste_14:
    print(f"{persoana.nume} - {persoana.varsta} ani")
    