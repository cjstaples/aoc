import sys
import hashlib


#   AOC
#   --- Day 6: Memory Reallocation ---


def load_puzzle():
    with open("data/aoc-2017_puzzle-6_tast.txt", "r") as ins:
        #   with open("data/aoc-2017_puzzle-6_input.txt", "r") as ins:
        tmp = ins.read().split("\n")
        #   inputlist = [i.split("\t") for i in tmp]
        inputlist = [int(n) for n in tmp.split('\t')]
    #    inputlist = ['a', 'b', 'c']
    return inputlist


def solve_puzzle(inputlist):
    #
    #   talk it through...
    #   done - get set of banks from input
    #   until checksum_match:
    #       done - get checksum for the current set of banks
    #       done - add checksum to the checksum list
    #       does checksum match any other checksum in list? (count > 2)
    #       if not:
    #           identify the biggest bank
    #           remove its contents, this is how many to distribute
    #           while distribution pile > 0:
    #               advance to the next higher bank (loop around to 0 when passing the end)
    #               increment current bank by 1 and decrement the distribution pile by 1
    #           - done distributing
    #           count++
    #
    final = 0
    is_found = False
    checksum_list = []

    for row in inputlist:
        print(row)

    while ((is_found == False) & (final < 10)):
        rowchecksum = checksum_row(row)
        print('rowchecksum = ', rowchecksum)
        print()
        checksum_list.append(rowchecksum)
        final += 1
        is_found = cx_find(checksum_list, rowchecksum)
        highest_bank = get_highest_bank(row)


    return final


def cx_find(cxlist, cx):
    is_found = False
    print('count: ', cxlist.count(cx))

    return is_found


def checksum_row(rowdata):
    rowcx = 0
    seed = 113
    limit = 10000007

    for item in rowdata:
        rowcx += int(item)
        rowcx *= seed
        rowcx %= limit
    #   print(item, rowcx)

    return rowcx


def get_highest_bank(row):
    print(row)
    bank = row.index(max(row))
    value = row[bank]
    print('hi bank :: ', bank)
    print('value   :: ', value)
    print('counts  :: ', row.count(value))
    return bank


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
