import pieces as p
from chartoint import dic
debug = 1

def printboard(board):
	print "-----BOARD-----"
	tmpboard = board
	for i in range(0,8):
		for j in range(0,8):
			if tmpboard[i][j] != 0:
				tmpboard[i][j] = tmpboard[i][j].team[0]
	for i in range(0,8):
		print tmpboard[i]
	print "-----BOARD-----"
	
def printboardraw(board):
	print "-----BOARD_RAW-----"
	for i in range(0,8):
		print board[i]
	print "-----BOARD_RAW-----"
	
board = [[0 for x in range(8)] for x in range(8)]

printboardraw(board)

kingwhite = p.King(3,3,"white")
kingblack = p.King(3,4,"black")
board[3][3] = kingwhite
board[3][4] = kingblack

printboardraw(board)

c = ""
while c != "quit" and c!= "exit":
	c=raw_input(">> ")
	cmd = c.split()
	if cmd[0] == "move":
		try:
			fromx = int(cmd[1][0])
			fromy = dic[cmd[1][1]]
			tox = int(cmd[2][0])
			toy = dic[cmd[2][1]]
			if debug:
				print "Bewegung von {}.{} nach {}.{}".format(fromx, fromy, tox, toy)
			print board[fromx][fromy]
			if board[fromx][fromy].checkValidTurn(tox,toy,board):
				board[tox][toy] = board[fromx][fromy]
				board[fromx][fromy] = 0
		except IndexError as i:
			print "INDEX ERROR"
	printboardraw(board)