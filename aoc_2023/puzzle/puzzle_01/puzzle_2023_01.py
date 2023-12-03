import sys
import re


def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        # tmp = ins.read().split("\n")
        tmp = ins.read().splitlines()
        # input_set = [int(i) for i in tmp]

    return tmp


def process_input(data):
    print('---- process line data: ' + str(data))

    # get first digit value
    digit_1 = re.search(r'[0-9]+', data).group()
    print(f'digit_1: {digit_1}')

    # get last digit value
    reversed_data = "".join(reversed(data))
    digit_2 = re.search(r'[0-9]+', reversed_data).group()
    print(f'digit_2: {digit_2}')

    # assemble two-digit number
    line_value = int(digit_1) * 10 + int(digit_2)
    print(f'line_value: {line_value}')
    return line_value


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))
    item_sum = 0

    for data in indata:
        print('do something with : ' + str(data) + ' ')

        # send line data to be processed.  return will be an integer value.
        data_value = process_input(data)

        item_sum = item_sum + data_value
        print(f'running total: {item_sum}')
    return item_sum


# noinspection DuplicatedCode
def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle_2023-01a) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc_2023_puzzle_01_input.txt'
    print(f'PARAM: [ {param} ]')
    path = 'data/puzzle_01/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle_2023-01a) end::')
    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
