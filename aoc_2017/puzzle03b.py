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
    #   puzzleinput = [361527]
    return puzzleinput


def solve_puzzle(square):
    print('-- solving for ' + str(square))
    final = 0
    neighbor_spaces = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    neighbor_values = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    all_values = [[]]

    ring = get_ring(square)
    position = get_ring_position(square, ring)
    # position will be used in the list storing square values for each ring

    all_values = build_value_lists(ring)
    print(all_values)

    neighbor_spaces = get_neighbor_spaces(square)
    neighbor_values = get_neighbor_values(square)

    print('ring: ', ring, 'position: ', position)

    # once we know all the neighbor values, add them up and return
    print('neighbor_spaces: ', neighbor_spaces)
    print('neighbor_values: ', neighbor_values)
    for value in neighbor_values:
        final += value
    return final


def build_value_lists(ring):
    values = []
    ringval = []
    ring = 1

    ringval.append([1])
    ringval.append([1, 2, 4, 5, 10, 11, 23, 25])

    for x in range(0, ring+1):
        print('loop: ',x)
        values.append(ringval[x])

    return values


def get_neighbor_spaces(square):
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    return values


def get_neighbor_values(square):
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    return values


def get_square_value(square):
    ring = ring = get_ring(square)
    index = get_ring_position(square, ring)
    return


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
            #   print('>===> ring bump!  decoder:', decoder)
            current_ring += 1
        decoder += 1

    ring = current_ring
    return ring


def get_ring_max_square(ring):
    return (ring * 2 + 1) ** 2


def get_ring_min_value(ring):
    # virtual value for the LR corner in each ring
    rms = get_ring_max_square(ring)
    rs = ring * 2
    return rms - 4 * rs


def get_ring_position(square, ring):
    # returns +n position along ring from the 0 (LR) corner value
    # e.g. for ring 1 -> square 2 = 1, square 4 = 3
    # e.g. for ring 2 -> square 11 = 2, square 15 = 6
    # find the lowest value in the ring, subtract it from square
    position = square - get_ring_min_value(ring)

    return position


def get_ring_offset(square, ring):
    offset = 0
    print('getting offset for square: ', square, 'ring: ', ring)

    ring_centers = get_ring_centers(ring)
    # returns square location numbers for centers as list of 4 ints
    print('::centers:: ', ring_centers)

    # offset is the distance to the closest center
    center_offset = int(sys.maxsize)
    print('got centers for ring: ', ring)

    for center in ring_centers:
        difference = abs(square - center)
        print('---  center ', center, ' is off by ', difference)
        if center_offset > difference:
            center_offset = difference

    print('center_offset: ', center_offset)
    return center_offset


def get_ring_corners(ring):
    # in each ring, assuming ringside (rs) = ring * 2,
    # the corners are ring_max_square (rms), rms-rs, rms-2rs, rms-3rs, and rms-4rs
    rms = get_ring_max_square(ring)
    rs = ring * 2
    corner_list = [(rms - rs * 3), (rms - rs * 2), (rms - rs), rms, (rms - 4 * rs)]
    return corner_list


def get_ring_centers(ring):
    # in each ring,
    # the centers are ring_max_square (rms) - ring, rms - 3 * ring, rms - 5 * ring, rms - 7 * ring
    rms = get_ring_max_square(ring)
    center_list = [(rms - ring * 7), (rms - ring * 5), (rms - ring * 3), (rms - ring)]
    return center_list


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
