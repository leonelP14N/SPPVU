from flask import Flask, request, jsonify
import sqlite3
import joblib
import pandas as pd
from flasgger import Swagger, swag_from

# Criar a aplicação Flask
app = Flask(__name__)
Swagger = Swagger(app)

# Carregar o modelo treinado
model = joblib.load('scripts/modelo_previsao_precos.pkl')

# Função para inicializar o banco de dados
def init_db():
    conn = sqlite3.connect('previsoes.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS previsoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            marca TEXT,
            modelo TEXT,
            transmissao TEXT,
            combustivel TEXT,
            ano INTEGER,
            quilometragem INTEGER,
            moto_size REAL,
            preco_previsto REAL
        )
    ''')
    conn.commit()
    conn.close()

# Inicializar o banco de dados
init_db()

@app.route('/prever_preco', methods=['POST'])
@swag_from({
    'tags': ['Previsão de Preços'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'marca': {'type': 'string'},
                    'modelo': {'type': 'string'},
                    'transmissao': {'type': 'string'},
                    'combustivel': {'type': 'string'},
                    'ano': {'type': 'integer'},
                    'quilometragem': {'type': 'integer'},
                    'moto_size': {'type': 'integer'}
                    },
                    'required': ['marca', 'modelo', 'transmissao', 'combustivel', 'ano', 'quilometragem', 'moto_size']
                }
        }
    ],
    'responses': {
        '200':{
            'description': 'Previsão de Preço do carro',
            'schema': {
                'type': 'object',
                'properties': {
                    'preco_previsto': {'type': 'float'},
                }
            }
        }
    }
})
def prever_preco():
    dados = request.json
    caracteristicas_carro = {
        "MARCA": [dados['marca']],
        "MODELO": [dados['modelo']],
        "TRANSMISSAO": [dados['transmissao']],
        "TP_COMBUSTIVEL": [dados['combustivel']],
        "ANO": [dados['ano']],
        "QUILOMETRAGEM": [dados['quilometragem']],
        "MOTO_SIZE": [dados['moto_size']]
    }

    # Criar DataFrame com as características do carro
    df_carro = pd.DataFrame(caracteristicas_carro)

    # Prever o preço usando o modelo treinado
    previsao_preco = model.predict(df_carro)

    # Armazenar as características e o preço previsto no banco de dados
    conn = sqlite3.connect('previsoes.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO previsoes (marca, modelo, transmissao, combustivel, ano, quilometragem, moto_size, preco_previsto)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (dados['marca'], dados['modelo'], dados['transmissao'], dados['combustivel'], dados['ano'], dados['quilometragem'], dados['moto_size'], float(previsao_preco[0])))
    conn.commit()
    conn.close()

    # Retornar a previsão como JSON
    resposta = {'preco_previsto': float(previsao_preco[0])}
    return jsonify(resposta)

@app.route('/docs')
def docs():
    return jsonify({'url': '/apidocs'})

if __name__ == '__main__':
    app.run(debug=True)
