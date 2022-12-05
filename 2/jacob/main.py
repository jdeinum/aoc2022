import numpy as np

def play_score(letter: str) -> int:
    return ord(letter) - ord("A") + 1

def outcome_score(a: str, b:str, mapping) -> int:
    return mapping[f"{a}{b}"]

def generate_score(a: str, b: str, mapping):
    return play_score(a) + outcome_score(a,b, mapping)

def generate_outcome_scores():
    options = np.array(["A", "B", "C"])
    responses = np.array(["X", "Y", "Z"])

    mapping = {}

    # roll 0 = score of 3
    # roll 1 = score of 6
    # roll 2 = score of 1
    x = {0:3, 1:6, 2:0}
    for i in range(3):
        a = np.roll(responses, i)

        for j in range(3):
            mapping[f"{options[j]}{a[j]}"] = x[i] 



    return mapping



def main():

    a = generate_outcome_scores()

    f = open("test.txt")
    total = 0
    for line in f:
        split = line.strip().split(" ")
        total = total + generate_score(split[0], split[1], a)

    print(total)


main()


