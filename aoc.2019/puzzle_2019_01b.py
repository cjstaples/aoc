import sys


def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        tmp = ins.read().split("\n")
        input_set = [int(i) for i in tmp]
    arraydata = input_set
    return arraydata


def compute_fuel(mass):
    fuel = int(mass / 3) - 2
    print('mass: ' + str(mass) + ' / fuel: ' + str(fuel))
    if fuel < 0:
        fuel = 0
    return fuel


def compute_fuel_recursive(mass):

    fuel = compute_fuel(mass)
    if fuel <= 0:
        return 0
    else:
        print('fuel: '+str(fuel))
        return fuel + compute_fuel_recursive(fuel)


def solve_puzzle(indata):
    total_fuel = 0
    mass = indata[0]
    print('-- solving for ' + str(mass))

    for data in indata:
        total_fuel += compute_fuel_recursive(data)
        print('total fuel: '+str(total_fuel))
        print('----')

    return total_fuel


def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle01b) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc-2019_puzzle-01_input.txt'
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
