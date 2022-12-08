class File:
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


class Directory:
    def __init__(self, name):
        self.name = name
        self.contents = []
        self.size = 0

    def add_contents(self, contents):
        self.contents.append(contents)

    def get_size(self):
        t_sum = 0
        for item in self.contents:
            t_sum += item.get_size()
        return t_sum

    def __eq__(self, other):
        return self.name == other.name
