from csvhelp import loadCsv
from util import profileFunction, parseStringDict


def main():
	key_data = loadCsv('../HeadKraken Records/keyboard.csv', {'key': parseStringDict})

	for key in key_data.keys():
		print('Key:', key, 'values:', len(key_data[key]))


if __name__ == "__main__":
	main()