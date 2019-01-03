'''
98 Point 6 Drop Token Game Challenge:

Description:
	Implement a command line program that allows two people to play a game of 9dt, or 98point6 drop token.
	This should allow the players to alternate turns, tell a player that they won with the last move, and print out the board on demand.

Game Rule:
	+ Place on a 4x4 grid
	+ A Token dropped along a column (labeled 1-4) and token goes to the lowest unoccupied row of the board.
	+ Player wins when they have 4 tokens next to each other either along a row, in a column, or on a diagonal.
	+ Players draw if the board is filled, and nobody has won then the game is a draw.
	+ Each player takes turn, starting with player 1, until the game reaches either win or draw.
	+ If the player tried to put a toke in a column that is already full, that result in an error state, and the player must play again until the play valid move.

Commands:
	+ PUT <column> -> OK | ERROR | WIN | DRAW
	+ GET -> List of columns that have been successfully put to
	+ BOARD -> A 4x4 matrix that shows the board state
	+ EXIT -> Ends the program
Where 0 is unfilled, 1 is player 1, and 2 is player 2.
'''
import sys
class Interface:

	'''
		Constructor
		param:
			+ row: The row need to set for the matrix board game
			+ col: The col need to set for the matrix board
	'''
	def __init__(self, row, col):
		self.row = row
		self.col = col
		self.matrixBoard = [[0 for _ in range(col)] for _ in range(row)]
		self.columnsPutArray = []
		self.playerTurn = 1
		self.currentRow = row - 1


	'''
		Function helper that generate the matrix board game command line
	'''
	def getBoardGame(self):
		for col in range(self.col):
			print('|', end=" ")
			for row in range(self.row):
				print(self.matrixBoard[col][row], end =" ")
			print("\n")

		for i in range(2):
			for j in range(self.col * 2 + 1):
				if i == 0:
					if j == 0:
						print("+", end="")
					else:
						print("-", end="")
				else:
					if j == 0:
						print(" ", end=" ")
					elif 1 <= j < 5:
						print(j, end=" ")
			print("\n")


	'''
		Function helper that get the list of columns succesfully assigned in the matrix board game
	'''
	def getListOfColumns(self):
		for col in self.columnsPutArray:
			print(col)


	'''
		Function helper to quit the game
	'''
	def exitTheGame(self):
		sys.exit()


	'''
		Function helper to put the specific value at the specific column
		Param:
			+ col: The column that need to assign value
	'''
	def putAtColumn(self, col):
		self.checkValidPosition(col)
		for row in range(self.row - 1, -1, -1): # Reverse order, bottom up
			newCol = col - 1
			if self.matrixBoard[row][newCol] == 0:
				self.currentRow = row # set the current row need to check
				self.matrixBoard[row][newCol] = self.getPlayerTurn()
				self.newTokenDropPosition(col)
				if (self.whoWon(newCol) != -1):
					return "WIN"
				if (len(self.columnsPutArray) == (self.row * self.col)):
					return "DRAW"
				newTurn = 2 if self.getPlayerTurn() == 1 else 1
				self.setPlayerTurn(newTurn)
				return "OK"
		return "ERROR"