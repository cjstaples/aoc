import sys
import hashlib


#   AOC
#   --- Day 6: Memory Reallocation ---


def load_puzzle():
    with open("data/aoc-2017_puzzle-6_test.txt", "r") as ins:
        #   with open("data/aoc-2017_puzzle-6_input.txt", "r") as ins:
        tmp = ins.read().split("\n")
        inputlist = [i.split("\t") for i in tmp]

    #    inputlist = ['a', 'b', 'c']
    return inputlist


def solve_puzzle(inputlist):
    #
    final = 0
    #   talk it through...
    #   get set of banks from input
    #
    #   get checksum for the current set of banks
    #   add checksum to the checksum list
    #   does checksum match any other checksum in list? (count > 2)
    #
    #   identify the biggest bank
    #   remove its contents, this is how many to distribute
    #   while distribution pile > 0:
    #       advance to the next higher bank (loop around to 0 when passing the end)
    #       increment current bank by 1 and decrement the distribution pile by 1
    #
    #   - done distributing
    #

    for row in inputlist:
        print(row)

        rowchecksum = checksum_row(row)
        print('rowchecksum = ', rowchecksum)
        print()

    return final


def checksum_row(rowdata):
    rowcx = 0
    seed = 113
    limit = 10000007

    for item in rowdata:
        rowcx += int(item)
        rowcx *= seed
        rowcx %= limit
        print(item, rowcx)

    return rowcx


def generate_md5_hash(word):
    md5 = hashlib.md5(word.encode())
    return md5.hexdigest()


def show_puzzle(output):
    print('')
    print('solution: ', output)


def main():
    print('(puzzle00a) main:')
    print('')

    mydata = load_puzzle()
    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle00a) end::')
    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
