from FileTypes import Directory, File


def main():
    lines = open("input.txt", "r").readlines()

    all_dirs = []
    current_dir = None

    for line in lines:
        if "cd" in line and ".." not in line:
            current_dir = get_directory(line[-2], all_dirs)
        elif "$" not in line and "dir" not in line:
            # add file size
            current_dir.add_contents(File(int(line.split()[0])))
        elif "$" not in line:
            d = get_directory(line.split()[1], all_dirs)
            current_dir.add_contents(d)

    print(get_sums_below_cap(all_dirs))


def get_directory(name, all_dirs):
    new_dir = Directory(name)
    if new_dir not in all_dirs:
        all_dirs.append(new_dir)
        return new_dir
    else:
        index = all_dirs.index(new_dir)
        return all_dirs[index]


def get_sums_below_cap(all_dirs):
    sum_below_cap = 0
    for d in all_dirs:
        d_sum = d.get_size()
        if d_sum <= 100000:
            sum_below_cap += d_sum
    return sum_below_cap


main()
