import numpy as np


def check(data,row,col,k):
	for n in range(9):
		if data[row][n] == k:
			return False

	for m in range(9):
		if data[m][col] == k:
			return False

	p = (row//3)*3
	q = (col//3)*3
	for m in range(p,p+3):
		for n in range(q,q+3):
			if data[m][n] == k:
				return False
	return True

def sodo(data,number):
	row = number //9
	col = number % 9
	if data[row][col] != '.':
		if number == 80:
			return
		else:
			sodo(data,number+1)
	else:
		for k in ['1','2','3','4','5','6','7','8','9']:
			if check(data,row,col,k):
				data[row][col] = k
				if number == 80:
					return
				else:
					sodo(data,number+1)
				data[row][col] = '.'


def sudoku(board):
	sodo(board, 0)
	print(board)

if __name__ == '__main__':
	data = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
	]
	
	sudoku(data)




