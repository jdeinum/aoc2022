def main():
    with open("input.txt", "r") as i:
        collisions = 0
        pairs = i.readlines()
        for pair in pairs:
            jobs = pair.split(",")
            elf1 = get_sections(jobs, 0)
            elf2 = get_sections(jobs, 1)
            if all(job in elf1 for job in elf2) or all(job in elf2 for job in elf1):
                collisions += 1
        i.close()

    print(collisions)

def get_sections(jobs, index):
    sections = jobs[index].split("-")
    return [x for x in range(int(sections[0]), int(sections[1]) + 1)]

if __name__ == "__main__":
    main()