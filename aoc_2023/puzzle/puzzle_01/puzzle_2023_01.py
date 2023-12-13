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
    print('---- ------- ---- ---- -------------')
    print('---- process line data: ' + str(data))

    # get first digit value
    # digit_1 = re.search(r'[0-9]', data).group()
    digit_1 = re.search(r'[0-9]', data)
    if digit_1 is not None:
        digit_1 = digit_1.group()
        print(f'digit_1: {digit_1}')
    else:
        print('---- no digits')

    # get last digit value
    reversed_data = "".join(reversed(data))

    # future - handle when there is only one digit in data to avoid 11 22 type duplication
    count_digits = len(re.findall(r'[0-9]', reversed_data))
    print(f'count_digits: {count_digits}')

    digit_2 = re.search(r'[0-9]', reversed_data)
    # future - if digit_2 is not None and count_digits > 1:
    if digit_2 is not None:
        digit_2 = digit_2.group()
        print(f'digit_2: {digit_2}')
    else:
        print('---- no digits')

    # assemble two-digit number
    # future - if digit_1 and digit_2 and count_digits > 1:
    if digit_1 and digit_2:
        line_value = int(digit_1) * 10 + int(digit_2)
    elif digit_1:
        line_value = int(digit_1)
    else:
        line_value = 0
    print(f'line_value: {line_value}')
    return line_value


def pre_sub_digits_for_text(data):
    print('---- pre sub digits in data: ' + str(data))
    new_data = data

    new_data = re.sub('oneight', '18', new_data)
    new_data = re.sub('twone', '21', new_data)
    new_data = re.sub('threeight', '38', new_data)
    new_data = re.sub('fiveight', '58', new_data)
    new_data = re.sub('sevenine', '79', new_data)
    new_data = re.sub('eightwo', '82', new_data)
    new_data = re.sub('eighthree', '83', new_data)
    new_data = re.sub('nineight', '98', new_data)
    new_data = re.sub('zerone', '01', new_data)

    new_data = re.sub('zero', '0', new_data)
    new_data = re.sub('one', '1', new_data)
    new_data = re.sub('two', '2', new_data)
    new_data = re.sub('three', '3', new_data)
    new_data = re.sub('four', '4', new_data)
    new_data = re.sub('five', '5', new_data)
    new_data = re.sub('six', '6', new_data)
    new_data = re.sub('seven', '7', new_data)
    new_data = re.sub('eight', '8', new_data)
    new_data = re.sub('nine', '9', new_data)

    print('---- pre sub returning     : ' + str(new_data))
    return new_data


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))
    item_sum = 0

    for data in indata:
        print('do something with : ' + str(data) + ' ')

        # preprocess input data
        intermediate_data = pre_sub_digits_for_text(data)

        # send line data to be processed.  return will be an integer value.
        data_value = process_input(intermediate_data)

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
