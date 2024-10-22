from crypt import methods

from flask import Flask, render_template, request, redirect, session, flash, url_for
from classes.class_jogo import Jogo
from classes.class_usuario import Usuario

app = Flask(__name__)
app.secret_key = 'fani'

user1 = Usuario('Ayron','yrin', '1234')
user2 = Usuario('Carlinhos', 'Dalva', 'adalvabebe')
user3 = Usuario('Luan', 'LuanGameplay', 'ronaldinho')

users = {   user1.nick : user1,
            user2.nick : user2,
            user3.nick : user3
         }

game1 = Jogo('God Of War', "Action", "Playstation")
game2 = Jogo('Pokemon Emerald', 'Turn', 'Nintendo GameBoy Advanced')
game_list = [game1, game2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=game_list)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login',proxima=url_for('novo') ) )
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',]) #methods['POST'] allow the method POST to this route
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    game_list.append(jogo)

    return redirect(url_for('index')) # redirected to the choose path


@app.route('/login')
def login():
    proxima = request.args.get('proxima') # /login?proxima=pagina
    return render_template('login.html', proxima=proxima)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['usuario'] in users:
        user = users[request.form['usuario']]
        if request.form['senha'] == user.senha:
            session['usuario_logado'] = user.nick
            flash(user.nick + ' logado com sucesso!')
            proxima_pag = request.form['proxima']
            return redirect(proxima_pag)
    else:
        flash('Usuario não logado!')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index')) # funcao que instancia a rota como argumento

app.run(host='0.0.0.0', port=8080, debug=True)
