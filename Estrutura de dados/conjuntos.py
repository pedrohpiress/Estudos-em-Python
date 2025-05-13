# Criando um conjunto
cidades = {'São Paulo', 'Rio de Janeiro', 'Belo Horizonte'}

# Adicionando um elemento
cidades.add('Salvador')

# Removendo um elemento
cidades.remove('Rio de Janeiro')

# União de conjuntos
cidades_sul = {'Curitiba'}
cidades_uniao = cidades.union(cidades_sul)

# Interseção de conjuntos
cidades_comuns = cidades.intersection(cidades_sul)