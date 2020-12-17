import sys
from collections import Counter

def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        tmp = ins.read().split("\n")
        input_set = [str(i) for i in tmp]
    arraydata = input_set
    return arraydata


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))
    final = ''
    passing = 0
    val_check_lower = False
    val_check_upper = False

    for data in indata:
        # print('input: ' + str(data) + ' ')
        data_line = data.split(" ")
        print(data_line)

        policy_vals = data_line[0]
        policy_vals_lower = int(policy_vals.split('-')[0])
        policy_vals_upper = int(policy_vals.split('-')[1])

        policy_char = data_line[1].split(':')[0]
        password = data_line[2]

        print('policy char       :: ' + str(policy_char))

        print('policy vals lower :: ' + str(policy_vals_lower))
        print('policy vals upper :: ' + str(policy_vals_upper))

        print('password lo pos   :: ' + password[policy_vals_lower-1])
        print('password hi pos   :: ' + password[policy_vals_upper-1])

        if policy_char in password[policy_vals_lower-1]:
            val_check_lower = True

        if policy_char in password[policy_vals_upper-1]:
            val_check_upper = True

        print('val_check_lower   :: ' + str(val_check_lower))
        print('val_check_upper   :: ' + str(val_check_upper))

        if False:
            print('pass')
            passing += 1
        else:
            print('fail')

    final = passing
    return final


def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle02b) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc_2020_puzzle_02_input.txt'
    print('PARAM: [ ' + param + ' ]')
    path = 'data/puzzle_02/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle02b) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
