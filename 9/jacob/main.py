import numpy as np
from scipy.spatial import distance
import math
import operator


class Mover:
    def __init__(self):
        self.pos = (4, 0)

    def move(self, new_pos: tuple[int, int]):
        self.pos = new_pos


class Grid:
    def __init__(self, moves, head, tail):
        start = np.ones((5, 6))
        start[4, 0] = 2
        self.board = start
        self.mapping = {1: ".", 2: "V"}
        self.moves = moves
        self.head = head
        self.tail = tail

    def print_board(self):
        board = np.vectorize(self.mapping.get)(self.board)

        if self.head.pos == self.tail.pos:
            board[self.head.pos] = "B"

        else:
            board[self.head.pos] = "H"
            board[self.tail.pos] = "T"

        print(board)

    def adjust_grid(self):
        trow, tcol = self.tail.pos
        if self.board[trow, tcol] != 2:
            self.board[trow, tcol] = 2

    def adjust_tail(self, last_direction: str):

        if last_direction == "U":
            self.tail.move(tuple(map(operator.add, self.head.pos, (1, 0))))
        if last_direction == "D":
            self.tail.move(tuple(map(operator.add, self.head.pos, (-1, 0))))
        if last_direction == "R":
            self.tail.move(tuple(map(operator.add, self.head.pos, (0, -1))))
        if last_direction == "L":
            self.tail.move(tuple(map(operator.add, self.head.pos, (0, 1))))

        self.adjust_grid()

    def currentDistance(self):
        hrow, hcol = self.head.pos
        trow, tcol = self.tail.pos
        return math.sqrt((hrow - trow)**2 + (hcol - tcol)**2)

    def make_single_move(self, direction: str):

        old_row, old_col = self.head.pos

        if direction == "U":
            self.head.move((old_row - 1, old_col))

        elif direction == "D":
            self.head.move((old_row + 1, old_col))

        elif direction == "L":
            self.head.move((old_row, old_col - 1))

        elif direction == "R":
            self.head.move((old_row, old_col + 1))

        if self.currentDistance() >= 2:
            self.adjust_tail(direction)

    def make_move(self, direction: str, value: int):

        # print(f"Making move: {direction} | {value}")

        for _ in range(abs(value)):
            self.make_single_move(direction)
            # self.print_board()

    def run(self):
        for move in self.moves:
            self.make_move(move[0], move[1])

        print(f"num positions: {len(np.where(self.board.flatten() == 2 )[0])}")


def parse_input() -> list[str, int]:
    with open("test.txt") as f:
        res = []
        for line in f:
            direction, spaces = line.strip().split(" ")
            spaces = int(spaces)
            res.append((direction, spaces))

        return res


def main():
    moves = parse_input()
    head = Mover()
    tail = Mover()
    sim = Grid(moves, head, tail)
    # sim.print_board()
    sim.run()


if __name__ == "__main__":
    main()
