#5. Se da un fisier de logging "login.txt" care contine date referitor la incercarile de autentificare ale utilizatorilor:
#   Sa se scrie un program care citeste fisierul "login.txt" si salveaza in fisierul "user_attempts.txt" numarul de incercari de autentificare
#   pentru fiecare utilizator si ora si data ultimei incercari de autentificare reusite in formatul:
   # <user> | <numar_incercari> | <ultima_data_ora_reusita>
# Formatul fisierului "login.txt" este urmatorul:
#$2026-02-12T13:45:00Z | @user7 | login failed
#$2026-02-12T13:45:00Z | @user7 | login passed

from datetime import datetime
user_attempts = {}
with open("login.txt", "r") as file:
    for linie in file:
        data, user, status = linie.strip().split(" | ")
        if user not in user_attempts:
            user_attempts[user] = {"incercari": 0, "ultima_reusita": None}
        user_attempts[user]["incercari"] += 1
        if status == "login passed":
            data = data.strip("$")
            data_reusita = datetime.strptime(data, "%Y-%m-%dT%H:%M:%SZ")
            if (user_attempts[user]["ultima_reusita"] is None or 
                data_reusita > user_attempts[user]["ultima_reusita"]):
                user_attempts[user]["ultima_reusita"] = data_reusita
with open("user_attempts.txt", "w") as file:
    for user, info in user_attempts.items():
        ultima_reusita_str = info["ultima_reusita"].strftime("%Y-%m-%d %H:%M:%S") if info["ultima_reusita"] else "N/A"
        file.write(f"{user} | {info['incercari']} | {ultima_reusita_str}\n")
file.close()


