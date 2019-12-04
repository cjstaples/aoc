# test
import unittest

from puzzle_2019_02a import load_puzzle, solve_puzzle


class TestPuzzle2019(unittest.TestCase):

    def test_sample_00(self):
        mydata = load_puzzle('../data/puzzle-02/', 'aoc-2019_puzzle-02_input_test-0.txt')  #
        t = solve_puzzle(mydata)
        assert t == [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]

    def test_sample_01(self):
        mydata = load_puzzle('../data/puzzle-02/', 'aoc-2019_puzzle-02_input_test-1.txt')  # [1, 0, 0, 0, 99]
        t = solve_puzzle(mydata)
        assert t == [2, 0, 0, 0, 99]

    def test_sample_02(self):
        mydata = load_puzzle('../data/puzzle-02/', 'aoc-2019_puzzle-02_input_test-2.txt')  # [2, 3, 0, 3, 99]
        t = solve_puzzle(mydata)
        assert t == [2, 3, 0, 6, 99]

    def test_sample_03(self):
        mydata = load_puzzle('../data/puzzle-02/', 'aoc-2019_puzzle-02_input_test-3.txt')  # [2, 4, 4, 5, 99, 0]
        t = solve_puzzle(mydata)
        assert t == [2, 4, 4, 5, 99, 9801]

    def test_sample_04(self):
        mydata = load_puzzle('../data/puzzle-02/', 'aoc-2019_puzzle-02_input_test-4.txt')  # [1, 1, 1, 4, 99, 5, 6, 0, 99]
        t = solve_puzzle(mydata)
        assert t == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    def test_sample_final_part_1(self):
        mydata = load_puzzle('../data/puzzle-02/', 'aoc-2019_puzzle-02_input.txt')  # puzzle input
        t = solve_puzzle(mydata)
        assert t == [0]


if __name__ == '__main__':
    unittest.main()
