#7) Scrie o funcție care primește o listă de stringuri și returnează o listă cu lungimile fiecărui string.
def get_string_lengths(string_list):
    lengths = []
    for s in string_list:
        lengths.append(len(s))
    return lengths

strings = ["apple", "banana", "cherry"]
print(get_string_lengths(strings))  # Afisează [5, 6, 6]