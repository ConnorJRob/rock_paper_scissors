from app import app
from flask import render_template, request
from models.game import *
from models.player import *
import random

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/', methods=["POST"])
def play_game():
    player_1_name = request.form['player-1']
    player_1_choice = request.form['player-1-choice'].lower()
    player_2_name = request.form['player-2']
    player_2_choice = request.form['player-2-choice'].lower()
    player1 = Player(name=player_1_name, choice=player_1_choice)
    player2 = Player(name=player_2_name, choice=player_2_choice)
    game = Game(player1, player2)
    return render_template('play_game.html', game = game)

@app.route('/play')
def vs_computer():
    return render_template('vs_computer.html')

@app.route('/play', methods=["POST"])
def check_vs_computer():
    player_1_name = "Player"
    player_1_choice = request.form['choice'].lower()
    player_2_name = "Computer"
    computer_choices = ["Rock","Paper","Scissors"]
    player_2_choice = random.choice(computer_choices).lower()
    player1 = Player(name=player_1_name, choice=player_1_choice)
    player2 = Player(name=player_2_name, choice=player_2_choice)
    game = Game(player1, player2)
    return render_template('play_game.html', game = game)


# @app.route('/rock/scissors')
# def rock_vs_scissors():
#     return "Player 1 wins by playing Rock"

# @app.route('/scissors/paper')
# def scissors_vs_paper():
#     return "Player 1 wins by playing Scissors"

# @app.route('/paper/rock')
# def paper_vs_rock():
#     return "Player 1 wins by playing Paper"

# @app.route('/scissors/rock')
# def scissors_vs_rock():
#     return "Player 2 wins by playing Rock"

# @app.route('/paper/scissors')
# def paper_vs_scissors():
#     return "Player 2 wins by playing Scissors"

# @app.route('/rock/paper')
# def rock_vs_paper():
#     return "Player 2 wins by playing Paper"

# @app.route('/rock/rock')
# def rock_vs_rock():
#     return None

# @app.route('/scissors/scissors')
# def scissors_vs_scissors():
#     return None

# @app.route('/paper/paper')
# def paper_vs_paper():
#     return None