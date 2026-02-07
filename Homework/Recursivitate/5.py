#5) Scrie o functie recursiva care calculeaza suma tuturor elementelor dintr-o lista imbricata.
#Ex: pentru [1, 2, [3, 4, [5, 6]], 7] returneaza 28
def nested_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total