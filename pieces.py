debug = 1

class King:
	def __init__(self, xpos, ypos, team):
		self.position = [xpos, ypos]
		self.team = team
		self.doesJump = False
		self.name = "King {}".format(team)
	
	def checkValidTurn(self, tox, toy, board):
		if abs(self.position[0]-tox) <= 1 and abs(self.position[1]-toy) <= 1:
			if board[tox][toy] == 0:
				if debug:
					print "Bewegung von {} erfolgreich".format(self.name)
				return 1
			elif board[tox][toy].team == self.team:
				if debug:
					print "Bewegung von {} durch Figur eigenes Teams aufgehalten".format(self.name) 
				return 0
			else:
				if debug:
					print "Bewegung von {} erfolgreich, {} dabei geschlagen".format(self.name,board[tox][toy].name)
				return 1
		if debug:
			print "Bewegung von {} nicht moeglich".format(self.name)
		return 0
		
	def updatePosition(self, xpos, ypos):
		self.position = [xpos, ypos]
	
	def drawSelf(self, canvas):
		canvas.create_rectangle(self.position[0]*110+30, self.position[1]*110+30, self.position[0]*110+80, self.position[1]*110+80, fill = self.team)

class Lady:
	def __init__(self, xpos, ypos, team):
		self.position = [xpos, ypos]
		self.team = team
		self.doesJump = False
		self.name = "Lady {}".format(team)
	
	def checkValidTurn(self, tox, toy, board):
		pass
		
	def updatePosition(self, xpos, ypos):
		pass
		
	def drawSelf(self, canvas):
		pass
	
class Tower:
	def __init__(self, xpos, ypos, team):
		self.position = [xpos, ypos]
		self.team = team
		self.doesJump = False
		self.name = "Tower {}".format(team)
	
	def checkValidTurn(self, tox, toy, board):
		posx = self.position[0]
		posy = self.position[1]
		#check if target is position
		try:
			if board[tox][toy].team == self.team:
				if debug:
					print "Bewegung von {} durch Figur eigenes Teams aufgehalten".format(self.name) 
				return 0
		except AttributeError as a:
			pass
		#moving along y axis
		if tox == posx and abs(posy - toy) > 1:
			if posy > toy:
				#check every field between pos and target
				for i in range(toy+1, posy):
					#if obstacle found
					if board[posx][i] != 0:
						if debug:
							print "Bewegung von {} nicht moeglich, Hinderniss bei x:{}, y:{}".format(self.name,posx,i)
						return 0
				#else unit can passthrough
				return 1
			else:
				#check every field between pos and target
				for i in range(posy+1, toy):
					if board[posx][i] != 0:
						if debug:
							print "Bewegung von {} nicht moeglich, Hinderniss bei x:{}, y:{}".format(self.name,posx,i)
						return 0
				return 1
		#moving along x axis
		elif toy == posy and abs(posx - tox) > 1:
			if posx > tox:
				for i in range(tox+1, posx):
					if board[i][posy] != 0:
						if debug:
							print "Bewegung von {} nicht moeglich, Hinderniss bei x:{}, y:{}".format(self.name,posx+1,i)
						return 0
				return 1
			else:
				for i in range(posx+1, tox):
					if board[i][posy] != 0:
						if debug:
							print "Bewegung von {} nicht moeglich, Hinderniss bei x:{}, y:{}".format(self.name,posx+1,i)
						return 0
				return 1
		elif toy != posy and tox != posx:
			if debug:
				print "Bewegung von {} diagonal nicht moeglich".format(self.name)
			return 0
		return 1
		
	def updatePosition(self, xpos, ypos):
		self.position = [xpos, ypos]
		
	def drawSelf(self, canvas):
		canvas.create_rectangle(self.position[0]*110+30, self.position[1]*110+30, self.position[0]*110+80, self.position[1]*110+80, fill = self.team)
		canvas.create_line(self.position[0]*110+55, self.position[1]*110+30, self.position[0]*110+55, self.position[1]*110+80, fill = "red", width = 2) 
	
class Runner:
	def __init__(self, xpos, ypos, team):
		self.position = [xpos, ypos]
		self.team = team
		self.doesJump = False
		self.name = "Runner {}".format(team)
		
	def __minimum(self, x, y):
		if x > y:
			return y
		else:
			return x
		
	def checkValidTurn(self, tox, toy, board):
		pass
		
	def updatePosition(self, xpos, ypos):
		pass
		
	def drawSelf(self, canvas):
		pass
		
	
class Horse:
	def __init__(self, xpos, ypos, team):
		self.position = [xpos, ypos]
		self.team = team
		self.doesJump = True
		self.name = "Horse {}".format(team)
	
	def checkValidTurn(self, tox, toy, board):
		pass
		
	def updatePosition(self, xpos, ypos):
		pass
		
	def drawSelf(self, canvas):
		pass
	
class Peasant:
	def __init__(self, xpos, ypos, team):
		self.position = [xpos, ypos]
		self.team = team
		self.doesJump = False
		self.name = "Peasant {}".format(team)
	
	def checkValidTurn(self, tox, toy, board):
		pass
		
	def updatePosition(self, xpos, ypos):
		pass
		
	def drawSelf(self, canvas):
		pass