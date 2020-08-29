#import matplotlib.pyplot as plt
import numpy as np
from numpy.random import default_rng
from matplotlib import pyplot as plt




#normal
mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.default_rng().normal(mu, sigma, 100000)
plt.figure(1)
count, bins, ignored = plt.hist(s, 30, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
np.exp( - (bins - mu)**2 / (2 * sigma**2) ),linewidth=2, color='r')
plt.title("Normal distribution")


#dirichlet
s = np.random.default_rng().dirichlet((10, 5, 3), 100).transpose()
plt.figure(2)
plt.barh(range(100), s[0])
plt.barh(range(100), s[1], left=s[0], color='g')
plt.barh(range(100), s[2], left=s[0]+s[1], color='r')
plt.title("Dirichlet didtribution(Lengths of Strings)")

#exponential
s = default_rng().exponential(1,100000)
plt.figure(3)
plt.hist(s)
plt.title("Exponential distribution")

#logistic
loc, scale = 10, 1
s = np.random.default_rng().logistic(loc, scale, 10000)
plt.figure(4)
count, bins, ignored = plt.hist(s, bins=50)
# plot against distribution
def logist(x, loc, scale):
	return np.exp((loc-x)/scale)/(scale*(1+np.exp((loc-x)/scale))**2)
lgst_val = logist(bins, loc, scale)
plt.plot(bins, lgst_val * count.max() / lgst_val.max())
plt.title("Logistic distribution")


#log_normal
rng = np.random.default_rng()
mu, sigma = 3., 1. # mean and standard deviation
s = rng.lognormal(mu, sigma, 1000)
plt.figure(5)
count, bins, ignored = plt.hist(s, 100, density=True, align='mid')
x = np.linspace(min(bins), max(bins), 10000)
pdf = (np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2)) / (x * sigma * np.sqrt(2 * np.pi)))
plt.plot(x, pdf, linewidth=2, color='r')
plt.axis('tight')
plt.title("Log normal distribution")

#multivariate normal
mean = [0, 0]
cov = [[1, 0], [0, 100]]  # diagonal covariance
x, y = np.random.default_rng().multivariate_normal(mean, cov, 100000).T
plt.figure(6)
plt.plot(x, y, 'x')
plt.axis('equal')
plt.title("multivariate_normal distribution")

#uniform
s = np.random.default_rng().uniform(-1,0,100000)
plt.figure(7)
count, bins, ignored = plt.hist(s, 15, density=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.title("uniform distribution")


#power law
rng = np.random.default_rng()
a = 5. # shape
samples = 100000
s = rng.power(a, samples)
plt.figure(8)
count, bins, ignored = plt.hist(s, bins=30)
x = np.linspace(0, 1, 100)
y = a*x**(a-1.)
normed_y = samples*np.diff(bins)[0]*y
plt.plot(x, normed_y)
plt.title("Power law distribution")
plt.show()





