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
import re

def main(argv):
    filename = ''
    if len(sys.argv) == 1:
        filename = 'input.txt'
    else:
        filename = 'test.txt'

    with open(filename, 'r') as myfile:
        data=myfile.read()



    for line in data.strip().splitlines():
        score = 0
        nest_depth = 0
        garbage = 0
        # preprocess to remove ! and the character immediately after
        no_excl_string = re.sub(r'\!.', '', line)
        index = 0
        while index < len(no_excl_string):
            if no_excl_string[index] == '<':
                index += 1
                while no_excl_string[index] != '>':
                    garbage += 1
                    index += 1
            elif no_excl_string[index] == '{':
                nest_depth += 1
            elif no_excl_string[index] == '}':
                score += nest_depth
                nest_depth -= 1
            index += 1

        # now count groups and points
        print(score)
        print(garbage)

if __name__ == '__main__':
    main(sys.argv[1:])
