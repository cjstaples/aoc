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

    for data in indata:
        # print('input: ' + str(data) + ' ')
        data_line = data.split(" ")
        print(data_line)

        policy_range = data_line[0]
        policy_range_lower = int(policy_range.split('-')[0])
        policy_range_upper = int(policy_range.split('-')[1])

        policy_char = data_line[1].split(':')[0]
        password = data_line[2]

        policy_char_count = password.count(policy_char)
        print('policy char count :: ' + str(policy_char_count))

        if policy_range_lower <= policy_char_count <= policy_range_upper:
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
    print('(puzzle02a) main:')
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
    print('(puzzle02a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
