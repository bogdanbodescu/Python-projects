"""
operations.py

Acest modul conține operațiile principale ale aplicației pentru gestionarea
angajaților. Sunt implementate funcționalitățile de tip CRUD, afișare,
filtrare și calcule salariale.

Funcționalități incluse:
    - adăugare angajat
    - căutare angajat după CNP
    - modificare angajat după CNP
    - ștergere angajat după CNP
    - afișare angajați
    - calcul cost total salarii companie
    - calcul cost total salarii departament
    - calcul fluturaș salarial
    - afișare angajați după senioritate
    - afișare angajați după departament
"""

from typing import Any

import storage as st
import utils as ut

Employee = dict[str, Any]


def cnp_existent(angajati: list[Employee], cnp: str) -> bool:
    """
    Verifică dacă există deja un angajat cu CNP-ul dat.

    Args:
        angajati (list[Employee]): Lista de angajați.
        cnp (str): CNP-ul căutat.

    Returns:
        bool: True dacă există, False altfel.
    """
    return any(angajat["cnp"] == cnp for angajat in angajati)


def adauga_angajat(angajati: list[Employee]) -> list[Employee]:
    """
    Adaugă un angajat nou în lista de angajați dacă datele introduse sunt valide.

    Args:
        angajati (list[Employee]): Lista curentă de angajați.

    Returns:
        list[Employee]: Lista actualizată de angajați.
    """
    print("Adăugare angajat:")
    nume = input("Nume: ").strip().title()
    prenume = input("Prenume: ").strip().title()
    cnp = input("CNP: ").strip()
    varsta = input("Vârstă: ").strip()
    departament = input("Departament: ").strip()
    salariu = input("Salariu: ").strip()
    senioritate = input("Senioritate (junior / mid / senior): ").strip().lower()

    is_valid, error_message = ut.validate_employee_data(
        nume, prenume, cnp, varsta, departament, salariu, senioritate
    )
    if not is_valid:
        print(f"Eroare: {error_message}")
        return angajati

    if cnp_existent(angajati, cnp):
        print("Eroare: Există deja un angajat cu acest CNP.")
        return angajati

    angajat_nou: Employee = {
        "nume": nume,
        "prenume": prenume,
        "cnp": cnp,
        "varsta": int(varsta),
        "departament": departament,
        "salariu": float(salariu),
        "senioritate": senioritate
    }

    angajati.append(angajat_nou)
    st.salveaza_angajati(angajati)
    print(f"Angajatul {nume} {prenume} a fost adăugat cu succes.")

    return angajati


def cauta_angajat(angajati: list[Employee]) -> None:
    """
    Caută un angajat după CNP și afișează datele acestuia.

    Args:
        angajati (list[Employee]): Lista de angajați în care se face căutarea.

    Returns:
        None
    """
    cnp_cautat = input("Introduceți CNP-ul angajatului pe care doriți să îl căutați: ").strip()

    if not ut.validate_cnp(cnp_cautat):
        print(f"Eroare: CNP-ul trebuie să conțină exact {ut.LEN_CNP} cifre și să fie numeric.")
        return

    for angajat in angajati:
        if angajat["cnp"] == cnp_cautat:
            print("Angajat găsit:")
            print(f'Nume: {angajat["nume"]}')
            print(f'Prenume: {angajat["prenume"]}')
            print(f'CNP: {angajat["cnp"]}')
            print(f'Vârstă: {angajat["varsta"]}')
            print(f'Departament: {angajat["departament"]}')
            print(f'Salariu: {angajat["salariu"]}')
            print(f'Senioritate: {angajat["senioritate"]}')
            return

    print("Angajatul cu CNP-ul specificat nu a fost găsit.")


