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

    elf_calories = []
    for data in indata:
        # incoming data is a list of lists
        # each list contains 1+ integers
        # sum each list
        # add sum to list of total calories
        print('do something with : ' + str(data) + ' ')

        item_sum = 0
        for item in data:
            item_sum = item_sum + int(item)

    return item_sum


def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle00a) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc_2022_puzzle_00_input.txt'
    print(f'PARAM: [ {param} ]')
    path = 'data/puzzle_00/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle00a) end::')
    return mysolution


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
