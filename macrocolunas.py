import pandas as pd

def verify_columns(data, multiindex_relations):
    """
    Verifica a existência das colunas no DataFrame e prepara os dados para o novo DataFrame,
    inserindo NaN para colunas ausentes.

	# Arguments
    data: DataFrame original com colunas planas.
    multiindex_relations: Lista de tuplas, onde cada tupla contém (Tema, Nome da Coluna).

    # Returns
    reordered_data: Dicionário com os dados reorganizados, incluindo colunas ausentes como NaN.
    """

	# INICIANDO O DICT
    reordered_data = {}

	# PERCORRENDO CADA UMA DOS NALORES DA RELAÇÃO DETERMINADA PARA O MULTIINDEX
    for theme, col_name in multiindex_relations:

		# VERIFICANDO SE A COLUNA REALMENTE EXISTE NO DATAFRAME
        if col_name in data.columns:
			# SE EXISTE, MANTÉM OS DADOS DA COLUNA EM ESPECÍFICO
            reordered_data[(theme, col_name)] = data[col_name]
        else:
            print(f"Aviso: A coluna '{col_name}' não existe no DataFrame original. Inserindo valores NaN.")
			# CASO NÃO EXISTA, CRIA A COLUNA COM VALORES NAN
            reordered_data[(theme, col_name)] = pd.Series([pd.NA] * len(data), index=data.index)

    return reordered_data

def create_multiindex(multiindex_relations):
    """
    Cria um MultiIndex para o DataFrame com base nas relações fornecidas.

	# Arguments
    multiindex_relations: Lista de tuplas, cada tupla contendo (Tema, Nome da Coluna).

    # Returns
    Objeto MultiIndex criado a partir das relações fornecidas.
    """
    return pd.MultiIndex.from_tuples(multiindex_relations)

def create_multiindex_dataframe(data, multiindex_relations):
    """
    Cria um DataFrame com MultiIndex nas colunas a partir de um DataFrame com colunas planas,
    utilizando funções auxiliares para verificar a existência de colunas e criar o MultiIndex.

	# Arguments
    data: DataFrame original com colunas planas.
    multiindex_relations: Lista de tuplas, onde cada tupla contém (Tema, Nome da Coluna).

    # Returnss
    df_multi: DataFrame com colunas organizadas em MultiIndex.
    """
    reordered_data = verify_columns(data, multiindex_relations)
    multi_index = create_multiindex(multiindex_relations)
    df_multi = pd.DataFrame(reordered_data, index=data.index, columns=multi_index)
    return df_multi

# Exemplo de uso da função
data = {
    'Coluna1': range(1, 11),
    'Coluna2': range(11, 21),
    'Coluna3': range(21, 31)
}
df = pd.DataFrame(data)

multiindex_relations = [
    ('Tema 1', 'Coluna1'), ('Tema 1', 'Coluna2'), ('Tema 2', 'Coluna3'), ('Tema 1', 'Coluna4')
]

df_multi = create_multiindex_dataframe(df, multiindex_relations)
print(df_multi)
