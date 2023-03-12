from flask import Flask, flash , render_template, request, redirect, url_for,session

class Jogo:
    def __init__(self,nome,categoria,console):
         self.nome=nome
         self.categoria=categoria
         self.console=console

jogo1=Jogo("Tetris" , "Puzzle", "Atari")
jogo2=Jogo("God of War" , " Rack n Slash" , "PS2")
lista = [jogo1,jogo2]

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

usuario1 = Usuario("Bruno Divino", "BD@gmail.com", "alohomora")
usuario2 = Usuario("Camila Ferreira", "Mila@gmail.com", "paozinho")
usuario3 = Usuario("Guilherme Louro", "Cake@gmail.com", "Python_eh_vida")

usuarios = { usuario1.email : usuario1,
             usuario2.email : usuario2,
             usuario3.email : usuario3 }

app = Flask(__name__)
app.secret_key ='admin'
   

@app.route('/')
def index():
    return render_template('lista.html',titulo="Jogos",jogos=lista)

@app.route('/novo')
def novo():
    if session['usuario_logado']:
        return render_template('novo.html', titulo ="Registre um jogo: ")
        
    else:    
          return redirect(url_for('novo'))

@app.route('/criar' , methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return redirect(url_for('index'))

@app.route('/login')
def login():
    if session['usuario_logado']:
        return redirect(url_for('novo'))
    else:    
     return render_template('login.html')

@app.route('/autenticar' , methods = ['POST' ,] )
def autenticar():
 if request.form['Email'] in usuarios:
        usuario = usuarios[request.form['Email']]
        if request.form['inputPassword'] == usuario.senha:
            session['usuario_logado'] = usuario.email
            flash(usuario.email + ' logado com sucesso!')
            return redirect(url_for('novo'))

 else:
    flash('Usuário não logado!')
    return redirect(url_for('login'))
       
@app.route('/logout')
def logout():
    if session['usuario_logado']:
        session['usuario_logado'] = None 
        flash("Logout efetuado com sucesso!")
    else:
        flash('Não há usuários para deslogar nesta sessão! ')    

    return redirect(url_for('index'))     


app.run(debug=True)