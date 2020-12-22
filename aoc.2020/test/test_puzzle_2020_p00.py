# test
import unittest

from puzzle.puzzle_01.puzzle_2020_01a import load_puzzle, solve_puzzle

class TestPuzzle2020(unittest.TestCase):

    def test_sample_00(self):
        mydata = load_puzzle('../data/puzzle_00/', 'aoc_2020_puzzle_00_input.txt')   # 12
        t = solve_puzzle(mydata)
        assert t == False



if __name__ == '__main__':
    unittest.main()
