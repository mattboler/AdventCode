# Find sum of difference between max and min val of each row
import sys

def main(argv):
    total = 0
    with open('input.txt', 'r') as myfile:
        for line in myfile:
            data = [int(num) for num in line.split()]
            total = total + max(data) - min(data)
    print(total)


if __name__ == "__main__":
    main(sys.argv[1:])
