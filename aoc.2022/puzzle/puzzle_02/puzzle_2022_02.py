import sys


def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        # tmp = ins.read().split("\n")
        tmp = ins.read().splitlines()

    return tmp


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))

    for data in indata:
        print('do something with : ' + str(data) + ' ')

    return False


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
        param = 'aoc_2022_puzzle_02_input.txt'
    print(f'PARAM: [ {param} ]')
    path = 'data/puzzle_02/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle02a) end::')
    return mysolution


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
