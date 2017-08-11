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


# Iterate through each square. Find missing nums. Set-Intersect with each elem
def solve_squares(puzzle):
    for sq in puzzle:

        # Set all numbers that are missing in the 3x3 square to all_nums[1-9]
        missing_nums = all_nums[:]

        # Elements that are yet to be solved
        unsolved_elems = []

        for row_id, sq_row in enumerate(sq):
            for elem_id, elem in enumerate(sq_row):

                # If empty elem, add all possible nums as list
                if not elem:
                    sq[row_id][elem_id] = all_nums[:]
                    unsolved_elems.append((row_id, elem_id))

                # Add unsolved elem to list
                elif len(elem) != 1:
                    unsolved_elems.append((row_id, elem_id))

                # Use solved elem to calculate missing_nums
                else:
                    missing_nums.remove(elem[0])

        # Set intersection of missing nums and unsolved element's list
        for (row_id, elem_id) in unsolved_elems:
            sq[row_id][elem_id] = [x for x in missing_nums
                                   if x in sq[row_id][elem_id]]


# Iterate through each row. Find missing nums. Set-Intersect with each elem
def solve_rows(puzzle):
    pass

# Iterate through each col. Find missing nums. Set-Intersect with each elem

if __name__ == '__main__':
    problem = puzzle1
    solve_squares(problem)
    pprint(problem)
