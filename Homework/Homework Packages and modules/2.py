#2. Sa se creeze un pachet numit "geometry" care sa contina doua module: "area" si "perimeter". Modulul "area" sa contina functii pentru calcularea ariei unui cerc, patrat si dreptunghi, iar modulul "perimeter" sa contina functii pentru calcularea perimetrului acelorasi forme geometrice.
#   Din fisierul principal, sa se importe pachetul si sa se execute fiecare functie cu valori generate aleatoriu.

import random
from geometry import area, perimeter
if __name__ == "__main__":
    # Cerc
    raza = random.uniform(1.0, 10.0)
    print(f"Cerc - Raza: {raza:.2f}")
    print(f"Aria cercului: {area.cerc(raza):.2f}")
    print(f"Perimetrul cercului: {perimeter.cerc(raza):.2f}")

    # Patrat
    latura = random.uniform(1.0, 10.0)
    print(f"\nPatrat - Latura: {latura:.2f}")
    print(f"Aria patratului: {area.patrat(latura):.2f}")
    print(f"Perimetrul patratului: {perimeter.patrat(latura):.2f}")

    # Dreptunghi
    lungime = random.uniform(1.0, 10.0)
    latime = random.uniform(1.0, 10.0)
    print(f"\nDreptunghi - Lungime: {lungime:.2f}, Latime: {latime:.2f}")
    print(f"Aria dreptunghiului: {area.dreptunghi(lungime, latime):.2f}")
    print(f"Perimetrul dreptunghiului: {perimeter.dreptunghi(lungime, latime):.2f}")