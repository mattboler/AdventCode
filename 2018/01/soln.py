# Solution to problem 1 of Advent of Code 2018

INPUT_FILENAME = 'input.txt'

def part_1(filename):
    freq = 0
    with open(INPUT_FILENAME) as f:
        for line in f:
            """ The important thing here is the first character of the line
            will either be a '-' or a '+', and the following characters
            are the decrement/increment amount """
            operator = line[0]
            magnitude = int(line[1:])
            if operator == '+':
                freq += magnitude
            else:
                freq -= magnitude
    return freq


if __name__ == '__main__':
    freq = part_1(INPUT_FILENAME)
    print("Frequency: ", freq)


