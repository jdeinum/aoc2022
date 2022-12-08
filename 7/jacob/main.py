import numpy as np


class Directory:
    total_size = 0
    name = None

    def __init__(self, name):
        self.name = name
        self.subdirectory = []

    def addFile(self, size):
        self.total_size += float(size)

    def addSubdirectory(self, directory):
        self.subdirectory.append(directory)

    def isSmallEnough(self) -> bool:
        return self.total_size < 100000

    def updateTotal(self, mapping):
        self.total_size += sum(
            [mapping[x].getTotal(mapping) for x in self.subdirectory]
        )

    def getTotal(self, mapping) -> int:

        if self.isSmallEnough():
            return self.total_size + sum(
                [mapping[x].getTotal(mapping) for x in self.subdirectory]
            )

        else:
            return sum([mapping[x].getTotal(mapping) for x in self.subdirectory])


def read_lines(filename: str) -> list[list[str]]:
    f = open(filename)
    x = []
    for line in f:
        split = line.strip().split(" ")
        x.append(split)

    return x


def isChange(line):
    return line[1] == "cd"


def isAbsolute(line):
    return line[2] != ".."


def isFile(line):
    return line[0].isnumeric()


def isDir(line):
    return line[0] == "dir"


def isLS(line):
    return line[1] == "ls"


def getName(line):
    return line[2]


def getTotal(mapping):

    for dir in mapping.values():
        dir.updateTotal(mapping)

    start = mapping["/"]
    return start.getTotal(mapping)


def solve(lines: list[list[str]]):
    tree = []
    mapping = {}

    for line in lines:

        # absolute change, add directory to mapping if it doesn't exist
        if isChange(line) and isAbsolute(line):
            name = getName(line)
            if mapping.get(name) == None:
                mapping[name] = Directory(name)

            tree.append(name)

        elif isChange(line) and not isAbsolute(line):
            tree.pop()

        elif isDir(line):
            mapping[tree[-1]].addSubdirectory(line[1])

        elif isFile(line):
            mapping[tree[-1]].addFile(line[0])

        elif isLS(line):
            pass

    print(getTotal(mapping))


def main():
    lines = read_lines("test.txt")
    solve(lines)


if __name__ == "__main__":
    main()
