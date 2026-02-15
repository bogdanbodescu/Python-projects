'''4. Sa se creeze un modul numit "string_utils" care sa contina functii pentru manipularea stringurilor: inversarea unui string, verificarea daca un string este palindrom.
   Sa se scrie un script care sa importe modulul si sa se execute fiecare functie asupra unui string primit ca si argument din linia de comanda.
'''
import argparse
import string_utils
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Manipularea stringurilor: inversare si verificare palindrom.")
    parser.add_argument("--text", required=True, help="Stringul asupra caruia se vor executa functiile")

    args = parser.parse_args()
    text = args.text

    print(f"String original: {text}")
    print(f"String inversat: {string_utils.inversare(text)}")
    if string_utils.este_palindrom(text):
        print("Stringul este un palindrom.")
    else:
        print("Stringul nu este un palindrom.")