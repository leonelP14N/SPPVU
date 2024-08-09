from flask import Flask, request, jsonify
import joblib
import pandas as pd

# Criar a aplicação Flask
app = Flask(__name__)

# Carregar o modelo treinado
model = joblib.load('modelo_previsao_precos.pkl')

@app.route('/prever_preco', methods=['POST'])
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

    # Retornar a previsão como JSON
    resposta = {'preco_previsto': float(previsao_preco[0])}
    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
