'''2.
a) Creeaza o clasa Elev care are:
    
atribute private pentru trei note
atribut public pentru nume
b) Creeaza o metoda get_medie() care calculeaza media pe baza notelor.
d) Creeaza o metoda actualizeaza_note() care permite modificarea notelor.
e) Creeaza 3 elevi si:
    
afiseaza media fiecaruia
modifica notele unui elev
afiseaza noua medie
f) Explica de ce media NU ar trebui sa fie un atribut normal.
'''

class Elev:
    def __init__(self, nume, nota1, nota2, nota3):
        self.nume = nume
        self.__nota1 = nota1
        self.__nota2 = nota2
        self.__nota3 = nota3

    def get_medie(self):
        return (self.__nota1 + self.__nota2 + self.__nota3) / 3

    def actualizeaza_note(self, nota1=None, nota2=None, nota3=None):
        if nota1 is not None:
            self.__nota1 = nota1
        if nota2 is not None:
            self.__nota2 = nota2
        if nota3 is not None:
            self.__nota3 = nota3

elev1 = Elev("Alice", 8, 9, 10)
elev2 = Elev("Bob", 7, 6, 8)
elev3 = Elev("Charlie", 9, 9, 9)
print(f"{elev1.nume} are media: {elev1.get_medie():.2f}")
print(f"{elev2.nume} are media: {elev2.get_medie():.2f}")
print(f"{elev3.nume} are media: {elev3.get_medie():.2f}")
elev1.actualizeaza_note(nota1=10, nota2=10)
print(f"{elev1.nume} are noua media: {elev1.get_medie():.2f}")
# Explicație: Media nu ar trebui să fie un atribut normal deoarece este o valoare derivată care poate fi calculată în orice moment pe baza notelor. Dacă media ar fi un atribut normal, ar trebui să ne asigurăm că este actualizată de fiecare dată când se modifică notele, ceea ce poate duce la erori sau inconsistențe dacă uităm să actualizăm media. Prin menținerea mediei ca o metodă care calculează valoarea în timp real, ne asigurăm că întotdeauna obținem o medie corectă și actualizată, fără a depinde de starea unui atribut care poate deveni învechit sau incorect.