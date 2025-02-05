import grid as gd

def is_valid_move(grid, row, col, num):
    # Check row and column
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    # Check 3x3 grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True


def get_input_in_range_with_prompt(min_val, max_val, prompt):
    while True:
        try:
            user_input = int(input(f"{prompt} (between {min_val} and {max_val} inclusive): "))
            if min_val <= user_input <= max_val:
                return user_input
            else:
                print(f"Input must be between {min_val} and {max_val}. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def create_sudoku_grid():
    grid = [[0 for _ in range(9)] for _ in range(9)]

    flag = True
    while flag:
        fill_cell = input(f"Enter a value in a cell (Y/N): ")
        fill_cell = fill_cell.upper()
        if fill_cell in ["Y", "YES"]:
            row = get_input_in_range_with_prompt(1, 9, "Enter the row of filled cell: ")
            col = get_input_in_range_with_prompt(1, 9, "Enter the collumn of filled cell: ")
            value = get_input_in_range_with_prompt(1, 9, "Enter the value in the cell: ")

            if is_valid_move(grid, row-1, col-1, value):
                grid[row-1][col-1] = value
                print(f"grid[{row}][{col}] = {value}\n")
                # print('\nsudoku puzzle till now')
                # gd.print_sudoku(grid)
            else:
                print(f"{value} can't be in grid[{row}][{col}]")
        elif fill_cell in ["N", "NO"]:
            flag = False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    print('\n    Initial Sudoku Puzzle')
    gd.print_sudoku(grid)
    return grid


def main():
    print('''
███████╗██╗   ██╗██████╗  ██████╗ ██╗  ██╗██╗   ██╗
██╔════╝██║   ██║██╔══██╗██╔═══██╗██║ ██╔╝██║   ██║
███████╗██║   ██║██║  ██║██║   ██║█████╔╝ ██║   ██║
╚════██║██║   ██║██║  ██║██║   ██║██╔═██╗ ██║   ██║
███████║╚██████╔╝██████╔╝╚██████╔╝██║  ██╗╚██████╔╝
╚══════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
              Solve a game of SuDoKu
          ------------------------------
''')

    grid = create_sudoku_grid()
    
    if solve_sudoku(grid):
        print("\n    Solved Sudoku")
        gd.print_sudoku(grid)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()