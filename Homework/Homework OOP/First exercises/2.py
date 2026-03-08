'''Creeaza o clasa numita "Masina" care are atributele "marca", "model" si "an_fabricatie". Adauga o metoda numita "descriere" care returneaza o descriere a masinii.
Creeaza o clasa numita "Masina" care are atributele "marca", "model" si "an_fabricatie". Adauga o metoda numita "descriere" care returneaza o descriere a masinii.
Instantiaza trei obiecte ale clasei "Masina" si afiseaza informatiile despre fiecare masina.

'''

class Masina:
    def __init__(self, marca, model, an_fabricatie):
        self.marca = marca
        self.model = model
        self.an_fabricatie = an_fabricatie

    def descriere(self):
        return f"{self.marca} {self.model} fabricată în {self.an_fabricatie}."
masina1 = Masina("Toyota", "Corolla", 2010)
masina2 = Masina("Ford", "Mustang", 2015)
masina3 = Masina("Honda", "Civic", 2018)
print(masina1.descriere())
print(masina2.descriere())
print(masina3.descriere())
