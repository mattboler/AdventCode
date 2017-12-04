# Find sum of difference between max and min val of each row
import sys

def find_divisor(num_list): # finds two numbers that evenly divide in a list
    for num in num_list:
        for n in num_list:
            if num % n == 0 and num != n:
                divident = num
                divisor = n
        # look for number where num % n = 0
        # store n as divisor, num as divident and break if found
        # otherwise move to next num
    return (divident, divisor)

def main(argv):
    total = 0
    with open('input.txt', 'r') as myfile:
        for line in myfile:
            data = [int(num) for num in line.split()]
            pair = find_divisor(data)
            total = total + int(pair[0]/pair[1])
    print(total)


if __name__ == "__main__":
    main(sys.argv[1:])
