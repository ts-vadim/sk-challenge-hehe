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
		trace('failed. Error: ' + str(e))
		return list()
	trace(' ' * (len(line_count_str) * 3) + '\rdone.')
	return data


def parseStringDict(string: str):
	# "{'A', 'B'}" -> "['A', 'B']"
	return ast.literal_eval('[' + string[1:-1] + ']')


def parseTime(time_string: str):
	# Input: 2021-02-01T17:25:12.284
	date, time_point = time_string.split('T')

	year, month, day = [int(e) for e in date.split('-')]
	hour, minute, sec_ms = [e for e in time_point.split(':')]
	hour = int(hour)
	minute = int(minute)
	second = int(sec_ms.split('.')[0])
	millisecond = int(sec_ms.split('.')[1])

	output = {
		'text': time_string,
		'year': year,
		'month': month,
		'day': day,
		'hour': hour,
		'min': minute,
		'sec': second,
		'ms': millisecond
	}

	return output



def main():
	keyboard_data = loadCsv("../HeadKraken Records/keyboard.csv", {'time': parseTime, 'key': parseStringDict})

	mouse_data = loadCsv(
		"../HeadKraken Records/mouse.csv",
		{
			'time': parseTime,
			'mouse_dx': lambda v: float(v),
			'mouse_dy': lambda v: float(v),
			'mouse_scroll': lambda v: int(v)
		}
	)

	mousebuttons_data = loadCsv(
		"../HeadKraken Records/mousekey.csv", {'tim': parseTime, 'mouse_key': parseStringDict}
	)

	for row in keyboard_data:
		print(row)
		input()


if __name__ == "__main__":
	main()