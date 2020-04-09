from api import ma
from ..models import tarefa_model
from marshmallow import fields


class TarefaSchema(ma.ModelSchema):
    class Meta:
        model = tarefa_model.Tarefa
        fields = ("id", "titulo", "descricao", "dt_expiracao")

    titulo = fields.String(required=True)
    descricao = fields.String(required=True)
    dt_expiracao = fields.String(required=True)
