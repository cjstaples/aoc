import sys


def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        # tmp = ins.read().split("\n")
        tmp = ins.read().splitlines()
        # input_set = [int(i) for i in tmp]

        # using list comprehension + zip() + slicing + enumerate()
        # split list into lists by arbitrary value
        # based on
        # https://www.geeksforgeeks.org/python-split-list-into-lists-by-particular-value/
        size = len(tmp)
        idx_list = [idx + 1 for idx, val in
                    enumerate(tmp) if val == '']
        # could reduce j index by one to drop the identified val '' from result lists
        # but then need to work around the list end better

        res = [tmp[i: j] for i, j in
               zip([0] + idx_list, idx_list +
                   ([size] if idx_list[-1] != size else []))]

        new_data = []
        for test_list in res:
            test_list = [i for i in test_list if i]
            new_data.append(test_list)

    return new_data


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))

    elf_calories = []
    for data in indata:
        # incoming data is a list of lists
        # each list contains 1+ integers
        # sum each list
        # add sum to list of total calories
        print('do something with : ' + str(data) + ' ')

        item_sum = 0
        for item in data:
            item_sum = item_sum + int(item)
        print(f'item_sum:  {item_sum}')
        elf_calories.append(item_sum)
        elf_calories_sorted = sorted(elf_calories)
        top_three_list = elf_calories_sorted[-3::]

        top_three_sum = 0
        for item in top_three_list:
            top_three_sum = top_three_sum + int(item)

    print(f'elf_calories           :  {elf_calories}')
    print(f'elf_calories_sorted    :  {elf_calories_sorted}')
    print(f'elf_calories (smallest):  {min(elf_calories)}')
    print(f'elf_calories  (largest):  {max(elf_calories)}')
    print(f'elf_calories top three :  {top_three_list}')
    print(f'elf_calories top 3 sum :  {top_three_sum}')

    return False


def show_puzzle(output):
    print('----')
    print(output)
    print('----')


def main():
    print('(puzzle01a) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc_2022_puzzle_01_input.txt'
    print(f'PARAM: [ {param} ]')
    path = 'data/puzzle_01/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle01a) end::')
    return mysolution


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
