"""
main.py

Acest modul reprezintă punctul de intrare în aplicația de gestionare a
angajaților. El afișează meniul principal, preia opțiunea utilizatorului
și apelează funcțiile corespunzătoare din modulele aplicației.
"""

import operations as op
import storage as st


def menu() -> None:
    """
    Afișează meniul principal al aplicației.

    Returns:
        None
    """
    print("===================== MENIU =====================")
    print("1) Adăugare angajat")
    print("2) Căutare angajat (după CNP)")
    print("3) Modificare date angajat (după CNP)")
    print("4) Ștergere angajat (după CNP)")
    print("5) Afișare angajați")
    print("6) Calcul cost total salarii companie")
    print("7) Calcul cost total salarii departament")
    print("8) Calcul fluturaș salarial angajat (după CNP)")
    print("9) Afișarea angajaților pe baza seniorității")
    print("10) Afișarea angajaților pe baza departamentului")
    print("11) Ieșire")
    print("=================================================")


def main() -> None:
    """
    Rulează aplicația principală.

    Încarcă lista de angajați din fișierul JSON, afișează meniul și execută
    acțiunea selectată de utilizator. Dacă utilizatorul introduce de 3 ori
    consecutiv o opțiune invalidă, programul se închide.

    Returns:
        None
    """
    angajati = st.incarca_angajati()
    tries = 0

    while True:
        if tries >= 3:
            print("Ai depășit numărul maxim de încercări. Programul se va închide.")
            break

        menu()
        option = input("Alege o opțiune: ").strip()

        match option:
            case "1":
                angajati = op.adauga_angajat(angajati)
            case "2":
                op.cauta_angajat(angajati)
            case "3":
                angajati = op.modifica_angajat(angajati)
            case "4":
                angajati = op.sterge_angajat(angajati)
            case "5":
                op.afiseaza_angajati(angajati)
            case "6":
                op.calcul_cost_total_salariu_companie(angajati)
            case "7":
                op.calcul_cost_total_salariu_departament(angajati)
            case "8":
                op.calcul_fluturas_salar(angajati)
            case "9":
                op.afiseaza_angajati_dupa_senioritate(angajati)
            case "10":
                op.afiseaza_angajati_dupa_departament(angajati)
            case "11":
                print("La revedere!")
                break
            case _:
                print("Opțiune invalidă. Te rog să alegi o opțiune validă.")
                tries += 1
                continue

        # Resetăm numărul de încercări după o opțiune validă
        tries = 0


if __name__ == "__main__":
    main()