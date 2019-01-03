
# ***Description***
* Drop Token takes place on a 4x4 grid. A token is dropped along a column (labeled 1-4) and said token goes to the lowest unoccupied row of the board. 
* A player wins when they have 4 tokens next to each other either along a row, in a column, or on a diagonal.
* If the board is filled, and nobody has won then the game is a draw. Each player takes a turn, starting with player 1, until the game reaches either win or draw. If a player tries to put a token in a column that is already full, that results in an error state, and the player must play again until the play a valid move. 

# ***Commands***
1. PUT -> <column> (OK | ERROR | WIN | DRAW) 
2. GET -> List of columns that have been successfully put to 
3. BOARD -> a 4x4 matrix that shows the board state 
	* Where 0s are unfilled columns, 1 is player 1, 2 is player 2
4. EXIT -> ends the program. 
5. HELP -> shows catalog of the list of command allow to use

# ***Sample Interface***
```
Welcome to Drop Token Game!!!

Number of row: 4
Number of col: 4
> board
     | 0 0 0 0
     | 0 0 0 0
     | 0 0 0 0
     | 0 0 0 0
     +--------
       1 2 3 4
```



