# Find the sum of all digits that match the next digit in the list.
# The list is circulat, so the digit after the last digit is the first digit in the list
import sys

def sumChar(char1, char2):
    if char1 == char2:
        return int(char1)
    else: 
        return 0

def main(argv):

    if len(sys.argv) == 1:
            with open('input.txt', 'r') as myfile:
                input_string = myfile.read().replace('\n','')
    else:
        input_string = str(sys.argv[1])

    end = len(input_string)

    total = 0

    for index in range(len(input_string)):
        if index >= end/2:
            total += sumChar(input_string[index], input_string[int(index - (end/2))])
        else:
            total += sumChar(input_string[index], input_string[index + int((end/2))])

    print(total)

if __name__ == "__main__":
    main(sys.argv[1:])
