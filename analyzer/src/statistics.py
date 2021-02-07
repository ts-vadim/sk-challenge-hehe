

def processKeyData(csv_load: dict, button_column_name: str, no_trace=False):
	def trace(*args, **kwargs):
		if not no_trace:
			print(*args, **kwargs)

	# {'A': {'pressed': False, 'clicks': 0, 'start': 0, 'total': 0}}
	key_data = dict()
	records_count = 0

	trace('Processing \"' + button_column_name + '\" data... ', end='')
	try:
		records_count = len(csv_load[button_column_name])
		for time, active_buttons in zip(csv_load['time'], csv_load[button_column_name]):
			# Process all active keys
			for button in active_buttons:
				# Add new button statistic if its not present
				if button not in key_data.keys():
					key_data.update({button: {'pressed': True, 'clicks': 0, 'start': time, 'total': 0}})
				else:
					# if wasn't pressed save the time point
					if not key_data[button]['pressed']:
						key_data[button]['pressed'] = True
						key_data[button]['start'] = time
			# Process all disabled keys that was pressed
			disabled_buttons = [
				btn for btn in key_data.keys()
				if key_data[btn]['pressed'] and btn not in active_buttons
			]
			for button in disabled_buttons:
				key_data[button]['total'] += time - key_data[button]['start']
				key_data[button]['start'] = 0
				key_data[button]['clicks'] += 1
				key_data[button]['pressed'] = False
	except Exception as e:
		trace('failed. Error: ' + str(e))
		return dict()
	
	trace('done. (' + str(records_count) + ' records)')
	return key_data
