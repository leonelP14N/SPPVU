from flask import Flask, request, jsonify
import joblib
import pandas as pd
from flasgger import Swagger, swag_from
from pymongo import MongoClient

# Criar a aplicação Flask
app = Flask(__name__)
swagger = Swagger(app)

# Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['previsoes_db']
previsoes_collection = db['previsoes']

# Carregar o modelo treinado
model = joblib.load('scripts/modelo_previsao_precos.pkl')

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
        '200': {
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
    previsao_documento = {
        "marca": dados['marca'],
        "modelo": dados['modelo'],
        "transmissao": dados['transmissao'],
        "combustivel": dados['combustivel'],
        "ano": dados['ano'],
        "quilometragem": dados['quilometragem'],
        "moto_size": dados['moto_size'],
        "preco_previsto": float(previsao_preco[0])
    }
    
    previsoes_collection.insert_one(previsao_documento)

    # Retornar a previsão como JSON
    resposta = {'preco_previsto': float(previsao_preco[0])}
    return jsonify(resposta)

@app.route('/docs')
def docs():
    return jsonify({'url': '/apidocs'})

if __name__ == '__main__':
    app.run(debug=True)
