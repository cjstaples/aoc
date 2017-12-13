import sys
import math


#   puzzle inputs
#   square    1:        ring 0, offset 0, final 0  (per solution)
#   square   12:        ring 2, offset 1, final 3  (per solution)
#   square   23:        ring 2, offset 0, final 2  (per solution)
#   square 1024:        ring x, offset x, final 31 (per solution)
def load_puzzle():
    #   puzzleinput = [1, 2, 9, 10, 25, 26]
    puzzleinput = [1, 12, 23, 1024]
    #    puzzleinput = [361527]
    return puzzleinput


def solve_puzzle(square):
    print('-- solving for ' + str(square))
    final = 0

    ring = get_ring(square)
    offset = get_ring_offset(square, ring)
    final = ring + offset

    print('ring: ', ring, 'offset: ', offset, 'final: ', final)
    return final


def get_ring(square):
    # talk it through...
    # ring number #0 for squares #1 thru 1     ( 1 ^2 !)
    # ring number #1 for squares #2 thru 9     ( 3 ^2 !) aka (2r+1)^2
    # ring number #2 for squares #10 thru 25   ( 5 ^2 !)
    # ring number #3 for squares #26 thru 49   ( 7 ^2 !)
    # --
    # ring is base distance
    # offset is additional distance along ring toward a corner

    ring = 0
    decoder = 1
    current_ring = 0
    ring_max_square = 1

    print('square: ', square)
    while decoder < square:

        #        print('decoder: ', decoder)
        #        print('current_ring: ', current_ring)
        ring_max_square = get_ring_max_square(current_ring)
        #        print('ring_max_square: ', ring_max_square)

        if decoder >= ring_max_square:
            print('>===> ring bump!  decoder:', decoder)
            current_ring += 1
        decoder += 1

    ring = current_ring
    return ring


def get_ring_max_square(ring):
    return (ring * 2 + 1) ** 2


def get_ring_offset(square, ring):
    offset = 0
    print('getting offset for square: ', square, 'ring: ', ring)

    ring_corners = get_ring_corners(ring)
    # returns square location numbers for corners as list of 4 ints
    print('::corners:: ', ring_corners)

    # offset is the distance to the closest corner
    offset = int(sys.maxsize)
    print('got corners for ring: ', ring)

    for corner in ring_corners:
        difference = abs(square - corner)
        print('---  corner ', corner, ' is off by ', difference)
        if offset > difference:
            offset = difference

    print('offset: ', offset)
    return offset


def get_ring_corners(ring):
    # in each ring, assuming ringside (rs) = ring * 2,
    # the corners are ring_max_square (rms), rms-rs, rms-2rs, rms-3rs, and rms-4rs
    rms = get_ring_max_square(ring)
    rs = ring * 2
    corner_list = [(rms - rs * 3), (rms - rs * 2), (rms - rs), rms, (rms - 4 * rs)]
    return corner_list


def show_puzzle(output):
    print('')
    print('answer: ', output)


def main():
    print('(puzzle03a) main:')
    print('')

    mydata = load_puzzle()
    for data in mydata:
        mysolution = solve_puzzle(data)
        show_puzzle(mysolution)
        print('')

    print('')
    print('(puzzle03a) end::')


# ----------------------------------------
if __name__ == '__main__':
    result = main()
    sys.exit(result)
