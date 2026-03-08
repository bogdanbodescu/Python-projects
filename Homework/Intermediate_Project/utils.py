"""
utils.py

Acest modul conține funcții utilitare folosite în sistemul de management al
angajaților. Aici sunt definite constantele aplicației, funcțiile de validare
a datelor introduse și funcțiile pentru calculul fluturașului salarial.
"""

from typing import Tuple, Optional, Dict

# Constante aplicație
MINIMUM_AGE: int = 18
MINIMUM_SALARY: float = 4050.0
LEN_CNP: int = 13
MAX_AGE: int = 80
MAX_SALARY: float = 100000.0  

CAS: int = 10
CASS: int = 25
IMPOZIT: int = 10

VALID_SENIORITY_LEVELS: Tuple[str, ...] = ("junior", "mid", "senior")


def validate_cnp(cnp: str) -> bool:
    """
    Verifică dacă un CNP este valid.

    Args:
        cnp (str): CNP-ul introdus.

    Returns:
        bool: True dacă CNP-ul este valid, False altfel.
    """
    cnp = cnp.strip()
    return len(cnp) == LEN_CNP and cnp.isdigit()


def validate_name(text: str, field_name: str) -> Tuple[bool, Optional[str]]:
    """
    Validează numele sau prenumele unui angajat.

    Args:
        text (str): Textul introdus.
        field_name (str): Denumirea câmpului pentru mesajul de eroare.

    Returns:
        Tuple[bool, Optional[str]]
    """
    text = text.strip()

    if len(text) < 2:
        return False, f"{field_name} trebuie să aibă cel puțin 2 caractere."

    if not text.replace("-", "").replace(" ", "").isalpha():
        return False, f"{field_name} trebuie să conțină doar litere, spații sau cratimă."

    return True, None


def validate_department(departament: str) -> Tuple[bool, Optional[str]]:
    """
    Validează departamentul unui angajat.

    Args:
        departament (str): Numele departamentului.

    Returns:
        Tuple[bool, Optional[str]]
    """
    departament = departament.strip()

    if len(departament) < 2:
        return False, "Departamentul trebuie să conțină cel puțin 2 caractere."

    return True, None


def validate_age(varsta: str) -> Tuple[bool, Optional[str]]:
    """
    Validează vârsta unui angajat.

    Args:
        varsta (str): Vârsta introdusă.

    Returns:
        Tuple[bool, Optional[str]]
    """
    try:
        varsta_int = int(varsta)
    except ValueError:
        return False, "Vârsta trebuie să fie un număr întreg valid."

    if varsta_int < MINIMUM_AGE:
        return False, f"Vârsta trebuie să fie de cel puțin {MINIMUM_AGE} ani."

    if varsta_int > MAX_AGE:
        return False, f"Vârsta trebuie să fie mai mică sau egală cu {MAX_AGE}."

    return True, None


def validate_salary(salariu: str) -> Tuple[bool, Optional[str]]:
    """
    Validează salariul unui angajat.

    Args:
        salariu (str): Salariul introdus.

    Returns:
        Tuple[bool, Optional[str]]
    """
    try:
        salariu_float = float(salariu)
    except ValueError:
        return False, "Salariul trebuie să fie un număr valid."

    if salariu_float < MINIMUM_SALARY:
        return False, f"Salariul trebuie să fie mai mare sau egal cu {MINIMUM_SALARY}."

    if salariu_float > MAX_SALARY:
        return False, f"Salariul introdus este prea mare pentru a fi valid. Limita maximă este {MAX_SALARY}."

    return True, None


def validate_seniority(senioritate: str) -> Tuple[bool, Optional[str]]:
    """
    Validează nivelul de senioritate al angajatului.

    Args:
        senioritate (str): Senioritatea introdusă.

    Returns:
        Tuple[bool, Optional[str]]
    """
    if senioritate.strip().lower() not in VALID_SENIORITY_LEVELS:
        return False, "Senioritatea trebuie să fie una dintre valorile: junior, mid, senior."

    return True, None


def validate_employee_data(
    nume: str,
    prenume: str,
    cnp: str,
    varsta: str,
    departament: str,
    salariu: str,
    senioritate: str
) -> Tuple[bool, Optional[str]]:
    """
    Validează toate datele introduse pentru un angajat.

    Args:
        nume (str): Numele angajatului.
        prenume (str): Prenumele angajatului.
        cnp (str): CNP-ul angajatului.
        varsta (str): Vârsta angajatului.
        departament (str): Departamentul angajatului.
        salariu (str): Salariul brut.
        senioritate (str): Nivelul de senioritate.

    Returns:
        Tuple[bool, Optional[str]]
    """

    if not nume or not prenume or not cnp or not varsta or not departament or not salariu or not senioritate:
        return False, "Toate câmpurile sunt obligatorii."

    valid_name, name_error = validate_name(nume, "Numele")
    if not valid_name:
        return False, name_error

    valid_prenume, prenume_error = validate_name(prenume, "Prenumele")
    if not valid_prenume:
        return False, prenume_error

    if not validate_cnp(cnp):
        return False, f"CNP-ul trebuie să conțină exact {LEN_CNP} cifre și să fie numeric."

    valid_age, age_error = validate_age(varsta)
    if not valid_age:
        return False, age_error

    valid_department, department_error = validate_department(departament)
    if not valid_department:
        return False, department_error

    valid_salary, salary_error = validate_salary(salariu)
    if not valid_salary:
        return False, salary_error

    valid_seniority, seniority_error = validate_seniority(senioritate)
    if not valid_seniority:
        return False, seniority_error

    return True, None


def calculate_payroll(salariu: float) -> Dict[str, float]:
    """
    Calculează fluturașul salarial.

    Args:
        salariu (float): Salariul brut.

    Returns:
        Dict[str, float]: Detalii despre taxele calculate.
    """

    cas = salariu * CAS / 100
    cass = salariu * CASS / 100
    impozit = (salariu - cas - cass) * IMPOZIT / 100
    net = salariu - cas - cass - impozit

    return {
        "cas": cas,
        "cass": cass,
        "impozit": impozit,
        "net": net
    }