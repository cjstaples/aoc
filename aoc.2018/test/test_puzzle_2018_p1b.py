# test
import unittest

from puzzle_2018_01b import load_puzzle, solve_puzzle


class TestPuzzle2018(unittest.TestCase):

    def test_sample_10(self):
        mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input_test-10.txt')
        t = solve_puzzle(mydata)
        assert t == 2

    def test_sample_11(self):
        mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input_test-11.txt')
        t = solve_puzzle(mydata)
        assert t == 0

    def test_sample_12(self):
        mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input_test-12.txt')
        t = solve_puzzle(mydata)
        assert t == 10

    def test_sample_13(self):
        mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input_test-13.txt')
        t = solve_puzzle(mydata)
        assert t == 5

    def test_sample_14(self):
        mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input_test-14.txt')
        t = solve_puzzle(mydata)
        assert t == 14

    def test_sample_final_part_2(self):
        mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input.txt')
        t = solve_puzzle(mydata)
        assert t == 0

if __name__ == '__main__':
    unittest.main()