def modifica_angajat(angajati: list[Employee]) -> list[Employee]:
    """
    Modifică datele unui angajat identificat după CNP.

    Utilizatorul poate lăsa câmpurile goale pentru a păstra valorile curente.

    Args:
        angajati (list[Employee]): Lista curentă de angajați.

    Returns:
        list[Employee]: Lista actualizată de angajați.
    """
    cnp_cautat = input("Introduceți CNP-ul angajatului pe care doriți să îl modificați: ").strip()

    if not ut.validate_cnp(cnp_cautat):
        print(f"Eroare: CNP-ul trebuie să conțină exact {ut.LEN_CNP} cifre și să fie numeric.")
        return angajati

    for angajat in angajati:
        if angajat["cnp"] == cnp_cautat:
            print("Angajat găsit. Introduceți noile detalii (lăsați gol pentru a păstra valoarea curentă):")

            nume = input(f'Nume ({angajat["nume"]}): ').strip().title() or angajat["nume"]
            prenume = input(f'Prenume ({angajat["prenume"]}): ').strip().title() or angajat["prenume"]
            varsta = input(f'Vârstă ({angajat["varsta"]}): ').strip() or str(angajat["varsta"])
            departament = input(f'Departament ({angajat["departament"]}): ').strip() or angajat["departament"]
            salariu = input(f'Salariu ({angajat["salariu"]}): ').strip() or str(angajat["salariu"])
            senioritate = input(f'Senioritate ({angajat["senioritate"]}): ').strip().lower() or angajat["senioritate"]

            is_valid, error_message = ut.validate_employee_data(
                nume, prenume, cnp_cautat, varsta, departament, salariu, senioritate
            )
            if not is_valid:
                print(f"Eroare: {error_message}")
                return angajati

            angajat["nume"] = nume
            angajat["prenume"] = prenume
            angajat["varsta"] = int(varsta)
            angajat["departament"] = departament
            angajat["salariu"] = float(salariu)
            angajat["senioritate"] = senioritate

            st.salveaza_angajati(angajati)
            print(f"Datele angajatului cu CNP-ul {cnp_cautat} au fost actualizate cu succes.")
            return angajati

    print("Angajatul cu CNP-ul specificat nu a fost găsit.")
    return angajati


def sterge_angajat(angajati: list[Employee]) -> list[Employee]:
    """
    Șterge un angajat din listă după CNP, cu confirmare.

    Args:
        angajati (list[Employee]): Lista curentă de angajați.

    Returns:
        list[Employee]: Lista actualizată de angajați.
    """
    cnp_cautat = input("Introduceți CNP-ul angajatului pe care doriți să îl ștergeți: ").strip()

    if not ut.validate_cnp(cnp_cautat):
        print(f"Eroare: CNP-ul trebuie să conțină exact {ut.LEN_CNP} cifre și să fie numeric.")
        return angajati

    for i, angajat in enumerate(angajati):
        if angajat["cnp"] == cnp_cautat:
            confirmare = input(
                f"Sunteți sigur că doriți să ștergeți angajatul {angajat['nume']} {angajat['prenume']}? (da/nu): "
            ).strip().lower()

            if confirmare == "da":
                del angajati[i]
                st.salveaza_angajati(angajati)
                print(f"Angajatul cu CNP-ul {cnp_cautat} a fost șters cu succes.")
                return angajati

            print("Ștergerea a fost anulată.")
            return angajati

    print("Angajatul cu CNP-ul specificat nu a fost găsit.")
    return angajati


def afiseaza_angajati(angajati: list[Employee]) -> None:
    """
    Afișează toți angajații din listă.

    Args:
        angajati (list[Employee]): Lista de angajați.

    Returns:
        None
    """
    if not angajati:
        print("Nu există angajați de afișat.")
        return

    print("Lista angajaților:")
    for angajat in angajati:
        print(
            f'Nume: {angajat["nume"]} | '
            f'Prenume: {angajat["prenume"]} | '
            f'CNP: {angajat["cnp"]} | '
            f'Vârstă: {angajat["varsta"]} | '
            f'Departament: {angajat["departament"]} | '
            f'Salariu: {angajat["salariu"]} | '
            f'Senioritate: {angajat["senioritate"]}'
        )


def calcul_cost_total_salariu_companie(angajati: list[Employee]) -> None:
    """
    Calculează și afișează costul total al salariilor pentru întreaga companie.

    Args:
        angajati (list[Employee]): Lista de angajați.

    Returns:
        None
    """
    if not angajati:
        print("Nu există angajați pentru a calcula costul total al salariilor.")
        return

    total_salariu = sum(float(angajat["salariu"]) for angajat in angajati)
    print(f"Costul total al salariilor pentru companie este: {total_salariu:.2f}")


