#4. Se da un fisier de logging "log.txt" care contine date referitor la evenimentele dintr-un sistem:
#   Sa se scrie un program care citeste fisierul "log.txt" si afiseaza numarul de evenimente de fiecare tip (INFO, WARNING, ERROR)
#   si afiseaza ora si evenimentul de tip ERROR care a avut loc cel mai recent.
#  Formatul fisierului "log.txt" este urmatorul:
# 2024-01-01 13:29:00 - INFO - Sistemul a fost validat de echipa de management

from datetime import datetime
evenimente = {"INFO": 0, "WARNING": 0, "ERROR": 0}
ultimul_error = None
with open("log.txt", "r") as file:
    for linie in file:
        data, tip, mesaj = linie.strip().split(" - ")
        if tip in evenimente:
            evenimente[tip] += 1
            if tip == "ERROR":
                data_error = datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
                if ultimul_error is None or data_error > ultimul_error[0]:
                    ultimul_error = (data_error, mesaj)
print(f"Numar evenimente INFO: {evenimente['INFO']}")
print(f"Numar evenimente WARNING: {evenimente['WARNING']}")
print(f"Numar evenimente ERROR: {evenimente['ERROR']}")
if ultimul_error:
    print(f"Ultimul eveniment ERROR a avut loc la {ultimul_error[0]}: {ultimul_error[1]}")
file.close()