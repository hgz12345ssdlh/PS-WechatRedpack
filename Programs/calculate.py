import scipy.stats as stats

print(stats.beta.cdf(0.25, 1, 10))
print(stats.beta.cdf(1., 10, 1) - stats.beta.cdf(0.75, 10, 1))