import numpy as np


def isContained(a1, a2):
    if np.all(np.isin(a1, a2)):
        return True

    return False


def get_range(a: str):
    first, second = map(int, a.split("-"))
    return np.arange(first, second, 1)


def run(filename):
    f = open(filename)
    total = 0
    for line in f:
        first, second = line.strip().split(",")
        range1 = get_range(first)
        range2 = get_range(second)

        if isContained(range1, range2) or isContained(range2, range1):
            total = total + 1

    f.close()
    return total


def main():
    print("total = ", run("test.txt"))


if __name__ == "__main__":
    main()
