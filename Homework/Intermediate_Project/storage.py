"""
storage.py

Acest modul se ocupă de persistenta datelor aplicației.
Conține funcții pentru citirea și salvarea informațiilor despre
angajați în fișierul JSON utilizat ca bază de date simplă.

Funcționalități:
    - încărcarea listei de angajați din fișier
    - salvarea listei de angajați în fișier
"""

import json
from typing import List, Dict


def incarca_angajati() -> List[Dict]:
    """
    Încarcă lista de angajați din fișierul 'angajati.json'.

    Dacă fișierul nu există sau este corupt, funcția returnează
    o listă goală pentru a permite aplicației să continue rularea.

    Returns:
        List[Dict]: Lista de angajați citită din fișier.
    """

    try:
        with open("angajati.json", "r", encoding="utf-8") as f:
            angajati = json.load(f)

            # verificare minimă că structura este listă
            if not isinstance(angajati, list):
                print("Fisierul JSON nu contine o lista valida. Se porneste cu lista goala.")
                return []

            return angajati

    except FileNotFoundError:
        print("Fisierul 'angajati.json' nu a fost gasit. Se va crea unul nou la salvare.")
        return []

    except json.JSONDecodeError:
        print("Fisierul 'angajati.json' este corupt sau gol. Se porneste cu lista goala.")
        return []


def salveaza_angajati(angajati: List[Dict]) -> None:
    """
    Salvează lista de angajați în fișierul 'angajati.json'.

    Args:
        angajati (List[Dict]): Lista de angajați care trebuie salvată.

    Returns:
        None
    """

    with open("angajati.json", "w", encoding="utf-8") as f:
        json.dump(angajati, f, indent=4, ensure_ascii=False)