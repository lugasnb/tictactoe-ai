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

# Menampilkan papan permainan
def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

# Mengecek apakah ada pemenang
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
        [0, 4, 8], [2, 4, 6]             # Diagonal
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

# Fungsi untuk memperbarui GUI
def update_button(index, player):
    buttons[index].config(text=player, state="disabled", bg="#f1c40f" if player == PLAYER else "#e74c3c")
    board[index] = player

# Fungsi untuk menjalankan permainan
def play_game(index):
    global game_started
    if not game_started:
        return

    if board[index] != ' ':
        return

    update_button(index, PLAYER)

    if check_winner(board, PLAYER):
        messagebox.showinfo("Menang", "Selamat, Anda menang!")
        reset_game()
        return
    if is_board_full(board):
        messagebox.showinfo("Seri", "Permainan berakhir dengan seri!")
        reset_game()
        return

    # Giliran AI
    ai_move = best_move(board)
    update_button(ai_move, AI)

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
        button.config(text=' ', state="normal", bg="#ecf0f1")
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

# Mengatur lebar dan tinggi jendela (resizeable)
root.geometry("600x700")
root.resizable(True, True)  # Membuat jendela dapat diubah ukurannya

# Frame untuk seluruh UI
main_frame = tk.Frame(root)
main_frame.pack(pady=20, expand=True)

# Judul permainan
title_label = tk.Label(main_frame, text="Tic-Tac-Toe", font=("Arial", 20, "bold"), fg="#2c3e50")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Frame untuk papan permainan
board_frame = tk.Frame(main_frame)
board_frame.grid(row=1, column=0, columnspan=3, pady=10)

# Membuat tombol untuk setiap kotak pada papan permainan dengan ukuran lebih kecil
buttons = []
for i in range(9):
    button = tk.Button(board_frame, text=' ', width=4, height=2, font=("Arial", 16), 
                       command=lambda i=i: play_game(i), padx=5, pady=5, bg="#ecf0f1", relief="solid")
    button.grid(row=i//3, column=i%3, padx=5, pady=5, sticky="nsew")  # Menambahkan jarak antar tombol dan memastikan kotak persegi
    buttons.append(button)

# Mengatur agar grid meng-expand sesuai dengan ukuran jendela
for i in range(3):
    board_frame.grid_columnconfigure(i, weight=1, uniform="equal")
    board_frame.grid_rowconfigure(i, weight=1, uniform="equal")

# Frame untuk tombol Start/Reset
control_frame = tk.Frame(main_frame, bg="#2c3e50")
control_frame.grid(row=2, column=0, columnspan=3, pady=20)

# Tombol Start/Reset
start_reset_button = tk.Button(control_frame, text="Start Game", font=("Arial", 16), command=start_game, bg="#2ecc71", fg="white", relief="solid")
start_reset_button.pack()

# Menjalankan aplikasi
root.mainloop()
