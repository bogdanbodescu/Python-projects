# Folositi list comprehension pentru a rezolva urmatoarele exercitii:
# 1) Creeaza o lista cu patratele numerelor de la 0 la 9. Ex: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
lista_patrate = [x**2 for x in range(10)]
# 2) Creeaza o lista cu toate numerele pare intre divizibile cu 3 dintre 1 si 50 inclusiv. Ex: [6, 12, 18, 24, 30, 36, 42, 48]
lista_pare_div3 = [x for x in range(1, 51) if x % 2 == 0 and x % 3 == 0]
# 3) Dintr-o lista cu cuvinte creeaza o lista cu lungimile fiecarui cuvant. Ex: ['ana', 'maria', 'ion', 'marioara', '1468912'] -> [3, 5, 3, 8, 7]
cuvinte = ['ana', 'maria', 'ion', 'marioara', '1468912']
lungimi_cuvinte = [len(cuvant) for cuvant in cuvinte]
# 4) Dintr-o lista cu numere de la 1 la 25, creeaza o lista cu patratele numerelor care sunt divizibile cu 4 si cu 6. Ex: [144, 576, 1296, 2304]
patrate_div4_si_6 = [x**2 for x in range(1, 26) if x % 4 == 0 and x % 6 == 0]
# 5) Creeaza o lista cu toate vocalele dintr-un text dat. Ex: 'Aceasta este o propozitie de test.' -> ['A', 'e', 'a', 'a', 'e', 'o', 'o', 'i', 'i', 'e', 'e']
text = 'Aceasta este o propozitie de test.'
vocale = [litera for litera in text if litera.lower() in 'aeiou']

# Folositi any pentru rezolvarea urmatoarelor exercitii:
# 1) Verifica daca intr-o lista de numere exista cel putin un numar par. Ex: [1, 3, 5, 7, 8] -> True
numere = [1, 3, 5, 7, 8]
exista_numar_par = any(numar % 2 == 0 for numar in numere)
# 2) Verifica daca intr-o lista de cuvinte exista cel putin un cuvant care sa contina litera 'z'. Ex: ['ana', 'maria', 'ioana', 'zebra'] -> True
cuvinte = ['ana', 'maria', 'ioana', 'zebra']
exista_cuvant_cu_z = any('z' in cuvant for cuvant in cuvinte)
# 3) Verifica daca intr-o lista de numere exista cel putin un numar negativ. Ex: [4, 5, -1, 3, 0] -> True
numere = [4, 5, -1, 3, 0]
exista_numar_negativ = any(numar < 0 for numar in numere)
# 4) Verifica daca intr-o lista de stringuri exista cel putin un string care sa fie gol. Ex: ['ana', '', 'maria'] -> True
stringuri = ['ana', '', 'maria']
exista_string_gol = any(len(s) == 0 for s in stringuri)
# 5) Verifica daca intr-o lista de caractere exista cel putin o vocala mare (A, E, I, O, U). Ex: ['a', 'b', 'C', 'D', 'E'] -> True
# lista_caractere = ['a', 'b', 'C', 'D', 'E']
lista_caractere = ['a', 'b', 'C', 'D', 'E']
exista_vocala_mare = any(litera in 'AEIOU' for litera in lista_caractere) 