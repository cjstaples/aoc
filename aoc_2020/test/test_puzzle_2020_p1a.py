# test
import unittest

from puzzle.puzzle_01.puzzle_2020_01a import load_puzzle, solve_puzzle

class TestPuzzle2020(unittest.TestCase):

    def test_sample_00(self):
        mydata = load_puzzle('../data/puzzle_01/', 'aoc_2020_puzzle_01_input_test_0.txt')   # 12
        t = solve_puzzle(mydata)
        assert int(t) == 514579

    def test_sample_final_part_1(self):
        mydata = load_puzzle('../data/puzzle_01/', 'aoc_2020_puzzle_01_input.txt')          # puzzle input
        t = solve_puzzle(mydata)
        assert int(t) == 646779


if __name__ == '__main__':
    unittest.main()
