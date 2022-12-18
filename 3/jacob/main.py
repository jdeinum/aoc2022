import numpy as np
from typing import Optional, Tuple
from string import ascii_lowercase, ascii_uppercase


def seperate_knapsack(a: str) -> Tuple[str, str]:
    x = int(len(a) / 2)
    return (a[:x], a[x:])


def find_duplicates(a: str, b: str) -> list[str]:
    return list(np.intersect1d(list(a), list(b)))


def test(a: str, x: str) -> None:
    return None


# sum of numbers between 0 and 1000 that are divisible by 3 or 5
def sum_of_multiples_of_3_and_5():
    return sum([x for x in range(1000) if x % 3 == 0 or x % 5 == 0])


def get_value(x: list[str], mapping):

    if len(x) == 0:
        return 0

    return mapping[x]


def create_value_mapping():
    mapping = {}
    for x in range(len(ascii_lowercase)):
        mapping[f"{ascii_lowercase[x]}"] = x + 1

    for x in range(len(ascii_uppercase)):
        mapping[f"{ascii_uppercase[x]}"] = x + 27

    return mapping


def main():

    f = open("test.txt")
    mapping = create_value_mapping()
    total = 0

    for line in f:
        a, b = seperate_knapsack(line.strip())

        dups = find_duplicates(a, b)

        for x in dups:
            total = total + get_value(x, mapping)

    print("total = ", total)


main()
