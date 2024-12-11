import random

class MinimaxAI:
    @staticmethod
    def best_move(board, player):
        """Mengembalikan posisi terbaik untuk AI berdasarkan algoritma Minimax."""
        opponent = 'X' if player == 'O' else 'O'
        best_score = float('-inf')
        move = None

        for i in range(len(board)):
            if board[i] == ' ':
                board[i] = player
                score = MinimaxAI.minimax(board, 0, False, player, opponent)
                board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i

        return move

    @staticmethod
    def minimax(board, depth, is_maximizing, player, opponent):
        winner = MinimaxAI.check_winner(board)
        if winner == player:
            return 10 - depth
        elif winner == opponent:
            return depth - 10
        elif ' ' not in board:
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(len(board)):
                if board[i] == ' ':
                    board[i] = player
                    score = MinimaxAI.minimax(board, depth + 1, False, player, opponent)
                    board[i] = ' '
                    best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(len(board)):
                if board[i] == ' ':
                    board[i] = opponent
                    score = MinimaxAI.minimax(board, depth + 1, True, player, opponent)
                    board[i] = ' '
                    best_score = min(best_score, score)
            return best_score

    @staticmethod
    def check_winner(board):
        """Mengecek siapa yang menang (X, O, atau None jika belum ada)."""
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for line in win_conditions:
            if board[line[0]] == board[line[1]] == board[line[2]] and board[line[0]] != ' ':
                return board[line[0]]
        return None
