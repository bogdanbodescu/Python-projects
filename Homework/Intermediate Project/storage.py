import json

def incarca_angajati() -> list[dict]:
    """
    Incarca angajatii din fisierul angajati.json.
    Daca fisierul nu exista sau este corupt, returneaza lista goala.
    """
    try:
        with open("angajati.json", "r", encoding="utf-8") as f:
            angajati = json.load(f)

            # verificare minimă că este listă
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
    

def salveaza_angajati(angajati: list[dict]) -> None:
    """
    Salveaza lista de angajati in fisier JSON.
    """
    with open("angajati.json", "w", encoding="utf-8") as f:
        json.dump(angajati, f, indent=4, ensure_ascii=False)