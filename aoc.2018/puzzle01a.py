import sys

def load_puzzle():
    # chars = '12131415'
    chars = '123'
    return chars

def solve_puzzle(indata):
    print('-- solving for ' + str(indata))
    final = 0

    return final

def show_puzzle(output):
    print(output)

def main():
    print('(puzzle01a) main:')
    print('')

    mydata = load_puzzle()

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle01a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
