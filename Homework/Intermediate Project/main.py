"""
Sa se scrie un program care tine evidenta angajatilor dintr-o companie.
Informatiile pe care trebuie sa le retinem despre un angajat sunt urmatoarele:
	1) CNP
	2) Nume
	3) Prenume
	4) Varsta
	5) Salar
	6) Departament
	7) Senioritate (junior, mid, senior)

Programul trebuie sa dispuna de un meniu care ne permite sa efectuam urmatoarele actiuni:
	1) Adaugare angajat
	2) Cautare angajat (dupa CNP)
	3) Modificare date angajat (dupa CNP)
	4) Stergere angajat (dupa CNP)
	5) Afisare angajati
	6) Calcul cost total salarii companie
	7) Calcul cost total salarii departament
	8) Calcul fluturas salar angajat (dupa CNP) (CAS - 10% din brut, CASS - 25% din brut, Impozit - 10% din ce a ramas)
	9) Afisarea angajatilor pe baza senioritatii
	10) Afisarea angajatilor pe baza departamentului
	11) Iesire

Informatiile despre angajati trebuie sa fie stocate intr-un fisier astfel incat sa poata fi accesate si modificate ulterior.

Criterii notare:
    - 0.5p  documentare cod (docstrings, comentarii)
    - 0.5p  type hints
    - 1p    modularitate (impartirea codului in functii, module, etc)
    - 1p    naming conventions (denumire variabile, denumire functii, etc)
    - 1p    error handling (try-except, validare integritate date *, etc)
    - 1p    salvarea datelor intr-un fisier (citire/scriere)
    - 0.5p  adaugare angajati
    - 0.5p  afisare angajati
    - 0.5p  cautare angajat
    - 0.5p  modificare date angajat
    - 0.5p  stergere angajat
    - 0.5p  calcul cost total salarii companie
    - 0.5p  calcul cost total salarii departament
    - 0.5p  calcul fluturas salarial
    - 0.5p  afisarea angajatilor pe baza senioritatii
    - 0.5p  afisarea angajatilor pe baza departamentului

	* Verificare integriatate date (parametrii introdusi sa fie corespunzatori)
		- Exemple:
			- CNP sa fie de lungime corespunzatoare si sa contina doar cifre
			- Varsta sa fie mai mare de 18 ani
			- Salarul sa fie mai mare decat minimul pe economie (4050)
			- etc

Termen limita: Sambata 6 martie 2026 ora 23:59
Lucrul in echipa pentru acest proiect este permis, dar fiecare membru trebuie sa predea o versiune individuala a proiectului,
care sa fie diferita de cea a colegilor sai (de exemplu, prin adaugarea unor functionalitati suplimentare sau prin implementarea intr-un mod diferit a functionalitatilor cerute).
Pentru persoanele care depasesc termenul limita se vor scadea cate 0.25p pentru fiecare zi de intarziere.
Maximul de zile de intarziere este de 14 zile, dupa care proiectul nu va mai fi acceptat, iar nota va fi 1.
"""


from unittest import case
import operations as op
import storage as st
import utils as ut


def menu():
    print("=====================Meniu:=====================")
    print("1) Adaugare angajat")
    print("2) Cautare angajat (dupa CNP)")
    print("3) Modificare date angajat (dupa CNP)")
    print("4) Stergere angajat (dupa CNP)")
    print("5) Afisare angajati")
    print("6) Calcul cost total salarii companie")
    print("7) Calcul cost total salarii departament")
    print("8) Calcul fluturas salar angajat (dupa CNP)")
    print("9) Afisarea angajatilor pe baza senioritatii")
    print("10) Afisarea angajatilor pe baza departamentului")
    print("11) Iesire")
    print("================================================")

def main():
    angajati = st.incarca_angajati()
    tries = 0
    while True:
        if tries >= 3:
            print("Ai depasit numarul maxim de incercari. Programul se va inchide.")
            break
        menu()
        option = input("Alege o optiune: ").strip()
        match option:
            case "1":
                # Cod pentru adaugare angajat
                pass
            case "2":
                # Cod pentru cautare angajat
                pass
            case "3":
                # Cod pentru modificare date angajat
                pass
            case "4":
                # Cod pentru stergere angajat
                pass
            case "5":
                # Cod pentru afisare angajati
                pass
            case "6":
                # Cod pentru calcul cost total salarii companie
                pass
            case "7":
                # Cod pentru calcul cost total salarii departament
                pass
            case "8":
                # Cod pentru calcul fluturas salarial angajat
                pass
            case "9":
                # Cod pentru afisarea angajatilor pe baza senioritatii
                pass
            case "10":
                # Cod pentru afisarea angajatilor pe baza departamentului
                pass
            case "11":
                print("La revedere!")
                break
            case _ :
                print("Optiune invalida. Te rog sa alegi o optiune valida.")
                tries += 1
                continue
        tries = 0  # Resetam numarul de incercari dupa o optiune valida

if __name__ == "__main__":
    main()