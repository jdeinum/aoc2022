import numpy as np
from itertools import islice
import re

# move 1 crate from stack1 to stack2
def move_crate(stack1: list[str], stack2: list[str]):
    if len(stack1) > 0:
        stack2.append(stack1.pop())


def parse_input():
    f = open("test.txt")
    start = []
    moves = []
    for line in f:

        if not line.strip():
            break

        start.append(line.replace("\n", "").split(" "))

    for line in f:
        moves.append(line.replace("\n", "").split(" "))

    return start, moves


def get_inital_stacks(lines: list[list[str]]):
    stack1 = []
    stack2 = []
    stack3 = []
    stacks = [stack1, stack2, stack3]

    for row in lines:
        for i in range(0, len(row), 3):
            a = row[i : i + 3]

            for k in range(len(a)):

                if not a[k]:
                    continue
                else:
                    stacks[k].insert(0, a[k][1])

    return stacks


def parse_moves(moves):
    m = []
    for move in moves:
        m.append(list(map(int, [move[1], move[3], move[5]])))
    return m


def main():
    start, moves = parse_input()
    stack = get_inital_stacks(start[:-1])
    actions = parse_moves(moves)

    for times, start, end in actions:
        for _ in range(times):
            move_crate(stack[start - 1], stack[end - 1])

    print([x[-1] for x in stack])


if __name__ == "__main__":
    main()
