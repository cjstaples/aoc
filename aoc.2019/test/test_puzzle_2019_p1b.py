# test
import unittest

from puzzle_2019_01b import load_puzzle, solve_puzzle


class TestPuzzle2019(unittest.TestCase):

    def test_sample_00(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2019_puzzle-01_input_test-0.txt')   # 12
        t = solve_puzzle(mydata)
        assert t == 2

    def test_sample_01(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2019_puzzle-01_input_test-1.txt')   # 14
        t = solve_puzzle(mydata)
        assert t == 2

    def test_sample_02(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2019_puzzle-01_input_test-2.txt')   # 1969
        t = solve_puzzle(mydata)
        assert t == 654

    def test_sample_03(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2019_puzzle-01_input_test-3.txt')   # 100756
        t = solve_puzzle(mydata)
        assert t == 33583

    def test_sample_final_part_1(self):
        mydata = load_puzzle('../data/puzzle-01/', 'aoc-2019_puzzle-01_input.txt')          # puzzle input
        t = solve_puzzle(mydata)
        assert t == 3406432


if __name__ == '__main__':
    unittest.main()
