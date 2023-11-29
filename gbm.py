import numpy as np
import matplotlib.pyplot as plt
import math

# Parameter Definitions

# S0    :   initial stock price
# dt    :   time increment -> a day in our case
# T     :   length of the prediction time horizon(how many time points to predict, same unit with dt(days))
# N     :   number of time points in prediction the time horizon -> T/dt
# t     :   array for time points in the prediction time horizon [1, 2, 3, .. , N]
# mu    :   mean of historical daily returns
# sigma :   standard deviation of historical daily returns
# b     :   array for brownian increments
# W     :   array for brownian path

T = 100
dt = 1
N = T//dt
S0 = 50
t = [i for i in range(1,N+1)]
print(t)
mu = 1
sigma = 1

scen_size = 50 # User input
b = {str(scen): np.random.normal(0, 1, int(N)) for scen in range(1, scen_size + 1)}
W = {str(scen): b[str(scen)].cumsum() for scen in range(1, scen_size + 1)}

# Calculating drift and diffusion components
drift = [(mu - 0.5 * sigma**2) * i for i in t]
#print(drift)
diffusion = {str(scen): sigma * W[str(scen)] for scen in range(1, scen_size + 1)}
#print(diffusion)

# Making the predictions
S = np.array([S0 * np.exp(drift + diffusion[str(scen)]) for scen in range(1, scen_size + 1)]) 
S = np.hstack((np.array([[S0] for scen in range(scen_size)]), S)) # add So to the beginning series
print(S[1][0:29])

# Plotting the simulations
for i in range(scen_size):
    plt.title("Daily Volatility: " + str(sigma))
    plt.plot(t, S[1][1:])
    plt.ylabel('Stock Prices, €')
    plt.xlabel('Prediction Days')
plt.show()