from pprint import pprint

all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example of a sudo puzzle to be solved
puzzle1_row1 = [[[7], [2], [3]],
                [[6], [], []],
                [[8], [], []]]

puzzle1_row2 = [[[], [], []],
                [[3], [], [2]],
                [[], [1], []]]

puzzle1_row3 = [[[1], [5], [9]],
                [[], [], [8]],
                [[], [], [2]]]

puzzle1_row4 = [[[], [7], []],
                [[], [], [4]],
                [[], [5], []]]

puzzle1_row5 = [[[6], [5], [4]],
                [[2], [], [7]],
                [[9], [3], [1]]]

puzzle1_row6 = [[[], [2], []],
                [[3], [], []],
                [[], [4], []]]

puzzle1_row7 = [[[5], [], []],
                [[4], [], []],
                [[9], [3], [2]]]

puzzle1_row8 = [[[], [7], []],
                [[1], [], [3]],
                [[], [], []]]

puzzle1_row9 = [[[], [], [3]],
                [[], [], [6]],
                [[7], [1], [4]]]

puzzle1 = [puzzle1_row1, puzzle1_row2, puzzle1_row3,
           puzzle1_row4, puzzle1_row5, puzzle1_row6,
           puzzle1_row7, puzzle1_row8, puzzle1_row9]

# Initial code for traversing
# for sq in puzzle1:
#     for sq_row in sq:
#         for elem in sq_row:
#
#             # If it needs to be solved, add all possible numbers
#             if not elem:
#                 elem = all_nums

# TODO:
# Set all empty squares as all_nums
# Iterate through each square. Find missing nums. Set-Intersect with each elem
for sq in puzzle1:

    # Numbers that are missing in the 3x3 square
    missing_nums = all_nums

    # Elements that are yet to be solved
    unsolved_elems = []

    for sq_row in sq:
        for elem in sq_row:

            # If empty elem, add all possible nums as list
            if not elem:
                elem = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                unsolved_elems.append(elem)

            # Add unsolved elem to list
            elif len(elem) != 1:
                unsolved_elems.append(elem)

            # Use solved elem to calculate missing_nums
            else:
                missing_nums.remove(elem[0])


    # Set intersection of missing nums and unsolved element's list
    for elem in unsolved_elems:
        elem = [x for x in elem if x in missing_nums]



# Iterate through each row. Find missing nums. Set-Intersect with each elem

# Iterate through each col. Find missing nums. Set-Intersect with each elem

pprint(puzzle1)
