# Criando um dicionário
aluno = {'nome': 'João', 'idade': 20, 'curso': 'Engenharia'}

# Acessando valores
print(aluno['nome'])  # Output: João

# Adicionando ou atualizando elementos
aluno['idade'] = 21

# Removendo elementos
del aluno['curso']

aluno['sobrenome'] = 'Pires'

# Iterando sobre dicionários
for chave, valor in aluno.items():
    print(f'{chave}: {valor}')