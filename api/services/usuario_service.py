from ..models import usuario_model
from api import db

def cadastrar_usuario(usuario):
    usuario_bd = usuario_model.Usuario(nome=usuario.nome, email=usuario.email, senha=usuario.senha)
    usuario_bd.gen_senha()
    db.session.add(usuario_bd)
    db.session.commit()
    return usuario_bd

def listar_usuario_email(email):
    usuario = usuario_model.Usuario.query.filter_by(email=email).first()
    return usuario

def listar_usuario_id(id):
    usuario = usuario_model.Usuario.query.filter_by(id=id).first()
    return usuario

def editar_usuario(usuario_bd, usuario_novo):
    usuario_bd.nome = usuario_novo.nome
    usuario_bd.email = usuario_novo.email
    usuario_bd.senha = usuario_novo.senha
    usuario_bd.gen_senha()
    db.session.commit()

def remover_usuario(usuario):
    db.session.delete(usuario)
    db.session.commit()