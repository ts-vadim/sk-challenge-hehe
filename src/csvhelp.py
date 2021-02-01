from csv import reader as CsvReader


# Return Data structure:
# {
# 	'column_title_1': [1_row_value, 2_row_value, ...]
# 	'column_title_2': [1_row_value, 2_row_value, ...]
# }
def loadCsv(filename: str, parser_funcs: dict = dict(), no_trace=False):
	def trace(*args, **kwargs):
		if not no_trace:
			print(*args, **kwargs)
	
	data = dict()
	parser_funcs_keys = parser_funcs.keys()
	csvrows_count = 0
	csvcolumns_count = 0
	trace('Loading \"' + filename + '\" CSV file... ', end='', flush=True)
	try:
		with open(filename) as file_in:
			reader = CsvReader(file_in)

			# Save csv data to list
			csvrows = list()
			for row in reader:
				csvrows.append(row)
            
			csvrows_count = len(csvrows)
			csvcolumns_count = len(csvrows[0])

			# Fill dictionary with list values
			for key_i, key in enumerate(csvrows[0]):
				data.update({key: list()})
				key_has_parser = key in parser_funcs_keys
				for value_i in range(1, csvrows_count):
					value = csvrows[value_i][key_i]
					if key_has_parser:
						value = parser_funcs[key](value)
					data[key].append(value)
	except Exception as e:
		trace('failed.\nError: ' + str(e))
		return dict()
	
	trace('done. (' + str(csvcolumns_count * csvrows_count) + ' items)')
	return data
