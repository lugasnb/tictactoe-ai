from flask import Flask, jsonify, render_template, request
from game_logic import GameLogic

app = Flask(__name__)
game = GameLogic()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/make_move", methods=["POST"])
def make_move():
    position = int(request.json["position"])
    game.make_move(position)
    return jsonify({
        "board": game.board,
        "game_over": game.game_over,
        "winner": game.winner
    })

@app.route("/reset", methods=["POST"])
def reset_game():
    game.reset_game()
    return jsonify({"board": game.board})

