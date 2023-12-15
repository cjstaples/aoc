# test
import unittest

from aoc_2023.puzzle.puzzle_02.puzzle_2023_02 import load_puzzle, solve_puzzle


class TestPuzzle2023(unittest.TestCase):

    def test_sample_02(self):
        mydata = load_puzzle('../data/puzzle_02/', 'aoc_2023_puzzle_02_input.txt')
        t = solve_puzzle(mydata)
        assert t == 55

    def test_sample_02_test(self):
        mydata = load_puzzle('../data/puzzle_02/', 'aoc_2023_puzzle_02_input_sample.txt')
        t = solve_puzzle(mydata)
        assert t == 15


if __name__ == '__main__':
    unittest.main()
