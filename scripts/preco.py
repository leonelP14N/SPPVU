# Instalar os pacotes necessários no Python, se ainda não estiverem instalados
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
#from category_encoders import CatBoostEncoder
from sklearn import tree
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

# Carregar o conjunto de dados
data = pd.read_csv("../../Data/database.csv")

# Configuração para evitar notação científica
pd.set_option('display.float_format', '{:.2f}'.format)

data =data.drop("Unnamed: 0", axis= 1)

# Supondo que 'data' seja o DataFrame com os dados
# data = pd.read_csv('path_to_your_dataset.csv')  # Substitua pelo caminho correto para o seu arquivo de dados

# Verificar se há valores negativos ou zero na coluna "PRECO" antes de prosseguir
data = data[data["PRECO"] > 0]

# Dividir o conjunto de dados em features e target
X = data.drop("PRECO", axis=1)
y = data["PRECO"]

# Codificar variáveis categóricas usando One-Hot Encoding
categorical_cols = ["MARCA", "MODELO", "TRANSMISSAO", "TP_COMBUSTIVEL"]
ct = ColumnTransformer(
    [("one_hot_encoder", OneHotEncoder(handle_unknown='ignore'), categorical_cols)], remainder="passthrough"
)
X_encoded = ct.fit_transform(X)

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Treinar o modelo de árvore de decisão
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# Fazer previsões no conjunto de teste
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Avaliar as métricas de desempenho do modelo
accuracy = metrics.accuracy_score(y_test, y_pred_test)
precision = metrics.precision_score(y_test, y_pred_test, average="macro")
recall = metrics.recall_score(y_test, y_pred_test, average="macro")


print("Acurácia:", accuracy)
print("Precisão:", precision)
print("Recall:", recall)

#características do carro:
caracteristicas_carro = {
    "MARCA": ["TOYOTA"],
    "MODELO": ["PRADO TXL"],
    "TRANSMISSAO": ["AUTOMATICO"],
    "TP_COMBUSTIVEL": ["Gasolina"],
    "ANO": [2020],
    "QUILOMETRAGEM": [60215],  # Exemplo de quilometragem
    "MOTO_SIZE": [4.2],  # Exemplo de Cc
}

#DataFrame com as características do carro
df_carro = pd.DataFrame(caracteristicas_carro)

X_carro_encoded = ct.transform(df_carro)

#prever o preço usando o modelo treinado
previsao_preco = model.predict(X_carro_encoded)

previsao_preco_df = pd.DataFrame(previsao_preco, columns=['previsao_preco'])

database = pd.concat([df_carro, previsao_preco_df], axis=1)


#resultado da previsão
print(f"O preço previsto para o seu carro é: {previsao_preco[0]:.2f} KZ")