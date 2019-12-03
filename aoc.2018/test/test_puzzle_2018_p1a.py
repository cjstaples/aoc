# test
import unittest

from puzzle_2018_01a import load_puzzle, solve_puzzle


class TestPuzzle2018(unittest.TestCase):

    def test_sample_00(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2018_puzzle-01_input_test-0.txt')
        t = solve_puzzle(mydata)
        assert t == 3

    def test_sample_01(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2018_puzzle-01_input_test-1.txt')
        t = solve_puzzle(mydata)
        assert t == 3

    def test_sample_02(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2018_puzzle-01_input_test-2.txt')
        t = solve_puzzle(mydata)
        assert t == 0

    def test_sample_03(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2018_puzzle-01_input_test-3.txt')
        t = solve_puzzle(mydata)
        assert t == -6

    def test_sample_final_part_1(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2018_puzzle-01_input.txt')
        t = solve_puzzle(mydata)
        assert t == 477


if __name__ == '__main__':
    unittest.main()
