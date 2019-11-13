# Solution to problem 1 of Advent of Code 2018

INPUT_FILENAME = 'input.txt'

def adjust_freq(line, freq):
    operator = line[0]
    magnitude = int(line[1:])
    if operator == '+':
        return freq + magnitude
    else:
        return freq - magnitude

def part_1(filename):
    freq = 0
    with open(filename) as f:
        for line in f:
            """ The important thing here is the first character of the line
            will either be a '-' or a '+', and the following characters
            are the decrement/increment amount """
            freq = adjust_freq(line, freq)
    return freq

def part_2(filename):
    freq = 0
    frequencies = {freq}
    """ Testing: Run through for just first iteration of file"""
    while True:
        with open(filename) as f:
            for line in f:
                freq = adjust_freq(line, freq)
                if freq in frequencies:
                    return freq
                else:
                    frequencies.add(freq)
    print(sorted(frequencies))

    return 'lol'


if __name__ == '__main__':
    freq = part_1(INPUT_FILENAME)
    print("Frequency: (Part 1)", freq)

    freq = part_2(INPUT_FILENAME)
    print("Frequency: (Part 2)", freq)
