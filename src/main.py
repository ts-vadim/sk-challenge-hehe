from csvhelp import loadCsv
from util import profileFunction, parseStringDict


def main():
	key_data = loadCsv('../HeadKraken Records/keyboard.csv', {'key': parseStringDict})
	mouse_date = loadCsv(
		'../HeadKraken Records/mouse.csv',
		{
			'mouse_dx': lambda v: int(v),
			'mouse_dy': lambda v: int(v),
			'time,mouse_dx,mouse_dy,mouse_scroll': lambda v: int(v)
		}
	)

	for key in key_data.keys():
		print('Key:', key, 'values:', len(key_data[key]))


if __name__ == "__main__":
	main()