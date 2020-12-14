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
    match = False
    product = 0
    target = 2020

    indata.sort()
    revdata = sorted(indata, reverse=True)

    for data in indata:
        print('seeking match for: ' + str(data) + ' ')
        for rev in revdata:
            print('  matching: ' + str(rev) + ' ')
            sum = data + rev
            if sum == target:
                product = str(data * rev)
                # print('    PRODUCT:: ' + product + ' ')
                print('** MATCH **')
                match = True
                break
        if match:
            break

    return product

    # find the two entries that sum to 2020
    # then multiply those two numbers together
    #
    # 1721
    # 979
    # 366
    # 299
    # 675
    # 1456
    #
    # In this list, the two entries that sum to 2020 are 1721 and 299.
    # Multiplying them together produces 1721 * 299 = 514579, so the correct answer is 514579.

    return final


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
        param = 'aoc-2020_puzzle-01_input.txt'
    print('PARAM: [ ' + param + ' ]')
    path = 'data/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle00a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
