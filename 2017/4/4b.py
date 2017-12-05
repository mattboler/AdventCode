import sys

def main(argv):
    total = 0
    with open('input.txt', 'r') as myfile:
        for line in myfile:
            passphrase = [''.join(sorted(word)) for word in line.split()]
            
            if len(passphrase) == len(set(passphrase)):
                total += 1

    print(total)

if __name__ == "__main__":
    main(sys.argv[1:])

