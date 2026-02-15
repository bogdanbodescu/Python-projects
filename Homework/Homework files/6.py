#6. Sa se actualizeze programul de la mini proiectul referitor la gestionarea elevilor dintr-o scoala astfel incat informatiile despre elevi
#   sa persiste intr-un fisier text numit "elevi.txt" astfel incat datele sa fie disponibile la repornirea programului.

# Todo: 
# 1.Verificat numele si prenumele sa fie de minim un caracter
# 2.Verificat daca inainte sa adugam un elev nou, daca acesta exista deja in dictionar 


# Sa se scrie un program care tine evidenta elevilor dintr-o scoala.
# Programul trebuie sa dispuna de un meniu care ne pune la dispozitie
# urmatoarele optiuni:
#
#     1. Adaugare elev
#     2. Afisarea elevilor existenti
#     3. Modificare informatii elev existent
#     4. Stergere elev
#     5. Cautare elev dupa nume si prenume
#     6. Afisare elevi in ordinea mediilor
#     7. Afisare elevi cu media peste 8
#     8. Afisare elevi in ordine alfabetica (dupa nume)
#
# Pentru fiecare elev trebuie sa retinem urmatoarele informatii:
#
#     - Nume
#     - Prenume
#     - Nota romana
#     - Nota matematica
#     - Nota engleza
#     - Media

FISIER_ELEVI = "elevi.txt"
elevi = []

def calculare_medie(*args):
    return sum(args) / len(args)

def normalizare_nume(s):
    s = s.strip()
    if not s:
        return ""
    return s[0].upper() + s[1:].lower()

def cheie_elev(nume, prenume):
    return (nume.strip().lower(), prenume.strip().lower())

def exista_elev(elevi, nume, prenume):
    key = cheie_elev(nume, prenume)
    for e in elevi:
        if cheie_elev(e["Nume"], e["Prenume"]) == key:
            return True
    return False

# ---------- PERSISTENTA ----------

def incarca_elevi():
    elevi = []
    try:
        f = open(FISIER_ELEVI, "r", encoding="utf-8")
    except FileNotFoundError:
        return elevi

    with f:
        for linie in f:
            linie = linie.strip()
            if not linie:
                continue

            parts = linie.split("|")
            if len(parts) != 5:
                continue

            nume, prenume, nr, nm, ne = parts

            try:
                nr = float(nr)
                nm = float(nm)
                ne = float(ne)
            except ValueError:
                continue

            elevi.append({
                "Nume": nume,
                "Prenume": prenume,
                "Nota_romana": nr,
                "Nota_matematica": nm,
                "Nota_engleza": ne,
                "Media": calculare_medie(nr, nm, ne)
            })

    return elevi

def salveaza_elevi(elevi):
    with open(FISIER_ELEVI, "w", encoding="utf-8") as f:
        for e in elevi:
            linie = f"{e['Nume']}|{e['Prenume']}|{e['Nota_romana']}|{e['Nota_matematica']}|{e['Nota_engleza']}\n"
            f.write(linie)

# ---------- OPERATII ----------

def citeste_nume_prenume():
    print("Va rugam introduceti datele despre elev")
    surname = input("Nume: ").strip()
    name = input("Prenume: ").strip()

    if len(surname) < 1 or len(name) < 1:
        print("Numele si prenumele trebuie sa aiba minim un caracter.")
        return None, None

    surname = normalizare_nume(surname)
    name = normalizare_nume(name)
    return surname, name

def citeste_note():
    attempts = 0
    while attempts < 3:
        try:
            nota_romana = float(input("Nota romana: ").strip())
            nota_matematica = float(input("Nota matematica: ").strip())
            nota_engleza = float(input("Nota engleza: ").strip())

            if not (1 <= nota_romana <= 10 and 1 <= nota_matematica <= 10 and 1 <= nota_engleza <= 10):
                attempts += 1
                print(f"Notele trebuie sa fie intre 1 si 10. Mai aveti {3-attempts} incercari.")
                continue

            return nota_romana, nota_matematica, nota_engleza

        except ValueError:
            attempts += 1
            print(f"Note invalide (nu sunt numere). Mai aveti {3-attempts} incercari.")

    return None, None, None

def adauga_elev(elevi):
    surname, name = citeste_nume_prenume()
    if surname is None:
        return elevi

    # verificare existenta
    if exista_elev(elevi, surname, name):
        print("Elevul exista deja. Nu a fost adaugat.")
        return elevi

    nr, nm, ne = citeste_note()
    if nr is None:
        return elevi

    elevi.append({
        "Nume": surname,
        "Prenume": name,
        "Nota_romana": nr,
        "Nota_matematica": nm,
        "Nota_engleza": ne,
        "Media": calculare_medie(nr, nm, ne)
    })

    salveaza_elevi(elevi)
    print("Elev adaugat si salvat.")
    return elevi

def afiseaza_elevi(elevi):
    if not elevi:
        print("Nu exista elevi inregistrati.")
        return

    for elev in elevi:
        print(
            f"{elev['Nume']} {elev['Prenume']} | "
            f"Romana: {elev['Nota_romana']} | "
            f"Matematica: {elev['Nota_matematica']} | "
            f"Engleza: {elev['Nota_engleza']} || "
            f"Media: {elev['Media']:.2f}"
        )

def index_elev(elevi):
    nume = input("Dati numele elevului: ").strip()
    prenume = input("Dati prenumele elevului: ").strip()
    key = cheie_elev(nume, prenume)

    for index, elem in enumerate(elevi):
        if cheie_elev(elem["Nume"], elem["Prenume"]) == key:
            return index
    return -1

