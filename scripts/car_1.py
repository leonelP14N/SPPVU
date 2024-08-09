import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from PIL import Image

# Passo 1: Carregar e limpar o dataset
dataset = pd.read_csv('dados_carros.csv')  # Substitua 'dados_carros.csv' pelo nome do seu arquivo CSV
dataset.dropna(inplace=True)  # Remover linhas com valores ausentes

# Passo 2: Extração de Recursos
X = dataset[['marca', 'modelo', 'ano', 'kilometragem', 'combustivel', 'amolgamentos']]  # Selecionar recursos
y = dataset['preco']  # Selecionar alvo

# Passo 3: Dividir o conjunto de dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Passo 4: Treinar o modelo
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Passo 5: Prever preços
def prever_preco(marca, modelo, ano, kilometragem, combustivel, amolgamentos, imagens):
    features = [[marca, modelo, ano, kilometragem, combustivel, amolgamentos]]
    predicted_price = model.predict(features)[0]
    # Processar imagens e considerar influência nos preços
    for imagem in imagens:
        img = Image.open(imagem)
        # Realizar processamento da imagem e considerar influência no preço
        # Atualizar o preço previsto com base no processamento da imagem, se necessário
    return predicted_price

# Exemplo de uso
predicted_price = prever_preco('Toyota', 'Corolla', 2018, 50000, 'Gasolina', 'Sem amolgamentos', ['frente.jpg', 'lado.jpg', 'tras.jpg'])
print('Preço previsto:', predicted_price)
