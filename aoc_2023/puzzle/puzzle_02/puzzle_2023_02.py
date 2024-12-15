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


def solve_puzzle(indata):
    # print('-- solving for ' + str(indata))
    item_sum = 0

    for data in indata:
        # print('do something with : ' + str(data) + ' ')

        # parse data line (game) into sections:
        # game number, prior to the first ':'
        # game set, prior to the next ';' or eol
        # until no more game sets
        game_number = 0
        max_red = 0
        max_blue = 0
        max_green = 0

        line = re.split(':|;', data)
        print(line)
        game_number = re.search(r'\d+', line[0]).group()
        for lineitem in line:
            print(lineitem)
            # each line item match separately for red blue green


        print(f'  game_number : {game_number}')
        print(f'  max_red     : {max_red}')
        print(f'  max_blue    : {max_blue}')
        print(f'  max_green   : {max_green}')
        print(f'------------  : ----------')
        # item_sum = item_sum + int(data)
    return item_sum


# noinspection DuplicatedCode
def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle_2023-02a) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc_2023_puzzle_02_input.txt'
    print(f'PARAM: [ {param} ]')
    path = 'data/puzzle_02/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle_2023-02a) end::')
    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
