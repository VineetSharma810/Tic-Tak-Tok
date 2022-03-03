
player, opponent = 'x', 'o'


def isMovesLeft(board) :

	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == '_') :
				return True
	return False
#This will check whether anyplaer has won the game or not
def evaluate(b) :

	# Checking for Rows for X or O victory.
	for row in range(3) :	
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :	
			if (b[row][0] == player) :
				return 10
			elif (b[row][0] == opponent) :
				return -10

	# Checking for Columns for X or O victory.
	for col in range(3) :
	
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
		
			if (b[0][col] == player) :
				return 10
			elif (b[0][col] == opponent) :
				return -10

	# Checking for Diagonals for X or O victory.
	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
	
		if (b[0][0] == player) :
			return 10
		elif (b[0][0] == opponent) :
			return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
	
		if (b[0][2] == player) :
			return 10
		elif (b[0][2] == opponent) :
			return -10

	# Else if none of them have won then return 0
	return 0


def minimax(board, depth, isMax) :
	score = evaluate(board)

	if (score == 10) :
		return score

	if (score == -10) :
		return score

	if (isMovesLeft(board) == False) :
		return 0

	if (isMax) :	
		best = -1000

		# Traverse all cells
		for i in range(3) :		
			for j in range(3) :
			
				# Check if cell is empty
				if (board[i][j]=='_') :
				
					# Make the move
					board[i][j] = player

					# Call minimax recursively and choose
					# the maximum value
					best = max( best, minimax(board,
											depth + 1,
											not isMax) )

					# Undo the move
					board[i][j] = '_'
		return best

	# If this minimizer's move
	else :
		best = 1000

		# Traverse all cells
		for i in range(3) :		
			for j in range(3) :
			
				# Check if cell is empty
				if (board[i][j] == '_') :
				
					# Make the move
					board[i][j] = opponent

					# Call minimax recursively and choose
					# the minimum value
					best = min(best, minimax(board, depth + 1, not isMax))

					# Undo the move
					board[i][j] = '_'
		return best

# This will return the best possible move for the player
def findBestMove(board) :
	bestVal = -1000
	bestMove = (-1, -1)

	for i in range(3) :	
		for j in range(3) :
		
			# Check if cell is empty
			if (board[i][j] == '_') :
			
				# Make the move
				board[i][j] = player

				# compute evaluation function for this
				# move.
				moveVal = minimax(board, 0, False)

				# Undo the move
				board[i][j] = '_'

				# If the value of the current move is
				# more than the best value, then update
				# best/
				if (moveVal > bestVal) :			
					bestMove = (i, j)
					bestVal = moveVal

	print("The value of the best Move is :", bestVal)
	print()
	return bestMove

#print Board 
def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()
   
# Driver code
board = [
	[ '_', '_', '_' ],
	[ '_', '_', '_' ],
	[ '_', '_', '_' ]
]

print("In the Game of Tic-Tak-Tok you are O and AI is {}".format(opponent))
printBoard(board)
while True:
    rPlace = int(input("Enter row number  0-2 "))
    cPlace = int(input("Enter col number  0-2 "))
    board[rPlace][cPlace] = opponent
    print("You have placed at {rPlace} row and {cPlace} column")
    printBoard(board)
    print()
    bestMove = findBestMove(board)
    board[bestMove[0]][bestMove[1]] = player
    print("AI has placed at Row {} and Col {} ".format(bestMove[0], bestMove[1]))
    printBoard(board)
    print()
    if evaluate(board) == 10:
        print("Player X has won the game")
    elif evaluate(board) == -10:
        print("Player O has won the game")
    if not isMovesLeft(board):
        print("No one has won the Game")
        break;