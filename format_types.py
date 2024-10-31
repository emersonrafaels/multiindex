import pandas as pd

format_types = {
    'monetary': '$#,##0.00',
    'percentage': '0.00%',
    'date': 'mm/dd/yyyy',
    'integer': '0',
    'float': '0.00',
    'text': '@'  # Texto (impede que números sejam convertidos em numéricos)
}


def apply_format_and_export(df, file_name, column_formats):
	"""
	Exporta um DataFrame para Excel aplicando formatos específicos a colunas selecionadas.

	:param df: DataFrame a ser exportado.
	:param file_name: Nome do arquivo (sem extensão) para salvar os dados.
	:param column_formats: Dicionário onde as chaves são as colunas e os valores são os tipos de formatação do dict 'format_types'.
	"""
	# Criar um escritor do pandas usando xlsxwriter
	writer = pd.ExcelWriter(f"{file_name}.xlsx", engine='xlsxwriter')
	df.to_excel(writer, index=True, sheet_name='Sheet1')

	# Obter o objeto workbook e o objeto worksheet do escritor
	workbook = writer.book
	worksheet = writer.sheets['Sheet1']

	# Aplicar formatações conforme especificado em column_formats
	for col_num, col_name in enumerate(df.columns):
		if col_name in column_formats:
			# Cria um objeto de formato para as células dessa coluna
			format_code = format_types[column_formats[col_name]]
			format_obj = workbook.add_format({'num_format': format_code})
			# Aplica o formato a todas as células da coluna, ajustando para o índice do Excel (col_num + 1 para índice)
			worksheet.set_column(col_num + 1, col_num + 1, None, format_obj)

	# Salvar o arquivo
	writer.save()
	print(f"DataFrame exportado e formatado com sucesso para {file_name}.xlsx")


# Exemplo de uso
data = {
	'Revenue': [1000, 1500, 800, 1200],
	'Discount': [0.1, 0.15, 0.2, 0.05],
	'Sale Date': pd.to_datetime(
		['2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01'])
}
df = pd.DataFrame(data)

# Formatos desejados para as colunas
column_formats = {
	'Revenue': 'monetary',
	'Discount': 'percentage',
	'Sale Date': 'date'
}

apply_format_and_export(df, 'sales_report', column_formats)
