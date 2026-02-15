#1. Sa se scrie un program care citeste de la tastatura informatii despre persoane (nume, prenume, varsta, oras)
#   si le salveaza intr-un fisier text numit "persoana.txt" in formatul: "Nume Prenume, Varsta, Oras".

nume = input("Introduceti numele: ")
prenume = input("Introduceti prenumele: ")
varsta = input("Introduceti varsta: ")
oras = input("Introduceti orasul: ")
with open("persoana.txt", "w") as file:
    file.write(f"{nume} {prenume}, {varsta}, {oras}")
file.close()
