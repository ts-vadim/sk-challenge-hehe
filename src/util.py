from time import time
from json import loads


def profileFunction(func, *args, **kwargs):
	start_time = time()
	return_value = func(*args, **kwargs)
	end_time = time()
	print('Function \"' + func.__name__ + '()\" Profile: ' + str(round(end_time - start_time, 4)) + 'sec')
	return return_value


def parseStringDict(string: str):
	# {'A', 'B'} -> ["A", "B"]
	return loads('[' + string[1:-1].replace('\'', '\"') + ']')


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