import tkinter as tk
from tkinter import messagebox
import random

# Representasi papan permainan
board = [' ' for _ in range(9)]

# Simbol pemain dan komputer
PLAYER = 'X'
AI = 'O'

# Status permainan
game_started = False

# Mengecek apakah ada pemenang
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
    ]
    
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

# Mengecek apakah papan penuh
def is_board_full(board):
    return ' ' not in board

# Fungsi minimax untuk menentukan langkah terbaik
def minimax(board, depth, is_maximizing):
    if check_winner(board, AI):
        return 10 - depth
    if check_winner(board, PLAYER):
        return depth - 10
    if is_board_full(board):
        return 0

    if is_maximizing:
        best = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = AI
                best = max(best, minimax(board, depth + 1, False))
                board[i] = ' '
        return best
    else:
        best = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = PLAYER
                best = min(best, minimax(board, depth + 1, True))
                board[i] = ' '
        return best

# Fungsi untuk menemukan langkah terbaik bagi AI
def best_move(board):
    best_value = -float('inf')
    move = -1

    for i in range(9):
        if board[i] == ' ':
            board[i] = AI
            move_value = minimax(board, 0, False)
            board[i] = ' '
            if move_value > best_value:
                best_value = move_value
                move = i

    return move

# Fungsi untuk memperbarui tombol GUI
def update_button(index, player):
    color = "#e74c3c" if player == PLAYER else "#3498db"
    buttons[index].config(text=player, state="disabled", fg=color)
    board[index] = player

# Fungsi untuk menjalankan permainan
def play_game(index):
    global game_started
    if not game_started:
        return

    if board[index] != ' ':
        return

    # Langkah pemain
    update_button(index, PLAYER)

    # Cek kemenangan atau seri setelah langkah pemain
    if check_winner(board, PLAYER):
        messagebox.showinfo("Menang", "Selamat, Anda menang!")
        reset_game()
        return
    if is_board_full(board):
        messagebox.showinfo("Seri", "Permainan berakhir dengan seri!")
        reset_game()
        return

    # Langkah AI
    ai_move = best_move(board)
    update_button(ai_move, AI)

    # Cek kemenangan atau seri setelah langkah AI
    if check_winner(board, AI):
        messagebox.showinfo("Kalah", "AI menang!")
        reset_game()
        return
    if is_board_full(board):
        messagebox.showinfo("Seri", "Permainan berakhir dengan seri!")
        reset_game()

# Fungsi untuk mereset permainan
def reset_game():
    global board, game_started
    board = [' ' for _ in range(9)]
    for button in buttons:
        button.config(text=' ', state="normal", fg="black")
    game_started = False
    start_reset_button.config(text="Start Game", bg="#2ecc71", fg="white")

# Fungsi untuk memulai permainan
def start_game():
    global game_started
    if not game_started:
        game_started = True
        start_reset_button.config(text="Reset Game", bg="#e74c3c", fg="white")
    else:
        reset_game()

# Membuat jendela utama
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("350x470")
root.resizable(True, True)

# Frame untuk seluruh UI
main_frame = tk.Frame(root)
main_frame.pack(pady=20, expand=True)

# Judul permainan
title_label = tk.Label(main_frame, text="Tic-Tac-Toe", font=("Arial", 20, "bold"), fg="#2c3e50")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Frame untuk papan permainan
board_frame = tk.Frame(main_frame)
board_frame.grid(row=1, column=0, columnspan=3, pady=10)

# Membuat tombol untuk setiap kotak pada papan permainan
buttons = []
for i in range(9):
    button = tk.Button(board_frame, text=' ', width=4, height=2, font=("Arial", 18), 
                       command=lambda i=i: play_game(i), padx=5, pady=5, relief="solid")
    button.grid(row=i//3, column=i%3, padx=2, pady=2, sticky="nsew")
    buttons.append(button)

# Mengatur agar grid meng-expand sesuai ukuran jendela
for i in range(3):
    board_frame.grid_columnconfigure(i, weight=1, uniform="equal")
    board_frame.grid_rowconfigure(i, weight=1, uniform="equal")

# Frame untuk tombol Start/Reset
control_frame = tk.Frame(main_frame, bg="#2c3e50")
control_frame.grid(row=2, column=0, columnspan=3, pady=10)

# Tombol Start/Reset
start_reset_button = tk.Button(control_frame, text="Start Game", font=("Arial", 14), command=start_game, bg="#2ecc71", fg="white", relief="solid")
start_reset_button.pack()

# Menjalankan aplikasi
root.mainloop()
