# test
import unittest

from aoc_2022.puzzle.puzzle_00.puzzle_2022_00 import load_puzzle, solve_puzzle


class TestPuzzle2022(unittest.TestCase):

    def test_sample_00(self):
        mydata = load_puzzle('../data/puzzle_00/', 'aoc_2022_puzzle_00_input.txt')
        t = solve_puzzle(mydata)
        assert t == 55

    def test_sample_00_test(self):
        mydata = load_puzzle('../data/puzzle_00/', 'aoc_2022_puzzle_00_input_sample.txt')
        t = solve_puzzle(mydata)
        assert t == 15


if __name__ == '__main__':
    unittest.main()
