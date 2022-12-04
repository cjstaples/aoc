import sys


def load_puzzle(path, puzzle_input):
    filename = puzzle_input
    pathname = path + filename
    with open(pathname, "r") as ins:
        # tmp = ins.read().split("\n")
        tmp = ins.read().splitlines()

    return tmp


def get_play_values(data):
    opp_play = data[:1]
    my_play = data[-1:]
    return opp_play, my_play


def get_play_score(play):
    if play == "X":
        return 1
    elif play == "Y":
        return 2
    elif play == "Z":
        return 3


def get_round_result(entry):
    if entry in ["A Z", "B X", "C Y"]:
        return 0
    elif entry in ["A X", "B Y", "C Z"]:
        return 3
    elif entry in ["A Y", "B Z", "C X"]:
        return 6
    else:
        return -1


def solve_puzzle(indata):
    print('-- solving for ' + str(indata))

    score_sum = 0
    for data in indata:
        # incoming data each like 'A Y' or 'B X' or 'C Z'
        # where first value ABC is opponent play
        #   A = Rock, B = Paper, C = Scissors
        # where second value XYZ is your play
        #   X = Rock (1), Y = Paper (2), Z = Scissors (3)

        # get play values from data line
        opponent_play, your_play = get_play_values(data)
        print(f'gpv: {opponent_play} and {your_play}')

        # get score for your play_value
        #   X = Rock (1), Y = Paper (2), Z = Scissors (3)
        play_score = get_play_score(your_play)
        print(f'play score: {play_score}')

        # get score for rps_round_result
        #   (0 for loss, 3 for draw, 6 for win)
        #   brute forcing values here for now
        #   (AZ, BX, CY) = 0
        #   (AX, BY, CZ) = 3
        #   (AY, BZ, CX) = 6
        rps_round_result = get_round_result(data)
        print(f'round result: {rps_round_result}')

        score_sum = score_sum + rps_round_result + play_score

    # sum of all data-lines scores
    # e.g. for sample A Y (6+2=8), B X (0+1=1), C Z (3+3=6) total = (15)

    return score_sum


def show_puzzle(output):
    print('----')
    print(f'total: {output}')
    print('----')


def main():
    print('(puzzle02a) main:')
    print('')

    try:
        param = sys.argv[1]
    except IndexError:
        print('** PARAM not found on command line, substitute default test file name**')
        param = 'aoc_2022_puzzle_02_input.txt'
    print(f'PARAM: [ {param} ]')
    path = 'data/puzzle_02/'
    mydata = load_puzzle(path, param)

    mysolution = solve_puzzle(mydata)
    show_puzzle(mysolution)
    print('')

    print('')
    print('(puzzle02a) end::')
    return mysolution


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
