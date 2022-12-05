from enum import Enum

class Selection(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3

class Outcome(Enum):
    Loss = 0
    Draw = 3
    Win = 6

mappings = {
    "A": Selection.Rock,
    "B": Selection.Paper,
    "C": Selection.Scissors,
    "X": Selection.Rock,
    "Y": Selection.Paper,
    "Z": Selection.Scissors
}

def main():
    total_points = 0
    with open("strategy-guide.txt") as sg:
        rounds = sg.readlines()
        for round in rounds:
            played = round.strip().split(" ")
            player_1 = played[0]
            player_2 = played[1]

            total_points += mappings[player_2].value

            if mappings[player_1] == mappings[player_2]:
                total_points += Outcome.Draw.value
            elif mappings[player_1] - mappings[player_2] == 1 or mappings[player_2] - 2 == mappings[player_1]:
                total_points += Outcome.Loss.value
            else:
                total_points += Outcome.Win.value

        print(total_points)

if __name__ == "__main__":
    main()