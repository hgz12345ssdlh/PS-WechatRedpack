# Local Modules
from redpack_datareading import read, redpackDataFrame
from redpack_plot import plotMeanVariance, plotPosDist, plotMaxMin
from redpack_simulation import redpackGenerate
from redpack_resultanalysis import compareMean, compareVariance, comparePosDist

# Data Collecting
raw_df = redpackDataFrame(read())
sample_size = raw_df.shape[0]
print('Sample Size is:', sample_size)

# Raw Data Plotting
plotMeanVariance(raw_df)
plotPosDist(raw_df)
plotMaxMin(raw_df)

# Simulation
simu_df_static = redpackGenerate('static', (10, 10), sample_size)
simu_df_dynamic = redpackGenerate('dynamic', (10, 10), sample_size)

# Hypotheses Testing
compareMean(raw_df, simu_df_static, simu_df_dynamic, \
			names = ('Raw Data', 'Static-Uniform Algo', 'Dynamic-Updating Algo'))
compareVariance(raw_df, simu_df_static, simu_df_dynamic, \
				names = ('Raw Data', 'Static-Uniform Algo', 'Dynamic-Updating Algo'))
comparePosDist(raw_df, simu_df_static, simu_df_dynamic, \
			   names = ('Raw', 'Static-Uniform', 'Dynamic-Updating'))
