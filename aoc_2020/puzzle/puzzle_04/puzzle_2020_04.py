import sys


def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        tmp = ins.read().split("\n")
        input_set = [i for i in tmp]
    arraydata = input_set
    return arraydata


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))

    for data in indata:
        print('do something with : ' + str(data) + ' ')
        if False:
            break

    return False


def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle04a) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc_2020_puzzle_04_input.txt'
    print('PARAM: [ ' + param + ' ]')
    path = 'data/puzzle_04/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle04a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
