import numpy as np
import networkx as nx
from collections import defaultdict


def main():
    lines = read_into_array("test.txt")
    parentArray = generateParentArray(lines)
    startRow, startCol = getStart(lines)
    endRow, endCol = getEnd(lines)
    lines[startRow, startCol] = "a"
    lines[endRow, endCol] = "z"
    graph = getGraph(lines)

    print(f"Start: {startRow}, {startCol}")
    print(f"End: {endRow}, {endCol}")

    if startRow == -1 or endRow == -1:
        print("No start or end")
        return

    bfs(graph, (startRow, startCol), (endRow, endCol), parentArray)

    path = backtrack(parentArray, (startRow, startCol), (endRow, endCol))
    print(f"path: {path}")
    print(f"length: {len(path) - 1}")


def getStart(lines):
    for i in range(len(lines)):
        for j in range(len(lines[1])):
            if lines[i][j] == "S":
                return (i, j)

    return (-1, -1)


def getEnd(lines):
    for i in range(len(lines)):
        for j in range(len(lines[1])):
            if lines[i][j] == "E":
                return (i, j)
    return (-1, -1)


# classic bfs
def bfs(graph, start, end, parentArray):
    queue = []
    queue.append(start)
    visited = set()
    visited.add(start)
    while queue:
        node = queue.pop(0)
        if node == end:
            return True
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                parentArray[(neighbour)] = node
                queue.append(neighbour)
    return False


# two nodes are connected if the cost only differs by 1
def getGraph(lines):
    graph = defaultdict(list)
    for i in range(len(lines)):
        for j in range(len(lines[1])):
            if i > 0 and abs(getCost(lines[i][j]) - getCost(lines[i - 1][j])) <= 1:
                graph[(i, j)].append((i - 1, j))
            if (
                i < len(lines) - 1
                and abs(getCost(lines[i][j]) - getCost(lines[i + 1][j])) <= 1
            ):
                graph[(i, j)].append((i + 1, j))
            if j > 0 and abs(getCost(lines[i][j]) - getCost(lines[i][j - 1])) <= 1:
                graph[(i, j)].append((i, j - 1))
            if (
                j < len(lines[1]) - 1
                and abs(getCost(lines[i][j]) - getCost(lines[i][j + 1])) <= 1
            ):
                graph[(i, j)].append((i, j + 1))

    return graph


# the parent dict is initialized to "N"
def generateParentArray(lines):
    parent = {}
    for i in range(len(lines)):
        for j in range(len(lines[1])):
            parent[(i, j)] = "N"
    return parent


def read_into_array(filename):
    f = open(filename, "r")
    lines = f.readlines()
    lines = [list(x.strip()) for x in lines]
    f.close()
    return np.array(lines)


def getCost(character):
    return ord(character) - 64


def backtrack(parentArray, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parentArray[current]
    path.append(start)
    path.reverse()
    return path


if __name__ == "__main__":
    main()
