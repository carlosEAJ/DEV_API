from flask import Flask
from flask import jsonify
import json
from flask import request

app = Flask(__name__)

desenvolvedores = [
    {
        'id': 0,
        'nome':'Rafael', 'habilidades':['Python', 'Flask']},
    {
    'id': 1,
    'nome': 'Galleani', 'habilidades':['Python', 'Django']},
]

#"dev" GET, recuperando todos os desenvolvedores
#"dev" PUT, atualiza desenvolvedor ou altera
#"dev" DELETE, exclui desenvolvedor
# devolve um desenvolvedor pelo id
@app.route('/dev/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = 'Desenvolvedor de ID {} não existe'.format(id)
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = 'Erro desconhecido. Procure o administrador da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    #id se torna a posição do desenvolvedor no array desenvolvedores.
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status':'sucesso', 'mensagem':'registro excluido'})

#lista todos os desenvolvedores e permite registrar novos desenvolvedores
@app.route('/dev', methods=['POST', 'GET'])  
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)
    

if __name__ == '__main__':
    app.run(debug=True)