import sys
import hashlib


#   AOC 2017
#   Day 5: A Maze of Twisty Trampolines, All Alike


def load_puzzle():
    #   with open("data/aoc-2017_puzzle-5_test.txt", "r") as ins:
    with open("data/aoc-2017_puzzle-5_input.txt", "r") as ins:
        tmp = ins.read().split("\n")
        # inputlist = [i.split(" ") for i in tmp]
        inputlist = [int(i) for i in tmp]
    # inputlist = [0,3,0,1,-3]
    return inputlist


def solve_puzzle(inputlist):
    #
    final = 0
    currentpos = 0
    lastpos = 0
    steps = 0

    print('start:::\n',inputlist,'\n')
    listlength = len(inputlist)

    #    while ((currentpos < listlength) & (z<10)) :
    while (currentpos < listlength):
        # print('currentpos: ',currentpos)
        # print('currentval: ',inputlist[currentpos])
        # print('   lastpos: ',lastpos)
        # print()
        #
        #   move position by current value
        #   increment value where we were   -   lastpos
        #
        #


        currentpos+=inputlist[currentpos]
        inputlist[lastpos]+=1
        #   print('lastpos newval: ',inputlist[lastpos])
        lastpos = currentpos
        #   print('current pos newval: ',currentpos)

        print(inputlist)

        steps+=1
        # print()

    # for r in range(0,listlength):
    #     print(r)
    #     print(inputlist[r])
    #
    # for idx, val in enumerate(inputlist):
    #     print('index: ', idx, 'value: ', val)
    #     final+=val

    final = steps
    return final


def show_puzzle(output):
    print('')
    print('solution: ', output)


def main():
    print('(puzzle05a) main:')
    print('')

    mydata = load_puzzle()
    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle05a) end::')
    return 0


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
