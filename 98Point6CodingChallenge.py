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
class MainBoardLogic:

	# Default global Variables
	columnsPutArray = []
	playerTurn = 1
	

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
					elif 1 <= j < self.col + 1:
						print(j, end=" ")
			print("\n")


	'''
		Function helper that get the list of columns succesfully assigned in the matrix board game
	'''
	def getListOfColumns(self):
		for col in self.columnsPutArray:
			print(col)

	
	'''
		Function helper that get the number of columns that assigned at the constructor
	'''
	def getNumberOfColumn(self):
		return self.col
		
		
	'''
		Function helper to get out the number of rows that assigned at the row
	'''
	def getNumberOfRow(self):
		return self.row


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


	'''
		Function helper to determine if which player win the game by checking horizontal, vertical and diagonal side.
		Param:
			+ col: The column that just assigned the value
	'''
	def whoWon(self, col):
		leftDiagonal = rightDiagonal = vertical = horizontal = 0

		# Check the vertical
		for row in range(self.row - 1, -1, -1):
			if self.matrixBoard[row][col] == 1:
				vertical += 1
			elif self.matrixBoard[row][col] == 2:
				vertical -= 1

		# Check the horizontal
		for checkCol in range(self.col):
			if self.matrixBoard[self.currentRow][checkCol] == 1:
				horizontal += 1
			elif self.matrixBoard[self.currentRow][checkCol] == 2:
				horizontal -= 1

		# Check the diagonal on left
		for row in range(self.row):
			if self.matrixBoard[row][row] == 1:
				leftDiagonal += 1
			elif self.matrixBoard[row][row] == 1:
				leftDiagonal -= 1

		# Check the diagonal on right
		if leftDiagonal != self.col or leftDiagonal != -(self.col):
			currCol = self.col - 1

			for row in range(self.row):
				if self.matrixBoard[row][currCol] == 1:
					rightDiagonal += 1
				elif self.matrixBoard[row][currCol] == 2:
					rightDiagonal -= 1
				currCol -= 1

		print("vertical: ", vertical)
		print("horizontal: ", horizontal)
		print("left diagonal: ", leftDiagonal)
		print("right diagonal: ", rightDiagonal)

		# If either vertical, horizontal or diagonals has all equal value then it end the game
		if vertical == self.col or vertical == -(self.col) or horizontal == self.col or horizontal == -(self.col) or leftDiagonal == self.col or leftDiagonal == -(self.col) or rightDiagonal == self.col or rightDiagonal == -(self.col):
			return self.matrixBoard[col][col]
		else:
			return -1


	'''
		Function helper to check if the position assign is valid location
		Param:
			+ col: The column need to check if valid or not
	'''
	def checkValidPosition(self, col):
		if col > self.col or col < 0:
			return "ERROR"


	'''
		Function helper that get the player turn
	'''
	def getPlayerTurn(self):
		return self.playerTurn


	'''
		Function helper that set the new player turn
		param:
			+ turn: The new turn for new player
	'''
	def setPlayerTurn(self, turn):
		self.playerTurn = turn


	'''
		Function helper that keep track of the list of columns successfully added
		param:
			+ putLocation: The location has been successfully added
	'''
	def newTokenDropPosition(self, putLocation):
		self.columnsPutArray.append(putLocation)


	'''
		Function helper that help user to see the list of command list allow to use
	'''
	def helperCommandList(self):
		hashDict = {
			"PUT <Col>" : "OK | ERROR | WIN | DRAW",
			"GET" : "List of columns that have been successfully put to",
			"BOARD" : "Get a 4x4 matrix that shows the board state",
			"EXIT" : "Ends the program"
		}
		for key in hashDict:
			print(". " + key + ": " + hashDict[key])


# Main solution class
class Solution(MainBoardLogic):

	def dropTokenGame(self):
		gameNotEnd = True
		while(gameNotEnd):
			command = input("> ").lower() # Ask the user input
			if command == 'exit':
				self.exitTheGame()
			elif command == 'board':
				self.getBoardGame()
			elif command == 'get':
				self.getListOfColumns()
			elif "put " in command:
				command, columnToAdd = command.split(" ")
				try:
					columnToAdd = int(columnToAdd)
					currentStatus = self.putAtColumn(columnToAdd)
					print(currentStatus)
				except:
					print("Please enter valid command. Example <PUT 1>")
			elif command == "help":
				self.helperCommandList()
			else:
				print("Please enter valid command or hit <HELP> for more details")


# Driver	
try:
	print("Welcome to Drop Token Game!!! \n")
	numberOfRow = int(input("Number of row: "))
	numberOfCol = int(input("number of col: "))
	if numberOfCol != numberOfRow:
		print("Please double check the number of rows and columns that you put in. To be able to play the game the matrix board must be a square matrix. Ex: 4x4")
	else:
		gameStart = Solution(numberOfRow, numberOfCol)
		gameStart.dropTokenGame()
except:
	print("Please enter the valid integer number")