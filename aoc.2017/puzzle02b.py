import itertools
import sys


def load_puzzle():
    #    with open("data/aoc-2017_puzzle-2_input_test.txt", "r") as ins:
    with open("data/aoc-2017_puzzle-2_input.txt", "r") as ins:
        tmp = ins.read().split("\n")
        arraydata = [i.split("\t") for i in tmp]

    return arraydata


def solve_puzzle(indata):
    #    print indata
    total = 0
    for row in indata:
        print 'row: ', row

        divcheck = divcheck_row(row)
        print 'row divcheck = ', divcheck
        total = total + divcheck
        print 'running total = ', total
        print

    return (total)


def divcheck_row(rowdata):
    rowresult = 0
    print 'rowdata: ', rowdata

    for a, b in itertools.permutations(rowdata, 2):
        a = int(a)
        b = int(b)
        modresult = a % b
        divresult = a / b
        print 'combo: ', a, b, ' -- ', 'div: ', divresult, 'mod: ', modresult
        if modresult == 0:
            rowresult = divresult

    return rowresult


def show_puzzle(output):
    print(output)


def main():
    print('(puzzle02b) main:')
    print

    mydata = load_puzzle()
    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print

    print
    print('(puzzle02b) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
