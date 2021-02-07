import json


def dumpData(filename: str, data: dict):
    print('Dumping data to \"' + filename + '\"... ', end='')
    json_len = 0
    try:
        json_string = json.dumps(data, sort_keys=True, indent=4)
        json_len = len(json_string)

        with open(filename, 'w') as out_file:
            out_file.write(json_string)
    except Exception as e:
        print('failed. Error: ' + str(e))
        return
    print('done. (Wrote ' + str(json_len) + ' chars)')
