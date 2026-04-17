sudoku = [0 for i in range(9)]
for i in range(9):
    sudoku[i] = list(map(int, input().split()))


zeropos = [(x, y) for x in range(9) for y in range(9) if sudoku[x][y] == 0]



def FindPossibleNumbers(row, col):
    numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    # check the cols and rows to find possible numbers
    for i in range(9):
        numbers.discard(sudoku[row][i])
        numbers.discard(sudoku[i][col])
    

    startrow = (row // 3) * 3
    startcol = (col // 3) * 3
    
    
    for r in range(startrow, startrow + 3):
        for c in range(startcol, startcol + 3):
            numbers.discard(sudoku[r][c])
            
    return numbers

#didnt tried al numbers but tried finding possible numbers
#if no possible numbers means before number was wrong

def sudokusolve(index):
    if index == len(zeropos):
        return True
    
    row, col = zeropos[index]
    possible = FindPossibleNumbers(row, col)
    
    
    for num in sorted(list(possible)):
        sudoku[row][col] = num 
        
        if sudokusolve(index + 1): #success next col try
            return True #if success the number stay
          
        sudoku[row][col] = 0 # put 0 and go back 
        
    return False


#start here -------------
if sudokusolve(0): #start from zero[index]
    print()
    for row in sudoku:
        print(*(row))
else:
  print('해답을 찾을 수 없습니다.')