def calcul_cost_total_salariu_departament(angajati: list[Employee]) -> None:
    """
    Calculează și afișează costul total al salariilor pentru un departament ales.

    Args:
        angajati (list[Employee]): Lista de angajați.

    Returns:
        None
    """
    departament_cautat = input(
        "Introduceți numele departamentului pentru care doriți să calculați costul total al salariilor: "
    ).strip()

    salariu_departament = sum(
        float(angajat["salariu"])
        for angajat in angajati
        if angajat["departament"].lower() == departament_cautat.lower()
    )

    if salariu_departament > 0:
        print(f"Costul total al salariilor pentru departamentul '{departament_cautat}' este: {salariu_departament:.2f}")
    else:
        print(f"Nu există angajați în departamentul '{departament_cautat}' sau departamentul nu a fost găsit.")


def calcul_fluturas_salar(angajati: list[Employee]) -> None:
    """
    Calculează și afișează fluturașul salarial pentru un angajat identificat după CNP.

    Args:
        angajati (list[Employee]): Lista de angajați.

    Returns:
        None
    """
    cnp_cautat = input(
        "Introduceți CNP-ul angajatului pentru care doriți să calculați fluturașul salarial: "
    ).strip()

    if not ut.validate_cnp(cnp_cautat):
        print(f"Eroare: CNP-ul trebuie să conțină exact {ut.LEN_CNP} cifre și să fie numeric.")
        return

    for angajat in angajati:
        if angajat["cnp"] == cnp_cautat:
            salariu_brut = float(angajat["salariu"])
            salariu_detaliat = ut.calculate_payroll(salariu_brut)

            print(f"Fluturaș salarial pentru {angajat['nume']} {angajat['prenume']}:")
            print(f"Vârstă: {angajat['varsta']}")
            print(f"Salariu Brut: {salariu_brut:.2f}")
            print(f"CAS: {salariu_detaliat['cas']:.2f}")
            print(f"CASS: {salariu_detaliat['cass']:.2f}")
            print(f"Impozit: {salariu_detaliat['impozit']:.2f}")
            print(f"Salariu Net: {salariu_detaliat['net']:.2f}")
            return

    print("Angajatul cu CNP-ul specificat nu a fost găsit.")


def afiseaza_angajati_dupa_senioritate(angajati: list[Employee]) -> None:
    """
    Afișează angajații ordonați după senioritate.

    Args:
        angajati (list[Employee]): Lista de angajați.

    Returns:
        None
    """
    if not angajati:
        print("Nu există angajați de afișat.")
        return

    ordine_senioritate = {"junior": 0, "mid": 1, "senior": 2}
    angajati_ordonati = sorted(
        angajati,
        key=lambda x: ordine_senioritate.get(x["senioritate"].lower(), 99)
    )

    print("Angajați ordonați după senioritate:")
    for angajat in angajati_ordonati:
        print(
            f'Nume: {angajat["nume"]} | '
            f'Prenume: {angajat["prenume"]} | '
            f'CNP: {angajat["cnp"]} | '
            f'Vârstă: {angajat["varsta"]} | '
            f'Departament: {angajat["departament"]} | '
            f'Salariu: {angajat["salariu"]} | '
            f'Senioritate: {angajat["senioritate"]}'
        )


def afiseaza_angajati_dupa_departament(angajati: list[Employee]) -> None:
    """
    Afișează angajații grupați după departament.

    Args:
        angajati (list[Employee]): Lista de angajați.

    Returns:
        None
    """
    if not angajati:
        print("Nu există angajați de afișat.")
        return

    departamente: dict[str, list[Employee]] = {}

    for angajat in angajati:
        departamente.setdefault(angajat["departament"], []).append(angajat)

    print("Angajați grupați după departament:")
    for departament, angajati_in_departament in departamente.items():
        print(f"\nDepartament: {departament}")
        for angajat in angajati_in_departament:
            print(
                f'  Nume: {angajat["nume"]} | '
                f'Prenume: {angajat["prenume"]} | '
                f'CNP: {angajat["cnp"]} | '
                f'Vârstă: {angajat["varsta"]} | '
                f'Salariu: {angajat["salariu"]} | '
                f'Senioritate: {angajat["senioritate"]}'
            )