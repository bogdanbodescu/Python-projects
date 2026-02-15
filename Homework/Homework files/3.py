#3. Se da urmatorul fisier "produse.txt" care contine informatii despre produse.
#   Sa se scrie un program care citeste informatiile despre produse din fisierul "produse.txt"
#   si calculeaza pretul total al stocului pentru fiecare produs.
# Pasta dinti - 20 lei - 50 bucati

with open("produse.txt", "r") as file:
    for linie in file:
        nume, pret, cantitate = linie.strip().split(" - ")
        pret_total = int(pret.split()[0]) * int(cantitate.split()[0])
        print(f"Produs: {nume}, Pret total stoc: {pret_total} lei")
file.close()
