import sys


def load_puzzle(path, input):
    filename = input
    pathname = path + filename
    with open(pathname, "r") as ins:
        tmp = ins.read().split("\n")
        inputlist = [int(i) for i in tmp]
    arraydata = inputlist
    return arraydata


def compute_fuel(data):
    pass
    fuel = int(data/3) - 2
    print(fuel)
    return fuel


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))
    final = 0

    for data in indata:
        final += compute_fuel(data)

    return final


def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle01a) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc-2019_puzzle-01_input.txt'
    print('PARAM: [ ' + param + ' ]')
    path = 'data/puzzle-01/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle01a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
