import sys


def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        tmp = ins.read().split("\n")
        input_set = [int(i) for i in tmp]
    arraydata = input_set
    return arraydata


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))
    final = 0

    return final


def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle03a) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc-2019_puzzle-03_input.txt'
    print('PARAM: [ ' + param + ' ]')
    path = 'data/puzzle-03/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle03a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
