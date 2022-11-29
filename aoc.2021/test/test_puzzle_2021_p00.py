# test
import unittest

from puzzle.puzzle_00.puzzle_2020_00 import load_puzzle, solve_puzzle


class TestPuzzle2021(unittest.TestCase):

    def test_sample_00(self):
        mydata = load_puzzle('../data/puzzle_00/', 'aoc_2021_puzzle_00_input.txt')  # 12
        t = solve_puzzle(mydata)
        assert t == False


if __name__ == '__main__':
    unittest.main()
