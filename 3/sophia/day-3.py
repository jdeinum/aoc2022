from string import ascii_lowercase, ascii_uppercase


def generate_mapping():
    lower = {x: ord(x) - 96 for x in ascii_lowercase}
    upper = {x: ord(x) - (64 - 26) for x in ascii_uppercase}
    lower.update(upper)
    return lower


def find_collisions(sack):
    collisions = []
    total = len(sack)
    comp1 = sack[:total // 2:]
    comp2 = sack[total // 2::]
    for item in comp1:
        if item in comp2 and item not in collisions:
            collisions.append(item)
    return collisions


def determine_total(collisions, mapping):
    sum = 0
    for item in collisions:
        sum += mapping[item]
    return sum


def main():
    sum_of_priorities = 0
    mapping = generate_mapping()
    with open("input.txt", "r") as i:
        sacks = i.readlines()
        for sack in sacks:
            sum_of_priorities += determine_total(find_collisions(sack), mapping)
        i.close()
    print(sum_of_priorities)


if __name__ == "__main__":
    main()
