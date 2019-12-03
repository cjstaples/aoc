# test

from puzzle01a import load_puzzle, solve_puzzle

def test_sample_00():
    mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input_test-0.txt')
    t = solve_puzzle(mydata)
    assert t == 3

def test_sample_01():
    mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input_test-1.txt')
    t = solve_puzzle(mydata)
    assert t == 3

def test_sample_02():
    mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input_test-2.txt')
    t = solve_puzzle(mydata)
    assert t == 0

def test_sample_03():
    mydata = load_puzzle('../data/puzzle-01/','aoc-2018_puzzle-01_input_test-3.txt')
    t = solve_puzzle(mydata)
    assert t == -6

def test_sample_final_part_1():
    mydata = load_puzzle('../data/puzzle-01/','aoc-2019_puzzle-01_input.txt')
    t = solve_puzzle(mydata)
    assert t == 477
