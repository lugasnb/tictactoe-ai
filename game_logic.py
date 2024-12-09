from ai.minimax import MinimaxAI

class GameLogic:
    def __init__(self):
        self.board = [' '] * 9
        self.current_player = 'X'  # User selalu 'X'
        self.game_over = False
        self.winner = None

    def make_move(self, position):
        if not self.game_over and self.board[position] == ' ':
            self.board[position] = self.current_player
            self.check_game_state()
            if not self.game_over:
                self.switch_player()
                if self.current_player == 'O':  # AI's turn
                    ai_move = MinimaxAI.best_move(self.board, 'O')
                    if ai_move is not None:
                        self.make_move(ai_move)

    def check_game_state(self):
        self.winner = MinimaxAI.check_winner(self.board)
        if self.winner or ' ' not in self.board:
            self.game_over = True

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.board = [' '] * 9
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
