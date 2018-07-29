# Packages
import xlrd # Excel IO
import pandas as pd

# Data Reading
'''
	redpack_data = [{'size': (Amount, People), 'data': [list of data]}, {...}, ...]
'''
def read():
	redpack_datafile = xlrd.open_workbook('red packet data.xlsx')
	redpack_datatable = redpack_datafile.sheets()[0]
	redpack_data = []
	for i in range(2, redpack_datatable.nrows):
		raw_row = redpack_datatable.row_values(i)
		row = [num for num in raw_row[1:] if num != '']
		if len(row) > 0:
			redpack_data.append({'size': (round(row[0], 2), int(row[1])), 'data': row[2:]})
	return redpack_data

# Data Processing
'''
	redpack_df: DataFrame
		Every row is a packet;
		Column number corresponds to sequences
'''
def redpackDataFrame(redpack_data):
	redpack_df = pd.DataFrame([packet['data'] for packet in redpack_data if packet['size'] == (10, 10)], columns = list('0123456789'))
	return redpack_df

# TEST
if __name__ == '__main__':
	redpack_data = read()
	# for packet in redpack_data:
	# 	print(packet)
	redpack_df = redpackDataFrame(redpack_data)
	print(redpack_df)