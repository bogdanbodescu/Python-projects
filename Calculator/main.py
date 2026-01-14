def check_entrydata(value1,value2):
    try:
        val1 = float(value1)
        val2 = float(value2)
        return val1, val2
    except ValueError:
        raise ValueError("Valorile introduse trebuie sa fie numere.")

def add(value1, value2):
    val1, val2 = check_entrydata(value1, value2)
    return val1 + val2  

def subtract(value1, value2):
    val1, val2 = check_entrydata(value1, value2)
    return val1 - val2  

def multiply(value1, value2):
    val1, val2 = check_entrydata(value1, value2)
    return val1 * val2

def divide(value1, value2):
    val1, val2 = check_entrydata(value1, value2)
    if val2 == 0:
        raise ValueError("Impartirea la zero nu este permisa.")
    return val1 / val2

def main():
    while True:
        print("Alege optiunea:")
        print("1. Adunare")
        print("2. Scadere")
        print("3. Inmultire")
        print("4. Impartire")
        print("5. Iesire din program")
        choice = input("Introduceti optiunea (1/2/3/4/5): ")
        if choice == '5':
            print("Iesire din program.")
            break
        if choice in "1234":
            value1 = input("Introduceti primul numar: ")
            value2 = input("Introduceti al doilea numar: ")
            try:
                if choice == '1':
                    result = add(value1, value2)
                    print(f"Rezultat: {result}")
                elif choice == '2':
                    result = subtract(value1, value2)
                    print(f"Rezultat: {result}")
                elif choice == '3':
                    result = multiply(value1, value2)
                    print(f"Rezultat: {result}")
                elif choice == '4':
                    result = divide(value1, value2)
                    print(f"Rezultat: {result}")
            except ValueError as e:
                print(e)    
        else:
            print("Optiune invalida. Va rugam sa incercati din nou.")



if __name__ == "__main__":
    main()