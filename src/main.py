from csvhelp import *
from util import *


def main():
	print('No parsers:')
	keyboard_data = profileFunction(
		loadCsv,
		"../HeadKraken Records/keyboard.csv"
	)

	print('\nparseTime():')
	keyboard_data = profileFunction(
		loadCsv,
		"../HeadKraken Records/keyboard.csv",
		{'time': parseTime}
	)

	print('\nparseStringDict():')
	keyboard_data = profileFunction(
		loadCsv,
		"../HeadKraken Records/keyboard.csv",
		{'key': parseStringDict}
	)

	print('\nBoth:')
	keyboard_data = profileFunction(
		loadCsv,
		"../HeadKraken Records/keyboard.csv",
		{'time': parseTime, 'key': parseStringDict}
	)


if __name__ == "__main__":
	main()