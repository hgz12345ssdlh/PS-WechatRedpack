# Packages
import matplotlib.pyplot as plt, seaborn as sns
import numpy as np

# Plotting
sns.set_style('darkgrid')

def plotMeanVariance(redpack_df):
	'''
		Mean & Variance along positions
	'''
	fig, (ax1, ax2) = plt.subplots(1, 2)

	sns.barplot(ax = ax1, data = redpack_df)
	ax1.set_title('Mean')
	ax1.set_xlabel('Position Order')
	ax1.set_ylabel('Amount (Yuan)')

	sns.barplot(ax = ax2, data = redpack_df, estimator = np.var)
	ax2.set_title('Variance')
	ax2.set_xlabel('Position Order')

	plt.show()

def plotPosDist(redpack_df, pos = None):
	'''
		param pos: None-plot distribution at all 10 positions
		           integer-plot distribution at certain position
	'''
	if pos == None:
		fig, axes = plt.subplots(5, 2)

		count = 0
		for j in range(2):
			for i in range(5):
				sns.distplot(redpack_df[str(count)], ax = axes[i,j])
				axes[i,j].set_xlabel('Amount (Yuan)')
				if j == 0:
					axes[i,j].set_ylabel('Frequency')
				axes[i,j].set_xlim(0., 4.)
				axes[i,j].set_ylim(0., .7)
				axes[i,j].set_yticks(np.arange(0, 0.8, 0.2))
				axes[i,j].annotate('Position ' + str(count), xy = (0,0), xytext = (2.5, .4))
				count += 1

	elif not 0 <= pos <= 9:
		print("Pos Error!")
	
	else:
		ax = sns.distplot(redpack_df[str(pos)])
		ax.set_xlabel('Amount (Yuan) at Position ' + str(pos))
		ax.set_ylabel('Frequency')
		ax.set_xlim(0., 4.)
		ax.set_ylim(0., .7)
		ax.set_yticks(np.arange(0, 0.8, 0.2))

	plt.show()

def plotMaxMin(redpack_df):
	'''
		Max and Min values along all red packets
	'''
	sns.barplot(data = redpack_df.T, color = 'tomato', estimator = np.max, ci = 0, label = 'Max')
	ax = sns.barplot(data = redpack_df.T, color = 'darkturquoise', estimator = np.min, ci = 0, label = 'Min')
	ax.tick_params(axis = 'x', labelsize = 7)
	ax.tick_params(axis = 'y', labelsize = 8)
	ax.set_xticks(np.arange(0, redpack_df.shape[0], 10))
	ax.set_xticklabels(ax.get_xticklabels(), rotation = 70, fontsize = 10)
	ax.legend(loc = 'upper right')
	ax.set_xlabel('Red Envelopes (×10)')
	ax.set_ylabel('Amount (Yuan)')

	plt.show()

# TEST
if __name__ == '__main__':
	import redpack_datareading
	
	redpack_data = redpack_datareading.read()
	redpack_df = redpack_datareading.redpackDataFrame(redpack_data)
	# plotMeanVariance(redpack_df)
	plotPosDist(redpack_df)
	# plotMaxMin(redpack_df)
