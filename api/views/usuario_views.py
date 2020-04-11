from flask_restful import Resource
from api import api
from ..schemas import usuario_schema
from flask import request, make_response, jsonify
from ..entidades import usuario
from ..services import usuario_service
from ..pagination import paginate
from ..models.usuario_model import Usuario
from flask_jwt_extended import jwt_required

class UsuarioList(Resource):
    @jwt_required
    def get(self):
        #usuarios = usuario_service.listar_usuarios()
        us = usuario_schema.UsuarioSchema(many=True)
        return paginate(Usuario, us)

    # Para criar usuario não deve ter token de autenticação
    def post(self):
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]
            usuario_novo = usuario.Usuario(nome=nome, email=email, senha=senha)
            result = usuario_service.cadastrar_usuario(usuario_novo)
            return make_response(us.jsonify(result), 201)


class UsuarioDetail(Resource):
    @jwt_required
    def get(self, id):
        usuario = usuario_service.listar_usuario_id(id)
        if usuario is None:
            return make_response(jsonify("Usuario não encontrado"), 404)
        us = usuario_schema.UsuarioSchema()
        return make_response(us.jsonify(usuario), 200)

    @jwt_required
    def put(self, id):
        usuario_bd = usuario_service.listar_usuario_id(id)
        if usuario_bd is None:
            return make_response(jsonify("Usuario não encontrado"), 404)
        us = usuario_schema.UsuarioSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            senha = request.json["senha"]
            usuario_novo = usuario.Usuario(nome=nome, email=email, senha=senha)
            usuario_service.editar_usuario(usuario_bd, usuario_novo)
            usuario_atualizado = usuario_service.listar_usuario_id(id)
            return make_response(us.jsonify(usuario_atualizado), 200)

    @jwt_required
    def delete(self, id):
        usuario = usuario_service.listar_usuario_id(id)
        if usuario is None:
            return make_response(jsonify("Usuario não encontrado"), 404)
        usuario_service.remover_usuario(usuario)
        return make_response('', 204)


api.add_resource(UsuarioList, '/usuarios')
api.add_resource(UsuarioDetail, '/usuarios/<int:id>')
