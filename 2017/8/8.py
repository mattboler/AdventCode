# you have a computer that gives instructions like so:
# register to modify, whether to increase or decrease that register's value, the amount by which to inc/dec, and a condition
# all registers start at 0

# You recieve instructions in the form:
# b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10

# I'm not going to use the 'eval' cheat or anything similar.

# instruction is of form (register) (+/-) (val) if (register) (condition) (val)

# steps: for first register, if first time being seen add an entry to a dictionary with name of register and value 0
# find true/false val of condition
# use switch to process instruction if condition is true
import sys

# string, string, int -> boolean
# tell if condition fails or passes

def process_condition(register_value, condition, value):
    if condition == "==":
        return register_value == value
    elif condition == ">=":
        return register_value >= value
    elif condition == "<=":
        return register_value <= value
    elif condition == ">":
        return register_value > value
    elif condition == "<":
        return register_value < value
    elif condition == "!=":
        return register_value != value

# string, dict -> int
# retreive value of register, if register not in registers add with value of 0

def retreive_register(name, registers):
    if name not in registers:
        registers[name] = 0
    return registers[name]

# string, int, dict -> none
# write value to register

def write_register(name, value, registers):
    registers[name] = value

# string, dict -> None
# Process the instruction and change the registers accordingly

def process_instruction(instruction, registers):
    instruction_list = [string for string in instruction.split()]

    active_register = instruction_list[0]
    active_register_value = retreive_register(active_register, registers)

    check_register = instruction_list[4]
    check_register_value = retreive_register(check_register, registers)

    if process_condition(check_register_value, instruction_list[5], int(instruction_list[6])):
        if instruction_list[1] == "inc":
            active_register_value += int(instruction_list[2])
        else:
            active_register_value -= int(instruction_list[2])

        write_register(active_register, active_register_value, registers)

def main(argv):
    filename = ''

    if len(sys.argv) == 1:
        filename = 'input.txt'
    else:
        filename = 'test.txt'

    with open(filename, 'r') as myfile:
        data = myfile.read()

    register_dict = {}
    max_vals = []

    for instruction in data.strip().splitlines():
        process_instruction(instruction, register_dict)
        max_vals.append(max([i for i in register_dict.values()]))

    print("Max val at end: " + str(max([i for i in register_dict.values()])))
    print("Max val ever: " + str(max(max_vals)))


if __name__ == "__main__":
    main(sys.argv[1:])
