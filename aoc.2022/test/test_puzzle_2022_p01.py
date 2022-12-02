# test
import unittest

from puzzle.puzzle_01.puzzle_2020_01a import load_puzzle, solve_puzzle


class TestPuzzle2022(unittest.TestCase):

    def test_sample_00(self):
        mydata = load_puzzle('../data/puzzle_01/', 'aoc_2022_puzzle_01_input.txt')
        t = solve_puzzle(mydata)
        assert t is False

    def test_sample_00_test(self):
        mydata = load_puzzle('../data/puzzle_01/', 'aoc_2022_puzzle_01_input_sample.txt')
        t = solve_puzzle(mydata)
        assert t is False


if __name__ == '__main__':
    unittest.main()
