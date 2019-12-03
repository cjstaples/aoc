import sys


def load_puzzle(path, input):
    filename = input
    pathname = path + filename
    with open(pathname, "r") as ins:
        tmp = ins.read().split("\n")
        inputlist = [int(i) for i in tmp]
    arraydata = inputlist
    return arraydata


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))
    value = 0
    final = 0
    frequency = 0
    freqlist = [0]

    while value == 0:
        for data in indata:
            print('new data: ',data)
            frequency += data
            print('new frequency: ',frequency)
        # check frequency list to see if it contains the data value
            if frequency in freqlist:
                # when duplicate found, set value to 1
                final = frequency
                value = 1
            else:
                # else add the new value to frequency list
                freqlist.append(frequency)
                print('new freqlist: ',sorted(freqlist))
                # print('len freqlist: ',len(freqlist))
                # print('min freqlist: ',min(freqlist))
                # print('max freqlist: ',max(freqlist))
                print('MIN:',min(freqlist),' :: LEN:',len(freqlist),' :: MAX:',max(freqlist))
                print('-------------')
            if value == 1:
                break
    # return the first value reached twice
    return final


def show_puzzle(output):
    print(output)


def main():
    print('(puzzle01b) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc-2018_puzzle-01_input_test.txt'
    print('PARAM: [ ' + param + ' ]')
    path = 'data/puzzle-01/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle01b) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
