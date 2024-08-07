# Solicita ao usuário uma lista de números separados por vírgula e os converte para ponto flutuante
numeros = list(map(float, input().split(',')))

# Define a função para calcular a mediana de uma lista de números
def calcular_mediana(numeros):
    # Ordena a lista de números em ordem crescente
    numeros_ordenados = sorted(numeros)
    # Obtém o comprimento da lista ordenada
    n = len(numeros_ordenados)
    # Calcula o ponto médio da lista
    ponto_medio = n // 2
    def mediana_par(lst):
        mid_index = len(lst) // 2
        return (lst[mid_index - 1] + lst[mid_index]) / 2
    # TODO: Verifique se a quantidade de números é ímpar
    if n % 2 != 0:
      #retorna o valor no meio da lista
      return numeros[ponto_medio]
    else:
      #retorna a média dos dois valores do meio da lista
      return mediana_par(numeros_ordenados)
    
# Chama a função calcular_mediana com a lista de números como argumento e imprime o resultado
print(calcular_mediana(numeros))