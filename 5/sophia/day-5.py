stacks = {}


def main():
    with open("input.txt", "r") as stack_file:
        line = generate_stacks(stack_file)
        shift_boxes_around(line, stack_file)
        print_tops()


def get_box_present(boxes):
    for box in boxes:
        if box[0] == "[" and box[2] == "]":
            return True
    return False


def generate_stacks(input_file):
    line = input_file.readline()
    while 1:
        # reached end of stack layout, return line of file
        if line.find("[") < 0:
            for x in range(2):
                line = input_file.readline()
            return line

        boxes = []
        for i in range(0, len(line), 4):
            boxes.append(line[i:i+4])

        add_boxes_to_stack(boxes)
        line = input_file.readline()


def add_boxes_to_stack(boxes):
    empty = " " * 4
    stack_num = 1

    for box in boxes:
        current_stack = stacks.get(stack_num)
        if len(box) > 0 and box != empty and current_stack is None:
            stacks[stack_num] = [box[1]]
        elif len(box) > 0 and box != empty:
            current_stack.append(box[1])
        stack_num += 1


def shift_boxes_around(line, stack_file):
    while line != "":
        instructions = [int(x) for x in line.strip().split(" ")[1::2]]
        move_box(instructions)
        line = stack_file.readline()


def move_box(instructions):
    for i in range(instructions[0]):
        source = stacks.get(instructions[1])
        dest = stacks.get(instructions[2])
        dest.insert(0, source.pop(0))


def print_tops():
    for i in range(len(stacks)):
        print(f"Top Box of Stack {i+1} is [{stacks.get(i+1)[0]}]")


if __name__ == "__main__":
    main()
