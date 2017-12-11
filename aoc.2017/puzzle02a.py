import sys
import csv

def load_puzzle():

    with open("aoc-2017_puzzle-2_input.txt", "r") as ins:
#    with open("file2a.txt", "r") as ins:
        tmp = ins.read().split("\n")
        arraydata = [i.split("\t") for i in tmp]

    return arraydata


def solve_puzzle(indata):
#    print indata
    total = 0
    for row in indata:
        print row

        rowchecksum = checksum_row(row)
        print 'rowchecksum = ',rowchecksum
        total = total + rowchecksum
        print 'running total = ', total
        print

    return (total)

def checksum_row(rowdata):
    min = int(sys.maxsize)
    max = 0

    for entry in rowdata:
        print 'entry = ',entry,'min = ',min,'max = ',max
        if int(entry) > max:
            max = int(entry)
        if int(entry) < min:
            min = int(entry)

    rowcx = max - min
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



