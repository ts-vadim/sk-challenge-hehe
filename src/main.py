from csvhelp import *
from util import *
from statistics import *


def main():
	keyboard_csv = loadCsv(
		'../HeadKraken Records/keyboard.csv',
		{
			'time': parseTimeMillis,
			'key': parseStringDict
		}
	)
	mouse_csv = loadCsv(
		'../HeadKraken Records/mouse.csv',
		{
			'time': parseTimeMillis,
			'mouse_dx': lambda v: int(v),
			'mouse_dy': lambda v: int(v),
			'mouse_scroll': lambda v: int(v)
		}
	)
	mousekeys_csv = loadCsv(
		'../HeadKraken Records/mousekey.csv',
		{
			'time': parseTimeMillis,
			'mouse_key': parseStringDict
		}
	)

	key_data = processKeyData(keyboard_csv, 'key')
	mousekey_data = processKeyData(mousekeys_csv, 'mouse_key')
	
	print('Keyboard data:')
	for key, value in key_data.items():
		print('\"' + key + '\":', value, end='')
		input()
	
	print('Mouse key data:')
	for key, value in mousekey_data.items():
		print('\"' + key + '\":', value, end='')
		input()



if __name__ == "__main__":
	main()