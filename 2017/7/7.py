import collections, sys, re


def main(argv):
    filename = ''
    if len(sys.argv) == 1:
        filename = 'input.txt'
        testing = False
    else:
        filename = 'test.txt'
        testing = True

# Simply: part one wants the parent program. The parent program is the only program that won't be listed as a child of another.
# So we take the list of all nodes and subtract the list of all children from it.
    weight = {}
    children = {}
    
    with open(filename, 'r') as myfile:
        data = myfile.read()

    for line in data.strip().splitlines():
        name, n, *kids = re.findall(r'\w+', line)
        weight[name] = int(n)
        children[name] = tuple(kids)

# double for loop here: cs is the tuple from children, c is the children from the tuples
    root, = set(weight) - {c for cs in children.values() for c in cs}
    print(root)


if __name__ == "__main__":
    main(sys.argv[1:])
