from flask import Flask, jsonify, request
import json
app = Flask(__name__)

listaDesenvolvedores = [
    {'ID':'0', 'NOME':'Maurilio', 'HABILIDADES': ['Python', 'Flask']},
    {'ID':'1', 'NOME':'Rafael', 'HABILIDADES': ['Java', 'Maven']},
    {'ID':'2', 'NOME':'Joanilson', 'HABILIDADES':['PHP','Django']}
]

@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def Consulta_Deleta_Desenvolvedor(id):
    if request.method == 'GET':
        try:
            desenvolvedor = listaDesenvolvedores[id]
            print(desenvolvedor)
        except IndexError:
            desenvolvedor = {'STATUS':'Erro!', 'MENSAGEM':'Registro inexistente!'}
        except Exception:
            desenvolvedor = {'STATUS':'Erro!', 'MENSAGEM':'Erro desconhecido'}
        return jsonify(desenvolvedor)

    elif request.method == 'PUT':
        dados = json.loads(request.data)
        listaDesenvolvedores[id] = dados
        return jsonify(dados)

    elif request.method == 'DELETE':
        listaDesenvolvedores.pop(id)
        return jsonify({'STATUS':'Sucesso!', 'MENSAGEM':'Registro excluído!'})

@app.route('/dev/', methods=['POST', 'GET'])
def Insere_Lista_Desenvolvedor():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(listaDesenvolvedores)
        dados['ID'] = posicao
        listaDesenvolvedores.append(dados)
        return jsonify(listaDesenvolvedores[posicao])

    elif request.method == 'GET':
        return jsonify(listaDesenvolvedores)

if __name__ == '__main__':
    app.run(debug=True)