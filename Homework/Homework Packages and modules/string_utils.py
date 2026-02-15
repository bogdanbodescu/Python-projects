'''4. Sa se creeze un modul numit "string_utils" care sa contina functii pentru manipularea stringurilor: inversarea unui string, verificarea daca un string este palindrom.
   Sa se scrie un script care sa importe modulul si sa se execute fiecare functie asupra unui string primit ca si argument din linia de comanda.
'''

def inversare(text):
    """Functie care inverseaza un string."""
    return text[::-1]

def este_palindrom(text):
    """Functie care verifica daca un string este palindrom."""
    text_curat = ''.join(text.split()).lower()  # Eliminam spatiile si convertim la lowercase
    return text_curat == text_curat[::-1]
