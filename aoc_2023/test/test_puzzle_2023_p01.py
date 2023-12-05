# test
import unittest

from aoc_2023.puzzle.puzzle_01.puzzle_2023_01 import load_puzzle, solve_puzzle


class TestPuzzle2023(unittest.TestCase):

    # @unittest.skip  # disable until logic built
    def test_sample_01(self):
        mydata = load_puzzle('../data/puzzle_01/', 'aoc_2023_puzzle_01_input.txt')
        t = solve_puzzle(mydata)
        assert t == 53921

    def test_sample_01_test(self):
        mydata = load_puzzle('../data/puzzle_01/', 'aoc_2023_puzzle_01_input_sample.txt')
        t = solve_puzzle(mydata)
        assert t == 142

    def test_sample_01_test_a(self):
        mydata = load_puzzle('../data/puzzle_01/', 'aoc_2023_puzzle_01_input_sample_a.txt')
        t = solve_puzzle(mydata)
        assert t == 157


if __name__ == '__main__':
    unittest.main()
