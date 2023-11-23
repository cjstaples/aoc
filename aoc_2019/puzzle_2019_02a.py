import sys


def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        tmp = ins.read().split(",")
        input_set = [int(i) for i in tmp]
    arraydata = input_set
    return arraydata


def execute_program(program_code):
    print('----')
    for index, code in enumerate(program_code):
        if index % 4 == 0:
            opcode = program_code[index]

            if opcode == 1:
                ptr_1 = program_code[index + 1]
                ptr_2 = program_code[index + 2]
                value_1 = program_code[ptr_1]
                value_2 = program_code[ptr_2]
                ptr_output = program_code[index + 3]
                old_value = program_code[ptr_output]
                new_value = program_code[ptr_1] + program_code[ptr_2]
                program_code[ptr_output] = new_value
            elif opcode == 2:
                ptr_1 = program_code[index + 1]
                ptr_2 = program_code[index + 2]
                value_1 = program_code[ptr_1]
                value_2 = program_code[ptr_2]
                ptr_output = program_code[index + 3]
                old_value = program_code[ptr_output]
                new_value = program_code[ptr_1] * program_code[ptr_2]
                program_code[ptr_output] = new_value
            elif opcode == 99:
                return program_code
            else:
                break

            print('opcode:: %3d, Ptr_1::%3d, Ptr_2::%3d, Val_1::%3d, Val_2::%3d' % (opcode, ptr_1, ptr_2, value_1, value_2))
            print(':::::::: (TARGET::%3d) old_value::%3d ==> new_value::%3d' % (ptr_output, old_value, new_value))

    return program_code

def parse_program(indata):
    program_code = []
    for data in indata:
        program_code.append(data)

    for index, code in enumerate(program_code):
        if index % 4 == 0:
            print('----')
            name='OPCD'
        elif index % 4 == 1:
            name = 'VAL1'
        elif index % 4 == 2:
            name = 'VAL2'
        elif index % 4 == 3:
            name='DEST'
        print('Index: %3d, ::%4s:: %3d' % (index, name, code))
    return program_code


def solve_puzzle(indata):
    print('-- solve for: ' + str(indata))

    program_code = parse_program(indata)

    program_code = execute_program(program_code)

    return program_code


def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle02a) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc-2019_puzzle-02_input.txt'
    print('PARAM: [ ' + param + ' ]')
    path = 'data/puzzle-02/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle02a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
