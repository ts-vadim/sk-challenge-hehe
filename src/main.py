import csv
import ast


def loadCsv(filename: str, parser_funcs: dict = dict(), no_trace=False):
	def trace(*args, **kwargs):
		if not no_trace:
			print(*args, **kwargs)
	
	data = list()
	trace('Loading \"' + filename + '\" CSV file...')
	try:
		with open(filename) as file_in:
			# Count lines
			line_count = 0
			for line in file_in:
				line_count += 1
			file_in.seek(0)
			line_count_str = str(line_count)
			parser_funcs_keys = parser_funcs.keys()
			# Create data list
			reader = csv.DictReader(file_in)
			for row_i, row in enumerate(reader):
				tmp = dict()
				for key in row.keys():
					value = row[key]
					if key in parser_funcs_keys:
						value = parser_funcs[key](value)
					tmp.update({key: value})
				data.append(tmp)
				if row_i % 1000 == 0:
					trace(str(row_i), '/', line_count_str, sep='', end='\r')
	except Exception as e:
		trace('failed.')
		trace('Error: ' + str(e))
		return list()
	trace(' ' * (len(line_count_str) * 3) + '\rdone.')
	return data


def parseStringDict(value: str):
	# "{'A', 'B'}" -> "['A', 'B']"
	return ast.literal_eval('[' + value[1:-1] + ']')


def main():
	keyboard_data = loadCsv("../HeadKraken Records/keyboard.csv", {'key': parseStringDict})

	mouse_data = loadCsv(
		"../HeadKraken Records/mouse.csv",
		{
			'mouse_dx': lambda v: float(v),
			'mouse_dy': lambda v: float(v),
			'mouse_scroll': lambda v: int(v)
		}
	)

	mousebuttons_data = loadCsv(
		"../HeadKraken Records/mousekey.csv", {'mouse_key': parseStringDict}
	)


if __name__ == "__main__":
	main()