def modifica_elev(elevi):
    idx = index_elev(elevi)
    if idx == -1:
        print("Elevul mentionat nu se afla in lista.")
        return elevi

    print("Elevul exista. Ce doriti sa modificati:")
    print("1. Nume/Prenume")
    print("2. Note (romana/matematica/engleza)")
    optiune = input("Alegeti optiunea: ").strip()

    if optiune == "1":
        name1 = input("Noul nume (sau 0): ").strip()
        name2 = input("Noul prenume (sau 0): ").strip()

        final_nume = elevi[idx]["Nume"]
        final_prenume = elevi[idx]["Prenume"]

        if name1 != "0":
            if len(name1.strip()) < 1:
                print("Numele nou trebuie sa aiba minim un caracter. Neschimbat.")
            else:
                final_nume = normalizare_nume(name1)

        if name2 != "0":
            if len(name2.strip()) < 1:
                print("Prenumele nou trebuie sa aiba minim un caracter. Neschimbat.")
            else:
                final_prenume = normalizare_nume(name2)

        # verificare duplicat la schimbare
        if cheie_elev(final_nume, final_prenume) != cheie_elev(elevi[idx]["Nume"], elevi[idx]["Prenume"]):
            if exista_elev(elevi, final_nume, final_prenume):
                print("Exista deja un elev cu acest nume si prenume. Modificarea a fost anulata.")
                return elevi

        elevi[idx]["Nume"] = final_nume
        elevi[idx]["Prenume"] = final_prenume
        print("Datele au fost modificate.")

    elif optiune == "2":
        try:
            nota1 = float(input("Nota romana (sau -1): ").strip())
            nota2 = float(input("Nota matematica (sau -1): ").strip())
            nota3 = float(input("Nota engleza (sau -1): ").strip())
        except ValueError:
            print("Note invalide. Nicio modificare.")
            return elevi

        if 1 <= nota1 <= 10:
            elevi[idx]["Nota_romana"] = nota1
        if 1 <= nota2 <= 10:
            elevi[idx]["Nota_matematica"] = nota2
        if 1 <= nota3 <= 10:
            elevi[idx]["Nota_engleza"] = nota3

        elevi[idx]["Media"] = calculare_medie(
            elevi[idx]["Nota_romana"],
            elevi[idx]["Nota_matematica"],
            elevi[idx]["Nota_engleza"],
        )

        print("Notele au fost modificate (doar cele intre 1 si 10).")

    else:
        print("Optiune invalida. Nicio modificare.")
        return elevi

    salveaza_elevi(elevi)
    print("Modificarile au fost salvate.")
    return elevi

def sterge_elev(elevi):
    idx = index_elev(elevi)
    if idx == -1:
        print("Elevul mentionat nu se afla in lista.")
        return elevi

    elevi.pop(idx)
    salveaza_elevi(elevi)
    print("Elevul mentionat a fost sters (si salvat).")
    return elevi

def cauta_elev(elevi):
    idx = index_elev(elevi)
    if idx == -1:
        print("Elevul nu a fost gasit.")
        return
    print("Elevul a fost gasit:")
    afiseaza_elevi([elevi[idx]])

def afiseaza_ord_medii(elevi):
    sortati = sorted(elevi, key=lambda x: x["Media"], reverse=True)
    afiseaza_elevi(sortati)

def afiseaza_medii_mari(elevi):
    media_minima = 8
    raspuns = [e for e in elevi if e["Media"] > media_minima]
    print(f"Elevii cu media mai mare decat {media_minima} sunt:")
    afiseaza_elevi(raspuns)

def afiseaza_ordine_alfabetica(elevi):
    sortati = sorted(elevi, key=lambda x: (x["Nume"], x["Prenume"]))
    print("Elevii in ordine alfabetica sunt:")
    afiseaza_elevi(sortati)

def print_options():
    print("\n===== MENIU GESTIONARE ELEVI =====")
    print("1. Adaugare elev")
    print("2. Afisarea elevilor existenti")
    print("3. Modificare informatii elev existent")
    print("4. Stergere elev")
    print("5. Cautare elev dupa nume si prenume")
    print("6. Afisare elevi in ordinea mediilor")
    print("7. Afisare elevi cu media peste 8")
    print("8. Afisare elevi in ordine alfabetica (dupa nume)")
    print("0. Iesire")

# ---------- MAIN ----------

elevi = incarca_elevi()

# daca nu exista fisier sau e gol, poti porni cu lista goala
# (daca vrei seed initial, poti adauga aici manual elevi si apoi salveaza_elevi(elevi))

while True:
    print_options()
    optiune_raw = input("Care este optiunea pe care vreti sa o faceti? ").strip()

    if not optiune_raw.isdigit():
        print("Optiunea este invalida. Introduceti un numar.")
        continue

    optiune = int(optiune_raw)

    match optiune:
        case 0:
            print("Ati parasit programul. O zi buna!")
            break
        case 1:
            elevi = adauga_elev(elevi)
        case 2:
            afiseaza_elevi(elevi)
        case 3:
            elevi = modifica_elev(elevi)
        case 4:
            elevi = sterge_elev(elevi)
        case 5:
            cauta_elev(elevi)
        case 6:
            afiseaza_ord_medii(elevi)
        case 7:
            afiseaza_medii_mari(elevi)
        case 8:
            afiseaza_ordine_alfabetica(elevi)
        case _:
            print("Nu exista optiunea aleasa.")