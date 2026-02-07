#4) Scrie o functie recursiva care calculeaza adancimea(cate liste nivele de liste sunt) unei liste imbricate.
#Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 3
def depth(lst):
    if not isinstance(lst, list):
        return 0
    return 1 + max(depth(item) for item in lst)