def generate_mapping():
    mapping = {}
    value = 1
    current = 'a'
    last = 'z'
    while current <= last:
        mapping[current] = value
        value += 1
        current = chr(ord(current) + 1)
        if current == 'Z':
            mapping[current] = value
            break
        if current > last:
            current = 'A'
            last = 'Z'
    return mapping


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
    with open("input.txt","r") as i:
        sacks = i.readlines()
        for sack in sacks:
            sum_of_priorities += determine_total(find_collisions(sack), mapping)
        i.close()
    print(sum_of_priorities)


if __name__ == "__main__":
    main()