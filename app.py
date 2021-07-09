from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/<int:id>')
def testApi_Informacoes(id):
    return jsonify({'id': id, 'Nome': 'Maurilio', 'Profissao': 'Desenvolvedor'})


@app.route('/soma/<int:num1>/<int:num2>/')
def soma(num1, num2):
    return jsonify({'soma':num1 + num2})

@app.route('/somaPlus', methods=['POST', 'PUT', 'GET'])
def somaPlus():
    if request.method == 'POST':
        dados = json.loads(request.data)
        total = sum(dados['num'])
    elif request.method == 'GET':
        total = str('TOME PINGUÉLO NA TESTA')
    return jsonify({'somaPlus':total})


if __name__ == '__main__':
    app.run(debug=True)
