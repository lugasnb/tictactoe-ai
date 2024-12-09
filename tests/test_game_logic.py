import pytest
from game_logic import GameLogic

# Test inisialisasi Game
def test_initialization():
    game = GameLogic()
    
    # Memastikan papan diinisialisasi dengan benar
    assert game.board == [' '] * 9
    # Memastikan pemain pertama adalah 'X'
    assert game.current_player == 'X'
    # Memastikan permainan belum selesai
    assert not game.game_over
    # Memastikan tidak ada pemenang di awal
    assert game.winner is None

# # Test gerakan pemain (Player Move)
# @pytest.fixture
# def test_player_move():
#     game = GameLogic()
    
#     # Pemain X membuat gerakan di posisi 0
#     game.make_move(0)
    
#     # Memastikan bahwa posisi 0 di papan sekarang adalah 'X'
#     assert game.board[0] == 'X'
#     # Memastikan giliran berpindah ke 'O' (AI)
#     assert game.current_player == 'O'
#     # Memastikan permainan belum berakhir
#     assert not game.game_over

# # Test gerakan AI (AI Move)
# @pytest.fixture
# def test_ai_move():
#     game = GameLogic()
    
#     # Pemain X membuat gerakan di posisi 0
#     game.make_move(0)
    
#     # Memastikan AI melakukan gerakan setelah pemain
#     # Misalnya AI memilih posisi 1 (disesuaikan dengan logika AI Anda)
#     assert game.board[1] == 'O'
#     # Memastikan giliran kembali ke 'X'
#     assert game.current_player == 'X'

# Test pengecekan kondisi permainan (Check Game State)
def test_check_game_state():
    game = GameLogic()
    
    # Mengatur papan untuk kemenangan horizontal
    game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    
    # Memeriksa status permainan setelah gerakan
    game.check_game_state()
    
    # Memastikan permainan berakhir dan ada pemenang 'X'
    assert game.game_over
    assert game.winner == 'X'

# Test game over (game berakhir jika tidak ada posisi kosong)
def test_game_over_draw():
    game = GameLogic()
    
    # Mengatur papan dengan hasil seri
    game.board = ['X', 'O', 'X', 'X', 'O', 'X', 'O', 'X', 'O']
    
    # Memeriksa status permainan setelah papan penuh
    game.check_game_state()
    
    # Memastikan permainan berakhir karena tidak ada posisi kosong
    assert game.game_over
    assert game.winner is None  # Tidak ada pemenang, hasil seri

# Test reset game
def test_reset_game():
    # Inisialisasi objek GameLogic
    game = GameLogic()

    # Simulasikan permainan dengan beberapa perubahan status
    game.board = ['X', 'O', 'X', 'O', 'X', ' ', ' ', ' ', ' ']
    game.current_player = 'O'
    game.game_over = True
    game.winner = 'X'

    # Panggil metode reset_game
    game.reset_game()

    # Pastikan papan direset ke keadaan awal
    assert game.board == [' '] * 9, "Board tidak direset dengan benar"

    # Pastikan giliran pemain direset ke 'X'
    assert game.current_player == 'X', "Giliran pemain tidak direset ke 'X'"

    # Pastikan game_over direset ke False
    assert not game.game_over, "Status game_over tidak direset ke False"

    # Pastikan pemenang direset ke None
    assert game.winner is None, "Pemenang tidak direset ke None"
