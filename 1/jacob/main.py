def main():
    with open("test.txt", "r") as f:
        current_max = 0
        current = 0
        for line in f:
            if not line.strip():

                if current > current_max:
                    current_max = current

                current = 0
                continue

            current = current + int(line.strip())

        print(current_max)


main()
