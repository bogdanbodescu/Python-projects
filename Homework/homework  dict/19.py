#19) Se da urmatorul text: "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani".
 #   Creeaza un dictionar care sa contina numele persoanelor ca si chei si varstele ca si valori.
text = "Ana are 12 ani, Ion are 15 ani, Maria are 12 ani, George are 15 ani, Elena are 14 ani"
people_dict = {}
for part in text.split(", "):
    name = part.split(" ")[0]
    age = int(part.split(" ")[2])
    people_dict[name] = age
print(people_dict)