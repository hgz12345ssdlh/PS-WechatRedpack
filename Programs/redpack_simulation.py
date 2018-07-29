# Packages
import random
import pandas as pd, numpy as np

# Algorithm 1
'''
	STATIC UNIFORM ALGO
	input: size: (Amount, People); num: integer
	return: DataFrame
'''
def redpackAlgo_1(size, num):
	simulation_data = []

	for i in range(num):
		packet = np.array([random.random() for j in range(10)])
		packet /= (sum(packet) / size[0])
		for j in range(len(packet) - 1):
			packet[j] = round(packet[j], 2)
		packet[-1] = size[0] - sum(packet[0:-1])
		simulation_data.append(packet)

	return pd.DataFrame(simulation_data, columns = list('0123456789'))

# Algorithm 2
'''
	DYNAMIC UNIFORM ALGO
	input: size: (Amount, People); num: integer
	return: DataFrame
'''
def redpackAlgo_2(size, num):
	simulation_data = []

	for i in range(num):
		packet = [0]*size[1]
		for pos in range(len(packet) - 1):
			rest_mean = round((100*size[0] - int(100*sum(packet))) / (size[1] - pos))
			rand_amount = round(random.randrange(1, 2*rest_mean) / 100, 2)
			if rand_amount >= size[0] - sum(packet):
				rand_amount = size[0] - sum(packet) - 0.01
			packet[pos] = rand_amount
		packet[-1] = round(size[0] - sum(packet), 2)
		# print(packet)
		# print(sum(packet))
		simulation_data.append(packet)

	return pd.DataFrame(simulation_data, columns = list('0123456789'))

# Data Generating
'''
	input: algo: 'static'/'dynamic'; size: (Amount, People); num: integer
	returns: DataFrame
'''
def redpackGenerate(algo, size, num):
	if algo == 'static':
		return redpackAlgo_1(size, num)
	elif algo == 'dynamic':
		return redpackAlgo_2(size, num)
	else:
		print("Algorithm Choice Error")

# TEST
if __name__ == '__main__':
	import redpack_plot

	# simulation_df = redpackGenerate('static', (10, 10), 200)
	# redpack_plot.plotPosDist(simulation_df)

	simulation_df = redpackGenerate('dynamic', (10, 10), 200)
	redpack_plot.plotPosDist(simulation_df)
