'''Exercitiu extra:
Se dau urmatoarele expresii matematice:
((a + b) * (c - d) + e) / f - (g * (h + i)) -> corect deschise si inchise
((a + b) * (c - d) + e) / f - )g * (h + i)( -> incorect deschise si inchise
Sa se verifice daca parantezele sunt corect deschise si inchise.'''


expresie1 = "((a + b) * (c - d) + e) / f - (g * (h + i))"
expresie2 = "((a + b) * (c - d) + e) / f - )g * (h + i)("

def verifica_paranteze(expresie):
    heap = []
    for char in expresie:
        if char == '(':
            heap.append(char)
        elif char == ')':
            if not heap:
                return False
            heap.pop()
    return len(heap) == 0
print(verifica_paranteze(expresie1))  # Ar trebui să returneze True
print(verifica_paranteze(expresie2))  # Ar trebui să returneze False
