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
        print(row)

        rowchecksum = checksum_row(row)
        print('rowchecksum = ', rowchecksum)
        total = total + rowchecksum
        print('running total = ', total)
        print()

    return (total)


def checksum_row(rowdata):
    minentry = int(sys.maxsize)
    maxentry = 0

    for entry in rowdata:
        print('entry = ', entry, 'min = ', minentry, 'max = ', maxentry)
        if int(entry) > maxentry:
            maxentry = int(entry)
        if int(entry) < minentry:
            minentry = int(entry)

    rowcx = maxentry - minentry
    return rowcx


def show_puzzle(output):
    print(output)


def main():
    print('(puzzle02a) main:')
    print

    mydata = load_puzzle()

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print

    print
    print('(puzzle02a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
