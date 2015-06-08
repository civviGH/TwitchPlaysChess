# -*- coding: utf-8 -*-

import unittest

from pieces import Tower, Runner, Queen, Knight, Pawn
from board import addPiece
from abc import abstractmethod


class PieceTestCase(unittest.TestCase):
    @abstractmethod
    def getPiece(self):
        return

    def setUp(self):
        self.board = [[0] * 8 for i in range(8)]
        self.OUT = self.getPiece()
        addPiece(self.OUT, self.board)


class TestTower(PieceTestCase):
    def getPiece(self):
        return Tower(0, 0, 'white')

    def test_allowed_moves(self):
        self.assertTrue(self.OUT.checkValidTurn(0, 5))
        self.assertTrue(self.OUT.checkValidTurn(5, 0))

    def test_disallowed_moves(self):
        self.assertFalse(self.OUT.checkValidTurn(7, 7))

    def test_blockage(self):
        other_tower1 = Tower(0, 4, 'white')
        other_tower2 = Tower(4, 0, 'black')
        addPiece(other_tower1, self.board)
        addPiece(other_tower2, self.board)

        self.assertFalse(self.OUT.checkValidTurn(0, 7))
        self.assertFalse(self.OUT.checkValidTurn(7, 0))

    def test_out_of_board(self):
        self.assertFalse(self.OUT.checkValidTurn(0, 8))

    def test_move_to_self(self):
        self.assertFalse(self.OUT.checkValidTurn(0, 0))


class TestRunner(PieceTestCase):
    def getPiece(self):
        return Runner(3, 3, 'white')

    def test_allowed_moves(self):
        self.assertTrue(self.OUT.checkValidTurn(1, 1))
        self.assertTrue(self.OUT.checkValidTurn(7, 7))
        self.assertTrue(self.OUT.checkValidTurn(5, 1))
        self.assertTrue(self.OUT.checkValidTurn(1, 5))

    def test_disallowed_moves(self):
        self.assertFalse(self.OUT.checkValidTurn(3, 5))
        self.assertFalse(self.OUT.checkValidTurn(5, 3))
        self.assertFalse(self.OUT.checkValidTurn(1, 7))
        self.assertFalse(self.OUT.checkValidTurn(6, 7))

    def test_blockage(self):
        other_piece = Tower(5, 5, 'white')
        addPiece(other_piece, self.board)
        self.assertFalse(self.OUT.checkValidTurn(6, 6))
        self.assertTrue(self.OUT.checkValidTurn(4, 4))

    def test_target_area(self):
        other_friendly_piece = Tower(4, 4, 'white')
        other_enemy_piece = Tower(1, 1, 'black')
        addPiece(other_friendly_piece, self.board)
        addPiece(other_enemy_piece, self.board)
        self.assertFalse(self.OUT.checkValidTurn(4, 4))
        self.assertTrue(self.OUT.checkValidTurn(1, 1))

    def test_out_of_board(self):
        self.assertFalse(self.OUT.checkValidTurn(8, 8))

    def test_move_to_self(self):
        self.assertFalse(self.OUT.checkValidTurn(3, 3))


class TestQueen(PieceTestCase):
    def getPiece(self):
        return Queen(2, 5, 'white')

    def test_allowed_moves(self):
        self.assertTrue(self.OUT.checkValidTurn(3, 6))
        self.assertTrue(self.OUT.checkValidTurn(3, 5))
        self.assertTrue(self.OUT.checkValidTurn(7, 5))
        self.assertTrue(self.OUT.checkValidTurn(1, 4))
        self.assertTrue(self.OUT.checkValidTurn(1, 5))

    def test_disallowed_moves(self):
        self.assertFalse(self.OUT.checkValidTurn(2, 5))
        self.assertFalse(self.OUT.checkValidTurn(3, 3))
        self.assertFalse(self.OUT.checkValidTurn(8, 8))

    def test_out_of_board(self):
        self.assertFalse(self.OUT.checkValidTurn(5, 8))

    def test_target_area(self):
        other_friendly_piece = Tower(3, 6, 'white')
        other_enemy_piece = Tower(4, 5, 'black')
        addPiece(other_friendly_piece, self.board)
        addPiece(other_enemy_piece, self.board)
        self.assertFalse(self.OUT.checkValidTurn(3, 6))
        self.assertTrue(self.OUT.checkValidTurn(4, 5))

    def test_blockage(self):
        other_piece = Tower(2, 6, 'white')
        addPiece(other_piece, self.board)
        self.assertFalse(self.OUT.checkValidTurn(2, 7))


