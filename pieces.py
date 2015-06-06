# -*- coding: utf-8 -*-
from abc import ABCMeta

# #decide if debugging is printed to console
# 1 = true
debug = 0


class Piece:
    __metaclass__ = ABCMeta

    def checkValidTurn(self, tox, toy):
        if tox < 0:
            return 0
        if toy < 0:
            return 0
        if tox > 7:
            return 0
        if toy > 7:
            return 0
        return 1


class King(Piece):
    def __init__(self, xpos, ypos, team):
        self.board = None
        self.position = [xpos, ypos]
        self.team = team

        # dont know if needed yet
        self.doesJump = False
        self.name = "King {}".format(team)

    def __str__(self):
        return 'K'

    # check for a point and the board if a turn is valid
    def checkValidTurn(self, tox, toy):
        if not super(King, self).checkValidTurn(tox, toy):
            return 0
        """
        koennte umgeschrieben werden zu:
            try:
                if board[tox][toy].team == self.team:
                    return 0
                return 1
            except AttributeError as a:
                return 1
        """

        # check if distance to target is 1
        if abs(self.position[0] - tox) <= 1 and abs(self.position[1] - toy) <= 1:
            # target field is empty
            if self.board[tox][toy] == 0:
                if debug:
                    print "Bewegung von {} erfolgreich".format(self.name)
                return 1
            # piece of own team blocks move
            elif self.board[tox][toy].team == self.team:
                if debug:
                    print "Bewegung von {} durch Figur eigenes Teams aufgehalten".format(self.name)
                return 0
            # enemy piece on target, valid move
            else:
                if debug:
                    print "Bewegung von {} erfolgreich, {} dabei geschlagen".format(self.name,
                                                                                    self.board[tox][toy].name)
                return 1
        if debug:
            print "Bewegung von {} nicht moeglich".format(self.name)
        return 0

    def updatePosition(self, xpos, ypos):
        self.position = [xpos, ypos]

    # draw piece on board, dimensions hardcoded atm
    def drawSelf(self, canvas):
        canvas.create_rectangle(self.position[0] * 110 + 30, self.position[1] * 110 + 30, self.position[0] * 110 + 80,
                                self.position[1] * 110 + 80, fill=self.team)


class Queen(Piece):
    def __init__(self, xpos, ypos, team):
        self.board = None
        self.position = [xpos, ypos]
        self.team = team
        self.doesJump = False
        self.name = "Lady {}".format(team)

    """
    TODO
    """

    def checkValidTurn(self, tox, toy):
        if not super(Queen, self).checkValidTurn(tox, toy):
            return 0


    def updatePosition(self, xpos, ypos):
        pass

    def drawSelf(self, canvas):
        pass


class Tower(Piece):
    def __init__(self, xpos, ypos, team):
        self.board = None
        self.position = [xpos, ypos]
        self.team = team
        self.doesJump = False
        self.name = "Tower {}".format(team)

    # check for a point and the board if a turn is valid
    def checkValidTurn(self, tox, toy):
        if not super(Tower, self).checkValidTurn(tox, toy):
            return 0

        # own position
        posx = self.position[0]
        posy = self.position[1]
        # check if target position is held by teammate
        try:
            if self.board[tox][toy].team == self.team:
                if debug:
                    print "Bewegung von {} durch Figur eigenes Teams aufgehalten".format(self.name)
                return 0
        # throws exception on board[tox][toy] == 0
        except AttributeError as a:
            pass

        # moving along y axis
        if tox == posx and abs(posy - toy) > 1:


            """
            koennte in eine funktion ausgelagert werden,
            die fuer zwei beliebige natuerliche zahlen  x,y alle
            zahlen dazwischen gibt, so dass zb
                foo(7,3) -> [4,5,6] etc
            """

            # check for range(x,y), as it only works with x < y
            if posy > toy:

                # check every field between pos and target
                for i in range(toy + 1, posy):
                    # if obstacle found
                    if self.board[posx][i] != 0:
                        if debug:
                            print "Bewegung von {} nicht moeglich, Hinderniss bei x:{}, y:{}".format(self.name, posx, i)
                        return 0
                # else unit can passthrough
                return 1
            else:
                # check every field between pos and target
                for i in range(posy + 1, toy):
                    if self.board[posx][i] != 0:
                        if debug:
                            print "Bewegung von {} nicht moeglich, Hinderniss bei x:{}, y:{}".format(self.name, posx, i)
                        return 0
                return 1

        # moving along x axis, same checks as above
        elif toy == posy and abs(posx - tox) > 1:
            if posx > tox:
                for i in range(tox + 1, posx):
                    if self.board[i][posy] != 0:
                        if debug:
                            print "Bewegung von {} nicht moeglich, Hinderniss bei x:{}, y:{}".format(self.name,
                                                                                                     posx + 1, i)
                        return 0
                return 1
            else:
                for i in range(posx + 1, tox):
                    if self.board[i][posy] != 0:
                        if debug:
                            print "Bewegung von {} nicht moeglich, Hinderniss bei x:{}, y:{}".format(self.name,
                                                                                                     posx + 1, i)
                        return 0
                return 1
        # check for diagonal movement
        elif toy != posy and tox != posx:
            if debug:
                print "Bewegung von {} diagonal nicht moeglich".format(self.name)
            return 0
        return 1

    def updatePosition(self, xpos, ypos):
        self.position = [xpos, ypos]

    # square with line from top to bottom
    def drawSelf(self, canvas):
        canvas.create_rectangle(self.position[0] * 110 + 30, self.position[1] * 110 + 30, self.position[0] * 110 + 80,
                                self.position[1] * 110 + 80, fill=self.team)
        canvas.create_line(self.position[0] * 110 + 55, self.position[1] * 110 + 30, self.position[0] * 110 + 55,
                           self.position[1] * 110 + 80, fill="red", width=2)


class Runner(Piece):
    def __init__(self, xpos, ypos, team):
        self.board = None
        self.position = [xpos, ypos]
        self.team = team
        self.doesJump = False
        self.name = "Runner {}".format(team)

    def __minimum(self, x, y):
        if x > y:
            return y
        else:
            return x

    """
    TODO
    """

    def checkValidTurn(self, tox, toy, board):
        if not super(Runner, self).checkValidTurn(tox, toy, board):
            return 0

    def updatePosition(self, xpos, ypos):
        pass

    def drawSelf(self, canvas):
        pass


class Horse(Piece):
    def __init__(self, xpos, ypos, team):
        self.board = None
        self.position = [xpos, ypos]
        self.team = team
        self.doesJump = True
        self.name = "Horse {}".format(team)

    """
    TODO
    """

    def checkValidTurn(self, tox, toy):
        if not super(Horse, self).checkValidTurn(tox, toy):
            return 0

    def updatePosition(self, xpos, ypos):
        pass

    def drawSelf(self, canvas):
        pass


class Peasant(Piece):
    def __init__(self, xpos, ypos, team):
        self.position = [xpos, ypos]
        self.team = team
        self.doesJump = False
        self.name = "Peasant {}".format(team)

    """
    TODO
    """

    def checkValidTurn(self, tox, toy):
        if not super(Peasant, self).checkValidTurn(tox, toy):
            return 0

    def updatePosition(self, xpos, ypos):
        pass

    def drawSelf(self, canvas):
        pass