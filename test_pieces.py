# -*- coding: utf-8 -*-

import unittest

from pieces import Tower, Runner
from board import addPiece


class TestTower(unittest.TestCase):
    def setUp(self):
        self.board = [[0] * 8 for i in range(8)]
        self.OUT = Tower(0, 0, 'white')
        addPiece(self.OUT, self.board)

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


class TestRunner(unittest.TestCase):
    def setUp(self):
        self.board = [[0] * 8] * 8
        self.OUT = Runner(3, 3, 'white')
        addPiece(self.OUT, self.board)

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
