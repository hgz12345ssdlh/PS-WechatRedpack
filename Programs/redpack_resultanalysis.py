# Packages
import matplotlib.pyplot as plt, seaborn as sns
import numpy as np

# Result Comparing
sns.set_style('darkgrid')

def compareMean(*dfs, names = None):
	'''
		param names: None-no names
		             ('name1', 'name2', ...)-names corresponding to dfs
		compare Uniformity of Mean
	'''
	raw_mean = np.array([])
	for i in range(len(dfs)):
		mean_series = np.array([np.mean(dfs[i][index]) for index in '0123456789'])
		if i == 0: raw_mean = mean_series

		if names == None:
			plt.plot(mean_series)
		else:
			plt.plot(mean_series, label = names[i])
			plt.legend(loc = 'center', frameon = True, framealpha = 0.9)

		plt.xticks(np.arange(0, 10, 1))
		plt.xlabel('Position')
		plt.ylabel('Amount (Yuan)')
		plt.ylim(.0, 1.1)

		if i > 0 and names != None:
			MSE = ((mean_series - raw_mean)**2).mean()
			plt.text(2, 0.4-0.1*i, 'MSE of ' + names[i] + ' = ' + str(round(MSE, 5)))

	plt.show()

def compareVariance(*dfs, names = None):
	'''
		param names: None-no names
		             ('name1', 'name2', ...)-names corresponding to dfs
		compare Variance Regression
	'''
	for i in range(len(dfs)):
		var_series = np.array([np.var(dfs[i][index]) for index in '0123456789'])

		if names == None:
			sns.regplot(x = np.array(range(0, 10)), y = var_series, order = 2)
		else:
			sns.regplot(x = np.array(range(0, 10)), y = var_series, order = 2, label = names[i])
			plt.legend(loc = 'upper center', frameon = True, framealpha = 0.9)

		plt.xticks(np.arange(0, 10, 1))
		plt.xlabel('Position')
		plt.ylabel('Amount (Yuan)')

	plt.show()

def comparePosDist(*dfs, names = None):
	'''
		param names: None-no names
		             ('name1', 'name2', ...)-names corresponding to dfs
		compare Distribution at Positions
	'''
	fig, axes = plt.subplots(5, 2)

	count = 0
	for j in range(2):
		for i in range(5):

			for ind in range(len(dfs)):
				if names == None:
					sns.kdeplot(dfs[ind][str(count)], ax = axes[i,j], shade = True)
				else:
					sns.kdeplot(dfs[ind][str(count)], ax = axes[i,j], shade = True, label = names[ind])
					axes[i,j].legend(loc = 'upper right', frameon = True, framealpha = 0.9, fontsize = 8)

			axes[i,j].set_xlabel('Amount (Yuan)')
			if j == 0:
				axes[i,j].set_ylabel('Frequency')
			axes[i,j].set_xlim(0., 4.)
			axes[i,j].set_ylim(0., .7)
			axes[i,j].set_yticks(np.arange(0, 0.8, 0.2))
			axes[i,j].annotate('Position ' + str(count), xy = (0,0), xytext = (2.5, .1))
			count += 1

	plt.show()

# TEST
if __name__ == '__main__':
	import redpack_datareading
	import redpack_simulation

	raw_df = redpack_datareading.redpackDataFrame(redpack_datareading.read())
	simu_df_static = redpack_simulation.redpackGenerate('static', (10, 10), 184)
	simu_df_dynamic = redpack_simulation.redpackGenerate('dynamic', (10, 10), 184)

	compareMean(raw_df, simu_df_static, simu_df_dynamic, \
				names = ('Raw Data', 'Static-Uniform Algo', 'Dynamic-Updating Algo'))
	compareVariance(raw_df, simu_df_static, simu_df_dynamic, \
				names = ('Raw Data', 'Static-Uniform Algo', 'Dynamic-Updating Algo'))
	comparePosDist(raw_df, simu_df_static, simu_df_dynamic, \
				names = ('Raw', 'Static-Uniform', 'Dynamic-Updating'))