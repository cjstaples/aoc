# test
import unittest

from puzzle_2019_01a import load_puzzle, solve_puzzle


class TestPuzzle2019(unittest.TestCase):

    def test_sample_00(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2019_puzzle-04_input_test-0.txt')   #
        t = solve_puzzle(mydata)
        assert t == 0

    def test_sample_final_part_1(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2019_puzzle-04_input.txt')          # puzzle input
        t = solve_puzzle(mydata)
        assert t == 0


if __name__ == '__main__':
    unittest.main()
