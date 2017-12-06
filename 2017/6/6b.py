import sys

def distribute(mem_list, index, blocks):
    # Distribute 1 block to next index, wrapping if reach end of list
    if blocks == 0:
        return mem_list
    else:
        mem_list[(index + 1) % len(mem_list)] += 1
        return distribute(mem_list, index + 1, blocks -1)

def find_bank(mem_list):
    # Find bank to redistribute: always pick largest (ties won by lowest-numbered bank)
    # return index of bank
    return mem_list.index(max(mem_list))

def iterate(mem_list):
# find largest bank and distribute
    index = find_bank(mem_list)
    blocks = mem_list[index]
    mem_list[index] = 0
    return distribute(mem_list, index, blocks)

def main(argv):
    if len(sys.argv) == 1:
        with open('input.txt', 'r') as myfile:
            for line in myfile:
               in_string = line
        testing = False
    elif sys.argv[1] == "test":
        testing = True
        in_string = "0 2 7 0"
    else:
        testing = False
        in_string = str(sys.argv[1])

    data = [int(num) for num in in_string.split()]

    if testing:
        if distribute([0, 2, 0, 0], 2, 7) == [2, 4, 1, 2] and distribute([2, 0, 1, 2], 1, 4) == [3, 1, 2, 3]:
            print("distribute passes!")
        if find_bank([0, 2, 7, 0]) == 2 and find_bank([3, 1, 2, 3]) == 0:
            print("find_bank passes!")
        if iterate([0, 2, 7, 0]) == [2, 4, 1, 2] and iterate([2, 4, 1, 2]) == [3, 1, 2, 3]:
            print("iterate passes!")
    else:
        num_iterations = 0
        first_time = 0
        history = []
        found = False
        while not found:
            data = iterate(data)
            found = data in history
            history.append(data[:])
            num_iterations += 1
        first_time = history.index(data) + 1


        print("Total iterations: ", num_iterations)
        print("length of loop: ", num_iterations - first_time)

if __name__ == "__main__":
    main(sys.argv[1:])
