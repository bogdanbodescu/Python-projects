"""3. Sa se creeze un script care sa accepte argumente din linia de comanda pentru nume, prenume, varsta, folosind modulul argparse. Scriptul sa afiseze numele complet al persoanei si varsta in urmatorul format:
    Nume: [nume]
    Prenume: [prenume]
    Varsta: [varsta] ani
"""

import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Afiseaza numele complet si varsta unei persoane.")
    parser.add_argument("--nume", required=True, help="Numele persoanei")
    parser.add_argument("--prenume", required=True, help="Prenumele persoanei")
    parser.add_argument("--varsta", type=int, required=True, help="Varsta persoanei")

    args = parser.parse_args()

    print(f"Nume: {args.nume}")
    print(f"Prenume: {args.prenume}")
    print(f"Varsta: {args.varsta} ani")