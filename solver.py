def validate_puzzle(puzzle):
    if len(puzzle) != 9:
        return False
    for row in puzzle:
        if len(row) != 9:
            return False
        for num in row:
            if type(num) != int:
                return False
            elif not 0 <= num <= 9:
                return False
    return True


def count_nums(puzzle):
    counts = dict.fromkeys(range(10),0)
    for row in puzzle:
        for num in row:
            counts[num] += 1
    return counts

def get_col(puzzle, col):
    return [puzzle[i][col] for i in range(9)]

def get_block(puzzle, block):
    start_col = block%3 * 3
    start_row = block//3 * 3 #0:0, 1:0, 2:0, 3:3, 4:3, 5:3, 6:6, 7:6, 8:6
    block = []
    for row in range(start_row, start_row+3):
        for col in range(start_col, start_col+3):
            block.append(puzzle[row][col])
    return block

def missing_row(puzzle, row):
    row = puzzle[row]
    missing = [num for num in range(1,10) if num not in row]
    return missing

def missing_col(puzzle, col):
    col = get_col(puzzle, col)
    missing = [num for num in range(1,10) if num not in col]
    return missing

def missing_block(puzzle, block):
    block = get_block(puzzle, block)
    missing = [num for num in range(1,10) if num not in block]
    return missing

def generate_possibles(puzzle):
    possibles = [[],[],[],[],[],[],[],[],[]]
    for row in range(9):
        for col in range(9):
            block = row//3*3 + col//3%3 # figure out formula to calculate block based on row and col block 0-8 col determine remainder row determine main row//3 + col%3
            possibles[row].append([])
            if puzzle[row][col] == 0:
                for i in range(1,10):
                    if i not in puzzle[row] and i not in get_col(puzzle, col) and i not in get_block(puzzle, block):
                        possibles[row][col].append(i)
            print(row, col, block, possibles[row][col])
    return possibles

def solve_singles(puzzle):
    possibles = generate_possibles(puzzle)
    for row in range(9):
        for col in range(9):
            if len(possibles[row][col]) == 1:
                puzzle[row][col] = possibles[row][col][0]

if __name__ == '__main__':

    # Zeros are empty spaces
    puzzle = [[5,0,0,6,9,4,0,3,2],
            [9,3,6,0,1,2,0,4,0],
            [0,0,0,3,0,7,0,0,0],
            [0,0,5,2,0,0,0,7,0],
            [0,0,0,0,0,1,0,0,9],
            [2,0,8,0,0,3,5,0,0],
            [0,6,2,0,3,0,0,0,4],
            [3,8,1,0,4,6,0,5,0],
            [4,0,0,7,0,8,6,1,0]
            ]

    print(validate_puzzle(puzzle))
    print(count_nums(puzzle))

    # find missing in row
    # find missing in col
    # find missing in cell
    print(missing_row(puzzle, 1))
    print(missing_col(puzzle, 1))
    print(missing_block(puzzle, 1))


    # 3d list where each innermost list is the potential values
    for row in generate_possibles(puzzle):
        print(row)
    
    solve_singles(puzzle)
    for row in puzzle:
        print(row)
