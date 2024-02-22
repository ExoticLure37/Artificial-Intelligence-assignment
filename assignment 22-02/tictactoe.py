#Aryan Maurya
#20223054
#prgm to implement tictactoe using minimax algorithm

player=1
opponent=-1

#move left
def isMoveLeft(b):
	for i in range(3):
		for j in range (3):
			if(b[i][j]==0):
				return True
	return False

#check for winner
def evaluate(b):
	#chk in row
	for r in range(3):
		if(b[r][0]==b[r][1] and b[r][1]==b[r][2]):
			if(b[r][0]==1):
				return +10
			elif(b[r][0]==-1):
				return -10
	
	#chk in col			
	for c in range(3):
		if(b[0][c]==b[1][c] and b[1][c]==b[2][c]):
			if(b[0][c]==1):
				return +10
			elif(b[0][c]==-1):
				return -10
	
	#chk in forward diagonal
	if(b[0][0]==b[1][1] and b[1][1]==b[2][2]):
		if(b[0][0]==1):
			return +10
		elif(b[0][0]==-1):
			return -10

	#chk in backward diagonal	
	if(b[0][2]==b[1][1] and b[1][1]==b[2][0]):
		if(b[0][2]==1):
			return +10
		elif(b[0][0]==-1):
			return -10

	return 0

def minimax(board, depth, isMax) :  
    score = evaluate(board)  
    if (score == 10) :  
        return score 
   
    if (score == -10) : 
        return score 
  
    if (isMoveLeft(board) == False) : 
        return 0
  
    # If this maximizer's move  
    if (isMax) :      
        best = -1000   
        for i in range(3) :          
            for j in range(3) : 
                # Check if cell is empty  
                if (board[i][j]==0) :   
                    board[i][j] = player   
                    best = max( best, minimax(board, depth + 1, not isMax) ) 
                    board[i][j] = 0
        return best 
    # If this minimizer's move  
    else : 
        best = 1000  
        for i in range(3) :          
            for j in range(3) : 
                # Check if cell is empty  
                if (board[i][j] == 0) :  
                    board[i][j] = opponent  
                    best = min(best, minimax(board, depth + 1, not isMax)) 
                    board[i][j] = 0
        return best 

def findBestMove(b):
	bestVal = -1000
	bestMove=(-1,-1)
		
	for i in range(3):
		for j in range(3):
			if(b[i][j]==0):
				b[i][j]=1
				MoveVal = minimax(b,0,False)
				b[i][j]=0
				if(MoveVal>bestVal):
					bestVal = MoveVal
					bestMove = (i,j)  
					
	print("The value of the best Move is :", bestVal) 
	print() 
	return bestMove 
# Driver code 
board = [ 
    [ 1,0,0 ],  
    [ 0,0,0 ],  
    [ 0,0,0 ]  
] 
  
bestMove = findBestMove(board)  
  
print("The Optimal Move is : ")  
print("ROW:", bestMove[0], " COL:", bestMove[1]) 