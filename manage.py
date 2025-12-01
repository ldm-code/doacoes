from flask import Flask,render_template,request,url_for,redirect,session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from enum import Enum
import re
app=Flask(__name__)
app.secret_key = "minha_chave_super_secreta_123"
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:sua_senha_do_banco_aqui@127.0.0.1/doacoes" 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)
class Usuario(db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=False)
    cpf = db.Column(db.String(22), nullable=False, unique=True)
class Produto(db.Model):
    __tablename__ = 'produtos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    quantidade_doada = db.Column(db.Integer, nullable=False, default=0)
    local_recebimento = db.Column(db.String(100))
    local_entrega = db.Column(db.String(100))
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

Usuario.produtos = db.relationship('Produto', backref='usuario', lazy=True)

class TipoMovimentacao(Enum):
    doacao = 'doacao'
    recebimento = 'recebimento'

class Movimentacao(db.Model):
    __tablename__ = 'movimentacoes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    produto_id = db.Column(db.Integer, db.ForeignKey('produtos.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.Enum(TipoMovimentacao), nullable=False, default=TipoMovimentacao.doacao)
    data = db.Column(db.DateTime, server_default=func.now())
    local_saida = db.Column(db.String(100), nullable=False)
    local_entrega = db.Column(db.String(100), nullable=False)

    produto = db.relationship('Produto', backref='movimentacoes')
    usuario = db.relationship('Usuario', backref='movimentacoes')
with app.app_context():
    db.create_all()
@app.route('/')
def inicio():
          return render_template('usuario.html')
@app.route('/reg', methods=['POST'])
def cadastro():
        nome=request.form.get('nome')
        email=request.form.get('email')
        senha=request.form.get('senha')
        cpf=request.form.get('cpf')
        if not re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf):
                     return 'CPF inválido', 400
       
        else:
         dados=Usuario(nome=nome,email=email,senha=senha,cpf=cpf)
         db.session.add(dados)
         db.session.commit()
         return render_template('login.html')
@app.route('/login',methods=['POST'])
def login():
       email=request.form.get('email').strip()
       senha=request.form.get('senha').strip()
       usuario=Usuario.query.filter_by(email=email,senha=senha).first()
       if usuario:
         session['usuario_id'] = usuario.id 
       
         doacoes=Produto.query.filter(Produto.quantidade>0).all()
         return render_template('inicial.html',produtos=doacoes)
       else:
            return "Email ou senha incorretos", 401
@app.route('/outra_tela')
def outra_tela():
    return render_template('login.html')


@app.route('/view',methods=['GET'])
def doacoes_tela():
      
      return render_template('doar.html')
@app.route('/produto',methods=['POST'])
def cadastrar_doacoes():
      nome=request.form.get('nome')
      tipo=request.form.get('tipo')
      quantidade=int(request.form.get('quantidade'))
      local_recebimento=request.form.get('local_recebimento')
      usuario_id = session.get('usuario_id')
      if not usuario_id:
        return "Usuário não logado", 401
      produto = Produto(
        nome=nome,
        tipo=tipo,
        quantidade=quantidade,
        local_recebimento=local_recebimento,
        usuario_id=usuario_id
      )

      db.session.add(produto)
      db.session.commit()
      doacoes=Produto.query.filter(Produto.quantidade>0).all()
      return render_template('inicial.html',produtos=doacoes) 
@app.route('/receber_doacao/<int:produto_id>', methods=['POST'])
def receber_doacao(produto_id):
    usuario_id = session.get('usuario_id')
    local=request.form.get('local_entrega')
    qtd=int(request.form.get('quantidade_receber'))
   
    if not usuario_id:
        return "Usuário não logado", 401
    
    produto = Produto.query.get_or_404(produto_id)
    produto_real=produto.id
    local_saida=produto.local_recebimento
    if produto.quantidade <= 0:
        return "Doação esgotada!", 400
    

    produto.quantidade -= qtd
    produto.quantidade_doada += qtd
    produto.local_entrega=local
    mov = Movimentacao(
    produto_id=produto_real,    
    usuario_id=usuario_id,   
    quantidade=qtd,             
    tipo=TipoMovimentacao.recebimento,
    local_saida=local_saida,
    local_entrega=local
    )

    db.session.add(mov)

    db.session.commit()
    doacoes=Produto.query.filter(Produto.quantidade>0).all()
    return render_template('inicial.html',produtos=doacoes)
@app.route('/produtos')
def produtos_para_doacao():
    doacoes = Produto.query.filter(Produto.quantidade > 0).all()
    return render_template('inicial.html', produtos=doacoes)

@app.route('/movimentacoes',methods=['GET'])
def movimentacoes():
     movimentacoes=Movimentacao.query.all()
     return render_template('movimentacoes.html',movimentacoes=movimentacoes)
if __name__=='__main__':
        app.run(debug=True)