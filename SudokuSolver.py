def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else "." for num in row))

def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(board, num, pos):
    # Check row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True  # Solved
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False

# Example Sudoku puzzle
r1=[]
i=1
while(i<10):
    n1=int(input("enter the element in 1st row : "))
    i=i+1
    r1.append(n1)
r2=[]
i=1
while(i<10):
    n2=int(input("enter the element in 2nd row : "))
    i=i+1
    r2.append(n2)
r3=[]
i=1
while(i<10):
    n3=int(input("enter the element in 3rd row : "))
    i=i+1 
    r3.append(n3)
r4=[]
i=1
while(i<10):
    n4=int(input("enter the element in 4th row : "))
    i=i+1
    r4.append(n4)
r5=[]
i=1
while(i<10):
    n5=int(input("enter the element in 5th row : "))
    i=i+1
    r5.append(n5)
r6=[]
i=1
while(i<10):
    n6=int(input("enter the element in 6th row : "))
    i=i+1
    r6.append(n6)
r7=[]
i=1
while(i<10):
    n7=int(input("enter the element in 7th row : "))
    i=i+1
    r7.append(n7)
r8=[]
i=1
while(i<10):
    n8=int(input("enter the element in 8th row : "))
    i=i+1
    r8.append(n8)
r9=[]
i=1
while(i<10):
    n9=int(input("enter the element in 9th row : "))
    i=i+1
    r9.append(n9)
print(r1)
print(r2)
print(r3)
print(r4)
print(r5)
print(r6)
print(r7)
print(r8)
print(r9)
sudoku_board = [
    r1,
    r2,
    r3,
    r4,
    r5,
    r6,
    r7,
    r8,
    r9
]

print("Original Sudoku Board:")
print_board(sudoku_board)
print("\nSolving Sudoku...\n")

if solve(sudoku_board):
    print("Sudoku Solved:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
