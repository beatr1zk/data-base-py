from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.crud.create import Usuario
from repositories import rep_usuario, rep_restaurante, rep_avaliacao, rep_cardapio

app = Flask(__name__)
app.secret_key = 'batata'

def login_required(funcao):
    @wraps(funcao)
    def verificar(*args, **kwargs):
        if 'id_usuario' not in session:
            return redirect(url_for('login'))
        else:
            return(*args, *kwargs)
    return verificar

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha_hash = generate_password_hash(request.form['senha'])
        if rep_usuario.buscar_por_email(email) is not None:
            return render_template('cadastro.html', erro='Este e-mail já está cadastrado.')
        else:
            usuario = Usuario(nome, email, senha_hash)
            rep_usuario.criar_usuario(usuario)
            return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request['email']
        senha = request['senha']

        usuario = rep_usuario.buscar_por_email(email)
        if usuario and check_password_hash(usuario._senha_hash, senha):
            session['usuario_id'] = usuario.id_usuario
            return redirect(url_for('painel'))
        else:
            return render_template('login.html', erro='E-mail ou senha inválidos.')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('id_usuario', None)
    return redirect(url_for('login'))

@app.route('/painel')
@login_required
def painel():
    usuario = rep_usuario.buscar_por_email(session['usuario_id'])
    return render_template('painel.html', usuario=usuario)

@app.route ('/restaurantes')
@login_required
def restaurantes():
    lista_restaurantes = rep_restaurante.listar_restaurantes()
    return render_template('restaurante.html', restaurantes=lista_restaurantes)

if __name__ == '__main__':
    rep_restaurante.tabela_restaurante()
    rep_avaliacao.tabela_avaliacoes()
    rep_cardapio.tabela_item_cardapio()
    rep_usuario.tabela_usuario()