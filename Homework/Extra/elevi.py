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


elevi = [
    {
        "Nume": "Popescu",
        "Prenume": "Ana",
        "Nota_romana": 9,
        "Nota_matematica": 10,
        "Nota_engleza": 8,
        "Media": (9 + 10 + 8) / 3
    },
    {
        "Nume": "Ionescu",
        "Prenume": "Maria",
        "Nota_romana": 7,
        "Nota_matematica": 8,
        "Nota_engleza": 9,
        "Media": (7 + 8 + 9) / 3
    },
    {
        "Nume": "Georgescu",
        "Prenume": "Andrei",
        "Nota_romana": 6,
        "Nota_matematica": 7,
        "Nota_engleza": 8,
        "Media": (6 + 7 + 8) / 3
    },
    {
        "Nume": "Dumitrescu",
        "Prenume": "Elena",
        "Nota_romana": 10,
        "Nota_matematica": 9,
        "Nota_engleza": 10,
        "Media": (10 + 9 + 10) / 3
    },
    {
        "Nume": "Stan",
        "Prenume": "Mihai",
        "Nota_romana": 5,
        "Nota_matematica": 6,
        "Nota_engleza": 7,
        "Media": (5 + 6 + 7) / 3
    }
]

def calculare_medie(*args):
    return sum(args) / len(args)

def adauga_elev(elevi):
    attempts = 0

    print("Va rugam introduceti datele despre elev")
    surname = input("Nume: ").strip()
    name = input("Prenume: ").strip()

    while attempts < 3:
        try:
            nota_romana = float(input("Nota romana: ").strip())
            nota_matematica = float(input("Nota matematica: ").strip())
            nota_engleza = float(input("Nota engleza: ").strip())

            if not (1 <= nota_romana <= 10 and 1 <= nota_matematica <= 10 and 1 <= nota_engleza <= 10):
                attempts += 1
                print(f"Notele trebuie sa fie intre 1 si 10. Mai aveti {3-attempts} incercari.")
                continue

            break  

        except ValueError:
            attempts += 1
            print(f"Notele nu sunt numere. Mai aveti {3-attempts} incercari.")
            continue

    if attempts >= 3:
        return elevi  

    elevi.append({
        "Nume": surname,
        "Prenume": name,
        "Nota_romana": nota_romana,
        "Nota_matematica": nota_matematica,
        "Nota_engleza": nota_engleza,
        "Media": calculare_medie(nota_romana, nota_matematica, nota_engleza)
    })

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
    for index, elem in enumerate(elevi):
        if elem["Nume"] == nume and elem["Prenume"] == prenume:
            return index
    return -1


def modifica_elev(elevi):
    index = index_elev(elevi)
    if index == -1:
        print("Elevul mentionat nu se afla in lista.")
        return elevi

    print("Elevul exista. Ce doriti sa modificati:")
    print("1. Nume/Prenume")
    print("2. Note (romana/matematica/engleza)")
    optiune = input("Alegeti optiunea: ").strip()

    if optiune == "1":
        name1 = input("Noul nume (sau 0): ").strip()
        name2 = input("Noul prenume (sau 0): ").strip()

        if name1 != "0" and name1:
            elevi[index]["Nume"] = name1[0].upper() + name1[1:].lower()
        if name2 != "0" and name2:
            elevi[index]["Prenume"] = name2[0].upper() + name2[1:].lower()

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
            elevi[index]["Nota_romana"] = nota1
        if 1 <= nota2 <= 10:
            elevi[index]["Nota_matematica"] = nota2
        if 1 <= nota3 <= 10:
            elevi[index]["Nota_engleza"] = nota3

        elevi[index]["Media"] = calculare_medie(
            elevi[index]["Nota_romana"],
            elevi[index]["Nota_matematica"],
            elevi[index]["Nota_engleza"],
        )

        print("Notele au fost modificate (doar cele intre 1 si 10).")

    else:
        print("Optiune invalida. Nicio modificare.")

    return elevi


def sterge_elev(elevi):
    index = index_elev(elevi)
    if index == -1:
        print("Elevul mentionat nu se afla in lista.")
        return elevi

    elevi.pop(index)
    print("Elevul mentionat a fost sters.")
    return elevi


def cauta_elev(elevi):
    index = index_elev(elevi)
    if index == -1:
        print("Elevul nu a fost gasit.")
        return
    print("Elevul a fost gasit:")
    afiseaza_elevi([elevi[index]])


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