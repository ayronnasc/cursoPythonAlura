from crypt import methods

from flask import Flask, render_template, request, redirect
from classes.class_jogo import Jogo

app = Flask(__name__)

game1 = Jogo('God Of War', "Action", "Playstation")
game2 = Jogo('Pokemon Emerald', 'Turn', 'Nintendo GameBoy Advanced')
game_list = [game1, game2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=game_list)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',]) #methods['POST'] allow the method POST to this route
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    game_list.append(jogo)

    return redirect('/') # redirected to the choose path

app.run(host='0.0.0.0', port=8080, debug=True)
