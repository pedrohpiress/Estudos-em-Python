# Lista de números com duplicatas
numeros = [1, 2, 3, 4, 1, 2, 5, 6, 7, 8, 9, 7, 10]

# Converter para conjunto para remover duplicatas
numeros_unicos = set(numeros)

# Converter de volta para lista
numeros_sem_duplicatas = list(numeros_unicos)

# Ou simplesmente:
# numeros_sem_duplicatas = list(set(numeros))

# Exibir resultado
print(numeros_sem_duplicatas)