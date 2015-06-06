# -*- coding: utf-8 -*-

import unittest

from pieces import Tower
from board import addPiece


class TestTower(unittest.TestCase):
    def setUp(self):
        self.board = [[0] * 8] * 8
        self.tower = Tower(0, 0, 'white')
        addPiece(self.tower, self.board)

    def test_allowed_moves(self):
        self.assertTrue(self.tower.checkValidTurn(0, 5, self.board))

    def test_disallowed_moves(self):
        self.assertFalse(self.tower.checkValidTurn(7, 7, self.board))

    def test_blockade(self):
        other_tower1 = Tower(0, 4, 'white')
        other_tower2 = Tower(4, 0, 'black')
        addPiece(other_tower1, self.board)
        addPiece(other_tower2, self.board)

        self.assertFalse(self.tower.checkValidTurn(0, 7, self.board))
        self.assertFalse(self.tower.checkValidTurn(7, 0, self.board))

    def test_out_of_board(self):
        self.assertFalse(self.tower.checkValidTurn(0, 8, self.board))