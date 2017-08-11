all_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Example of a sudo puzzle to be solved
puzzle1_row1 = [[[7], [2], [3]],
                [[6], [],  []],
                [[8], [],  []]]

puzzle1_row2 = [[[],  [],  []],
                [[3], [],  [2]],
                [[],  [1], []]]

puzzle1_row3 = [[[1], [5], [9]],
                [[],  [],  [8]],
                [[],  [],  [2]]]

puzzle1_row4 = [[[], [7], []],
                [[], [],  [4]],
                [[], [5], []]]

puzzle1_row5 = [[[6], [5], [4]],
                [[2], [],  [7]],
                [[9], [3], [1]]]

puzzle1_row6 = [[[],  [2], []],
                [[3], [],  []],
                [[],  [4], []]]

puzzle1_row7 = [[[5], [], []],
                [[4], [],  []],
                [[9], [3],  [2]]]

puzzle1_row8 = [[[], [7], []],
                [[1], [], [3]],
                [[], [],  []]]

puzzle1_row9 = [[[], [], [3]],
                [[], [],  [6]],
                [[7], [1], [4]]]

puzzle1 = [puzzle1_row1, puzzle1_row2, puzzle1_row3,
           puzzle1_row4, puzzle1_row5, puzzle1_row6,
           puzzle1_row7, puzzle1_row8, puzzle1_row9]


# Initial code for traversing
for sq in puzzle1:
    for sq_row in sq:
        for elem in sq_row:

            # If it needs to be solved, add all possible numbers
            if not elem:
                elem = all_nums
