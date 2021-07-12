import json

from flask import Flask, request
from flask_restful import Resource, Api
from app_restful_01_dev_habilidades import Dev_Habilidades

app = Flask(__name__)
api = Api(app)
listaDesenvolvedores = [
    {'ID': '0', 'NOME': 'Maurilio', 'HABILIDADES': ['Python', 'Flask']},
    {'ID': '1', 'NOME': 'Rafael', 'HABILIDADES': ['Java', 'Maven']},
    {'ID': '2', 'NOME': 'Joanilson', 'HABILIDADES': ['PHP', 'Django']}
]


class Desenvolvedor(Resource):
    def get(self, id):
        try:
            desenvolvedor = listaDesenvolvedores[id]
            print(desenvolvedor)
        except IndexError:
            desenvolvedor = {'STATUS': 'Erro!', 'MENSAGEM': 'Registro inexistente!'}
        except Exception:
            desenvolvedor = {'STATUS': 'Erro!', 'MENSAGEM': 'Erro desconhecido'}
        return desenvolvedor

    def put(self, id):
        dados = json.loads(request.data)
        listaDesenvolvedores[id] = dados
        return dados

    def delete(self, id):
        listaDesenvolvedores.pop(id)
        return {'STATUS': 'Sucesso!', 'MENSAGEM': 'Registro excluído!'}


class Insere_Lista_Desenvolvedor(Resource):
    def get(self):
        return listaDesenvolvedores

    def post(self):
        dados = json.loads(request.data)
        posicao = len(listaDesenvolvedores)
        dados['ID'] = posicao
        listaDesenvolvedores.append(dados)
        return listaDesenvolvedores[posicao]


api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Insere_Lista_Desenvolvedor, '/dev/')
api.add_resource(Dev_Habilidades, '/dev_habilidades/')

if __name__ == '__main__':
    app.run(debug=True)
