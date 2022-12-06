def moving_window(s_input: str):
    for i in range(0, len(s_input), 1):
        if len(set(list(s_input[i : i + 4]))) == 4:
            return i + 4


def main():
    with open("test.txt") as f:
        for line in f:
            print(moving_window(line))


if __name__ == "__main__":
    main()
