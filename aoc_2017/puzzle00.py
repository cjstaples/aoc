import sys
import hashlib


#   PUZZLE BLANK FRAMEWORK


def load_puzzle():
    #   with open("data/aoc-2017_puzzle-x_test.txt", "r") as ins:
    #   with open("data/aoc-2017_puzzle-x_input.txt", "r") as ins:
    #     tmp = ins.read().split("\n")
    #     inputlist = [i.split(" ") for i in tmp]

    inputlist = ['a', 'b', 'c']
    return inputlist


def solve_puzzle(inputlist):
    #
    final = 0

    # do stuff
    return final


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
