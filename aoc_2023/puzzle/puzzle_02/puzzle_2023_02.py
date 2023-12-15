import sys


def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        # tmp = ins.read().split("\n")
        tmp = ins.read().splitlines()
        # input_set = [int(i) for i in tmp]

    return tmp


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))
    item_sum = 0

    for data in indata:
        print('do something with : ' + str(data) + ' ')
        item_sum = item_sum + int(data)
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
