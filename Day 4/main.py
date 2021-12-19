import sys

input_file = open('input.txt', 'r')
input_lines = input_file.readlines()
for index in range(0, len(input_lines)):
    input_lines[index] = input_lines[index].strip()

#make number sequence usable
numseq = input_lines[0].split(',')
#create a list of each board
boards = []
for i in range(2, len(input_lines), 6):
    boards.append(input_lines[i:i+5])

#split each board's row into individual numbers
for board in boards:
    for i in range(len(board)):
        board[i] = board[i].split()

#convert strings into ints
for i in range(len(numseq)):
    numseq[i] = int(numseq[i])
for board in boards:
    for y in range(len(board)):
        for x in range(len(board[y])):
            board[y][x] = int(board[y][x])
#board[y][x]

def checkWin(inputBoard) -> bool:
    #check if a row wins
    for row in inputBoard:
        if sum(row) == -5: return True
    #check if column wins
    for i in range(len(inputBoard[0])):
        colSum = 0
        for row in inputBoard:
            colSum += row[i]
        if colSum == -5: return True
    return False

#replaces input number in every board with -1
def boardRepl(inputNum):
    for board in boards:
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == inputNum:
                    board[y][x] = -1

def findWinningBoard():
    for board in boards:
        if checkWin(board) == True:
            return board
    return 0

def findWinningBoardIndex() -> int:
    for i in range(len(boards)):
        if checkWin(boards[i]) == True:
            return i
    return -1

def findUnmarkedNumSum(inputBoard) -> int:
    output = 0
    for row in inputBoard:
        for val in row:
            if val != -1:
                output += val
    return output

def part1():
    for num in numseq:
        boardRepl(num)
        if findWinningBoard() != 0:
            break
    winBoard = findWinningBoard()
    print(findUnmarkedNumSum(winBoard)*num)

def part2():
    for i in range(len(numseq)):
        boardRepl(numseq[i])
        if len(boards) == 1:
            break
        while findWinningBoardIndex() != -1:
            del boards[findWinningBoardIndex()]
    for j in range(i, len(numseq)):
        boardRepl(numseq[j])
        if checkWin(boards[0]) == True:
            break
    print(findUnmarkedNumSum(boards[0])*numseq[j])
    
if len(sys.argv) == 1:
    print("Please enter \'1\' for part one or \'2\' for part two")
elif len(sys.argv) == 2:
    if int(sys.argv[1]) == 1:
        part1()
    elif int(sys.argv[1]) == 2:
        part2()
    else:
        print("Invalid input, please enter \'1\' for part one or \'2\' for part two")
else:
    print("Too many arguments passed, please enter \'1\' for part one or \'2\' for part two")