def main():
    with open("input.txt","r") as i:
        lines = i.readlines()
        for line in lines:
            parse_string(line)

def parse_string(line):
    start_marker = set()
    final_index = None
    for i in range(len(line)):
        for j in range(4):
            final_index = i+j+1
            start_marker.add(line[i+j])
        if len(start_marker) == 4:
            print(final_index)
            break
        else:
            start_marker = set()

main()