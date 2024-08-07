import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import joblib

# Carregar o conjunto de dados
data = pd.read_csv("../Data/database.csv")

# Configuração para evitar notação científica
pd.set_option('display.float_format', '{:.2f}'.format)

# Verificar se há valores negativos ou zero na coluna "PRECO" antes de prosseguir
data = data[data["PRECO"] > 0]

# Dividir o conjunto de dados em features e target
X = data.drop("PRECO", axis=1)
y = data["PRECO"]

# Codificar variáveis categóricas usando One-Hot Encoding
categorical_cols = ["MARCA", "MODELO", "TRANSMISSAO", "TP_COMBUSTIVEL"]
numerical_cols = ["ANO", "QUILOMETRAGEM", "MOTO_SIZE"]

# Criação do Pipeline para pré-processamento
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
    ]
)

# Criação do Pipeline do Modelo
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', DecisionTreeRegressor())
])

# Dividir os dados em conjuntos de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model.fit(X_train, y_train)

# Salvar o modelo treinado
joblib.dump(model, 'modelo_previsao_precos.pkl')

# Fazer previsões no conjunto de teste
y_pred_train = model.predict(X_train)
y_pred_test = model.predict(X_test)

# Avaliar as métricas de desempenho do modelo
mse = mean_squared_error(y_test, y_pred_test)
mae = mean_absolute_error(y_test, y_pred_test)
r2 = r2_score(y_test, y_pred_test)

print("Mean Squared Error (MSE):", mse)
print("Mean Absolute Error (MAE):", mae)
print("R-squared (R2):", r2)