import unittest
from game_logic import Game

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        """Set up a fresh game logic instance before each test."""
        self.game = Game()

    def test_initial_board(self):
        """Test if the board initializes correctly."""
        expected_board = [' '] * 9
        self.assertEqual(self.game.board, expected_board)

    def test_make_move(self):
        """Test if a valid move updates the board correctly."""
        self.assertTrue(self.game.make_move(0, 'X'))
        self.assertEqual(self.game.board[0], 'X')

    def test_invalid_move(self):
        """Test if making a move in a taken cell is invalid."""
        self.game.make_move(0, 'X')
        self.assertFalse(self.game.make_move(0, 'O'))

    def test_check_winner_horizontal(self):
        """Test if a horizontal win is detected."""
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game.check_winner('X'))
        self.assertFalse(self.game.check_winner('O'))

    def test_check_winner_vertical(self):
        """Test if a vertical win is detected."""
        self.game.board = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
        self.assertTrue(self.game.check_winner('O'))
        self.assertFalse(self.game.check_winner('X'))

    def test_check_winner_diagonal(self):
        """Test if a diagonal win is detected."""
        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.assertTrue(self.game.check_winner('X'))
        self.assertFalse(self.game.check_winner('O'))

    def test_draw(self):
        """Test if a draw is detected."""
        self.game.board = ['X', 'O', 'X', 'X', 'X', 'O', 'O', 'X', 'O']
        self.assertTrue(self.game.is_draw())
        self.assertFalse(self.game.check_winner('X'))
        self.assertFalse(self.game.check_winner('O'))

    def test_reset_game(self):
        """Test if the game resets correctly."""
        self.game.make_move(0, 'X')
        self.game.reset()
        self.assertEqual(self.game.board, [' '] * 9)

if __name__ == "__main__":
    unittest.main()
