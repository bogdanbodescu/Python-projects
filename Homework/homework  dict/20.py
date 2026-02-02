#20) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
#   Creeaza un dictionar care sa stocheze frecventa literelor din text si afiseaza-l. Exemplu: {'a': 7, 'n': 3, ... }.
text = "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani"
frequency = {}

for char in text.lower():
    if char.isalpha():           
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

print(frequency)