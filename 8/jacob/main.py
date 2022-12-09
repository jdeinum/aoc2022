import numpy as np
import functools
from nptyping import NDArray, Bool


def parse_input():
    with open("test.txt") as f:
        res = []
        for line in f:
            line = list(line.strip())

            res.append(line)

        return np.array(res)


def count_outer(trees: NDArray):
    return functools.reduce(lambda a, b: 2 * a + 2 * b - 4, trees.shape)


# a tree is visible if it can see outside of the square
# so we need to check if there is a line where each element is smaller than
# the target tree that reaches the outside
def isVisible(trees: NDArray, tree: tuple[int, int]):

    row, column = tree
    val = trees[row, column]

    return np.any(
        [
            # same row to the left
            allSmaller(trees[row, 0:column], val),
            # same row to the right
            allSmaller(trees[row, column + 1 :], val),
            # same column going up
            allSmaller(trees[0:row, column], val),
            # same column going down
            allSmaller(trees[row + 1 :, column], val),
        ]
    )


def allSmaller(line: NDArray, val: int) -> bool:
    return np.all(line < val)


def count_inner(trees: NDArray) -> int:
    nrows = trees.shape[0]
    ncols = trees.shape[1]
    tuples = [(x, y) for x in range(1, nrows - 1) for y in range(1, ncols - 1)]
    a = functools.partial(isVisible, trees)
    res = list(map(a, tuples))
    return np.count_nonzero(res)


def main():

    trees = parse_input()

    outer = count_outer(trees)

    inner = count_inner(trees)

    print(f"total: {outer + inner}")


if __name__ == "__main__":
    main()