class TestKnight(PieceTestCase):
    def getPiece(self):
        return Knight(3, 4, 'white')

    def test_allowed_moves(self):
        self.assertTrue(self.OUT.checkValidTurn(1, 3))
        self.assertTrue(self.OUT.checkValidTurn(1, 5))
        self.assertTrue(self.OUT.checkValidTurn(2, 2))
        self.assertTrue(self.OUT.checkValidTurn(2, 6))
        self.assertTrue(self.OUT.checkValidTurn(4, 2))
        self.assertTrue(self.OUT.checkValidTurn(4, 6))
        self.assertTrue(self.OUT.checkValidTurn(5, 3))
        self.assertTrue(self.OUT.checkValidTurn(5, 5))

    def test_disallowed_moves(self):
        self.assertFalse(self.OUT.checkValidTurn(0, 4))
        self.assertFalse(self.OUT.checkValidTurn(0, 0))

    def test_target_area(self):
        other_friendly_piece = Tower(1, 3, 'white')
        other_enemy_piece = Tower(1, 5, 'black')
        addPiece(other_friendly_piece, self.board)
        addPiece(other_enemy_piece, self.board)
        self.assertFalse(self.OUT.checkValidTurn(1, 3))
        self.assertTrue(self.OUT.checkValidTurn(1, 5))

    def test_out_of_board(self):
        self.OUT = Knight(6, 6, 'white')
        addPiece(self.OUT, self.board)
        self.assertFalse(self.OUT.checkValidTurn(8, 7))

class TestWhitePawn(PieceTestCase):
    """
    on peasant noch nicht im test
    schlagen noch nicht im test
    promotion nicht im test
    """
    def getPiece(self):
        return Pawn(1,6, "white")
    
    def test_allowed_moves(self):
        self.assertTrue(self.OUT.checkValidTurn(1,5))
        self.assertTrue(self.OUT.checkValidTurn(1,4))
        
    def test_disallowed_moves(self):
        self.assertFalse(self.OUT.checkValidTurn(2,6))
        self.assertFalse(self.OUT.checkValidTurn(1,3))
        self.assertFalse(self.OUT.checkValidTurn(1,7))
        self.assertFalse(self.OUT.checkValidTurn(1,6))

    def test_target_area(self):
        other_friendly_piece = Tower(1,5,"white")
        addPiece(other_friendly_piece, self.board)
        self.assertFalse(self.OUT.checkValidTurn(1,5))
        other_pawn = Pawn(2,6,"white")
        addPiece(other_pawn, self.board)
        other_enemy_piece = Tower(2,5,"black")
        addPiece(other_enemy_piece, self.board)
        self.assertTrue(other_pawn.checkValidTurn(2,5))
            
    def test_out_of_board(self):
        self.OUT = Pawn(1,0,"white")
        addPiece(self.OUT, self.board)
        self.assertFalse(self.OUT.checkValidTurn(1,-1))
        
class TestBlackPawn(PieceTestCase):
    def getPiece(self):
        return Pawn(1,1, "black")
    
    def test_allowed_moves(self):
        self.assertTrue(self.OUT.checkValidTurn(1,2))
        self.assertTrue(self.OUT.checkValidTurn(1,3))
        
    def test_disallowed_moves(self):
        self.assertFalse(self.OUT.checkValidTurn(2,1))
        self.assertFalse(self.OUT.checkValidTurn(1,0))
        self.assertFalse(self.OUT.checkValidTurn(1,4))
        self.assertFalse(self.OUT.checkValidTurn(1,5))

    def test_target_area(self):
        other_friendly_piece = Tower(1,2,"black")
        addPiece(other_friendly_piece, self.board)
        self.assertFalse(self.OUT.checkValidTurn(1,2))
        other_pawn = Pawn(2,1,"black")
        addPiece(other_pawn, self.board)
        other_enemy_piece = Tower(2,2,"white")
        addPiece(other_enemy_piece, self.board)
        self.assertTrue(other_pawn.checkValidTurn(2,2))
            
    def test_out_of_board(self):
        self.OUT = Pawn(1,7,"black")
        addPiece(self.OUT, self.board)
        self.assertFalse(self.OUT.checkValidTurn(1,8))