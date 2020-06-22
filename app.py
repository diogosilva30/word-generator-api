#!flask/bin/python
from flask import Flask, jsonify, make_response, url_for
import random

app = Flask(__name__)


words = [
    {
        'id': 1,
        'words': ['porta', 'pé', 'panela', 'copo', 'sapo', 'tapete']
    },
    {
        'id': 2,
        'words': ['banana', 'bicicleta', 'bola', 'cabelo', 'bebê', 'rabo']
    },
    {
        'id': 3,
        'words': ['tênis', 'tesoura', 'tapete', 'presente', 'porta', 'prato']
    },
    {
        'id': 4,
        'words': ['dedo', 'dado', 'dente', 'cadeira', 'escada', 'roda']
    },
    {
        'id': 5,
        'words': ['copo', 'cadeira', 'escada', 'macaco', 'faca']
    },
    {
        'id': 6,
        'words': ['gato', 'garfo', 'galinha', 'língua', 'fogo', 'barriga']
    },
    {
        'id': 7,
        'words': ['faca', 'fogo', 'folha', 'sofá', 'garfo', 'café']
    },
    {
        'id': 8,
        'words': ['vassoura', 'ventilador', 'vaca', 'cavalo', 'avião', 'ovo']
    },
    {
        'id': 9,
        'words': ['sofá', 'sapo', 'sapato', 'bicicleta', 'vassoura', 'coração', 'escada', 'espelho', 'estrela', 'tênis', 'óculos', 'lápis']
    },
    {
        'id': 10,
        'words': ['zebra', 'zero', 'zíper', 'presente', 'tesoura', 'mesa']
    },
    {
        'id': 11,
        'words': ['chinelo', 'chapéu', 'chave', 'bruxa', 'caixa', 'cachorro']
    },
    {
        'id': 12,
        'words': ['jacaré', 'joelho', 'girafa', 'relógio', 'laranja', 'beijo']
    },
    {
        'id': 13,
        'words': ['macaco', 'mão', 'mesa', 'cama', 'caminhão', 'tomate']
    },
    {
        'id': 14,
        'words': ['nariz', 'nuvem', 'navio', 'banana', 'tênis', 'chinelo']
    },
    {
        'id': 15,
        'words': ['caminhão', 'galinha', 'passarinho']
    },
    {
        'id': 16,
        'words': ['língua', 'lápis', 'luva', 'bola', 'cabelo', 'cavalo', 'bolsa', 'calça', 'fralda', 'pastel', 'anel', 'jornal']
    },
    {
        'id': 17,
        'words': ['tesoura', 'cadeira', 'vassoura', 'porta', 'garfo', 'porco', 'colher', 'ventilador', 'flor']
    },
    {
        'id': 18,
        'words': ['joelho', 'coelho', 'colher']
    },
    {
        'id': 19,
        'words': ['rabo', 'roda', 'relógio', 'cachorro', 'barriga', 'terra']
    },
    {
        'id': 20,
        'words': ['presente', 'língua', 'branco', 'trem', 'batom', 'nuvem']
    },

]


@app.route('/api/', methods=['GET'])
def home():
    return '''<h1>Welcome to word generator API. List of phonems:</h1> 
    <p>1 - /p/</p>
    <p>2 - /b/</p>
    <p>3 - /t/</p>
    <p>4 - /d/</p>
    <p>5 - /k/</p>
    <p>6 - /g/</p>
    <p>7 - /t/</p>
    <p>8 - /v/</p>
    <p>9 - /s/</p>
    <p>10 - /z/</p>
    <p>11 - /S/</p>
    <p>12 - /3/</p>
    <p>13 - /m/</p>
    <p>14 - /n/</p>
    <p>15 - /n_mudo/</p>
    <p>16 - /l/</p>
    <p>17 - /r/</p>
    <p>18 - /3/</p>
    <p>19 - /R/</p>
    <p>20 - /N/</p>
    <p> Consultar paper para lista de fonemas e palavras usadas: https://www.scielo.br/pdf/acr/v18n3/a09v18n3.pdf </p>
    Como usar: /api/word/[id]
    Este endpoint irá devolver uma palavra aleatória

    '''


def Convert(lst):
    res_dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    return res_dct


@app.route('/api/word/<int:phonem_id>', methods=['GET'])
def get_word(phonem_id):
    word = [word for word in words if word['id'] == phonem_id]
    return_word = random.choice(word[0]['words'])
    print('Returning word: ' + return_word)
    return jsonify({'status': 'ok', 'word': return_word, 'URI': url_for('get_word', phonem_id=phonem_id, _external=True)})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
