'''Creeaza o clasa numita "Animal" care are atributele "nume", "varsta" si "specie". Adauga o metoda numita "descriere" care returneaza o descriere a animalului.
Instantiaza doua obiecte ale clasei "Animal" si apeleaza metoda "descriere" pentru fiecare obiect.
'''

class Animal:
    def __init__(self, nume, varsta, specie):
        self.nume = nume
        self.varsta = varsta
        self.specie = specie

    def descriere(self):
        return f"{self.nume} este un {self.specie} de {self.varsta} ani."
    

animal1 = Animal("Leo", 5, "leu")
animal2 = Animal("Mia", 3, "pisică")

print(animal1.descriere())
print(animal2.descriere())
