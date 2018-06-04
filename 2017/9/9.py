# you have in input string that contains groups, which are defined as text
# between { and }
# within a group, there are zero or more other things separated by commas;
# either other groups or garbage.
# any } will close the most recently opened {.
# Garbage begins with < and ends with >.
# In your input, any character than comes after a ! is ignored.
# Examples:
# - <> empty garbage
# - <random characters> garbage containing random characters
# - <<<<> garbage, because the extra <s are ignored
# - <{!>}> garbage, because the first > is cancelled
# - <!!> garbage, because the first ! cancels the second
# - <!!!>> garbage, second ! and first > are cancelled
# - <{o"i!a,<{i<a> garbage, ends at first >
# - {} 1 group
# - {{{}}} 3 groups
# - {{},{}} also 3 groups
# - {{{},{},{{}}}} 6 groups
# - {<{},{},{{}}>} 1 group which contains garbage
# - {{<a>},{<a>},{<a>},{<a>}} 5 groups
# - {{<!>},{<!>},{<!>},{<a>}} 2 groups

# Your goal is to find the total score of all of the groups in your input.
# Each group is assigned a score that's 1 more than the score of the group
# containing it. (outermost group has score of 1)

# - {} score of 1
# - {{{}}} score of 1 + 2 + 3 = 6
# - {{{},{},{{}}}} score of 1 + 2 + 3 + 3 + 3 + 4 = 16
# - {<a>,<a>,<a>,<a>} score of 1

# personal notes: input is taken in as one line.

import sys

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def remove_exclamations(str):
    excl_ind = str.find('!')
    if excl_ind == -1:
        return str
    else:
        prefix = str[:excl_ind]
        suffix = remove_exclamations(str[(excl_ind+2):])
        return prefix + suffix

def remove_garbage(str):
    garbage_entry = str.find('<')
    garbage_exit = str.find('>')
    if garbage_entry == -1:
        return str
    else:
        prefix = str[:garbage_entry]
        suffix = str[(garbage_exit+1):]
        return remove_garbage(prefix + suffix)

def process_brackets(str, stack, val = None, sum = None):
    if val == None:
        val = 0
    if sum == None:
        sum = 0
    if len(str) == 0:
        return sum
    else:
        if str[0] == '{':
            stack.push(val+1)
            return process_brackets(str[1:], stack, val+1, sum)
        elif str[0] == '}':
            sum += stack.pop()
            return process_brackets(str[1:], stack, val-1, sum)
        else:
            return process_brackets(str[1:], stack, val, sum)

def main(argv):
    filename = ''
    if len(sys.argv) == 1:
        filename = 'input.txt'
    else:
        filename = 'test.txt'

    with open(filename, 'r') as myfile:
        data=myfile.read()

    for line in data.strip().splitlines():
        # preprocess to remove !s and the character immediately after
        no_excl_string = remove_exclamations(line)
        # then remove everything between < and >
        cleaned_string = remove_garbage(no_excl_string)
        # now count groups and points
        s = Stack()
        sum = process_brackets(cleaned_string, s)
        print(sum)

if __name__ == '__main__':
    main(sys.argv[1:])
