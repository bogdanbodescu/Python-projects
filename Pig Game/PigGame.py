import random

def initialization():
    players = []
    players_score = []
    target = 0
    while True:
        playersNumber=input("How many players do you want to play? Minimum of 2 and a maximum of 4\n")
        if not playersNumber.isdigit() or int(playersNumber)>4 or int(playersNumber) < 2:
            break
        playersNumber = int(playersNumber)
        players_score = [0 for _ in range(playersNumber)]
        target = input("What is the score we want to play for?\n")
        if not target.isdigit() or int(target)<0:
            target = 0
            break
        for _ in range(playersNumber):
            players.append(input(f"Which is the name of player {_ + 1}?\n"))
        break
        
    if players == []:
        return [] , [] , ""
    
    return players, players_score, int(target)
        
def roll_round(score,target):
    result = 0
    while True:
        temp = random.randint(1,6)
        if temp == 1:
            print("Oh, unlucky, you rolled a 1. No points are added. Try again next round.\n")
            return 0
        if target-result-temp-score <= 0:
            message ="and you currently won. Press N or any other key if you want to stop and collect your prize."
        else:
            message=f"and you are off by {target-result-temp-score} points of the target."
        print(f"You rolled a {temp}. This means your current roll sums up to {result+temp}, which means your current total is {result+temp+score} "+ message)
        response = input("Do you want to continue rolling? Y/N\n")
        if response.upper() == "Y":
            result+= temp
            continue
        else:
            return result+temp


def play():
    max = 0
    flag = 0
    while True:
        players, players_score, target=initialization()
        if not players == []:
            break
        if players == []:
            response = input("Number of players does not fit the criteria. Do you want to try again?Y/N\n")
            if response.upper() == "N":
                break
        if target == 0:
            response = input("Target points is not valid. Do you want to try again?Y/N\n")
            if response.upper() == "N":
                break
    if not players == [] and not target == 0:
        print("Game starts! Good luck\n")
        while max < target:
            for player in range(len(players)):
                print(f"It is your turn {players[player]}")
                players_score[player] += roll_round(players_score[player],target)
                if players_score[player] >= target:
                    print(f"And we have a winner!!! Congratulation, {players[player]}! He has achieved {players_score[player]} points!\n")
                    max = target
                    break
                max = players_score[player] if players_score[player] > max else max
        print("Game has ended\n")
            

def main():
    play()

main()