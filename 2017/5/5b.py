import sys

def main(argv):
    location = 0
    step = 0
    with open('input.txt', 'r') as myfile:
       instructions = [int(instruction) for instruction in myfile]

    while location < len(instructions):
        offset = instructions[location]
        location = location + offset
        if offset >= 3:
            instructions[location - offset] -= 1
        else:
            instructions[location - offset] += 1
        step += 1
    print(step)


if __name__ == "__main__":
    main(sys.argv[1:])
