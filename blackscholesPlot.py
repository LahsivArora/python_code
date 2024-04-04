import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt 

N = norm.cdf

def BS_CALL(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * N(d1) - K * np.exp(-r*T)* N(d2)

def BS_PUT(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2/2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma* np.sqrt(T)
    return K*np.exp(-r*T)*N(-d2) - S*N(-d1)

K = 100
r = 0.1
T = 1
sigma = 0.3

# plot call and put prices with change in Spot
S = np.arange(60,140,0.1)
calls = [BS_CALL(s, K, T, r, sigma) for s in S]
puts = [BS_PUT(s, K, T, r, sigma) for s in S]
plt.plot(S, calls, label='Call Value')
plt.plot(S, puts, label='Put Value')
plt.xlabel('$S_0$')
plt.ylabel(' Value')
plt.legend()
plt.show()

# plot call and put prices with change in Vols
Sigmas = np.arange(0.1, 1.5, 0.01)
S = 100

calls = [BS_CALL(S, K, T, r, sig) for sig in Sigmas]
puts = [BS_PUT(S, K, T, r, sig) for sig in Sigmas]
plt.plot(Sigmas, calls, label='Call Value')
plt.plot(Sigmas, puts, label='Put Value')
plt.xlabel('$\sigma$')
plt.ylabel(' Value')
plt.legend()
plt.show()

# plot call and put prices with change in Time
T = np.arange(0.01, 2, 0.01)

calls = [BS_CALL(S, K, t, r, sigma) for t in T]
puts = [BS_PUT(S, K, t, r, sigma) for t in T]
plt.plot(T, calls, label='Call Value')
plt.plot(T, puts, label='Put Value')
plt.xlabel('$T$ in years')
plt.ylabel(' Value')
plt.legend()
plt.show()

# plot call and put prices with change in Strike
T = 1
K = np.arange(60,140,0.1)
calls = []
puts = []
for k in K:
    calls.append(BS_CALL(S, k, T, r, sigma))
    puts.append(BS_PUT(S, k, T, r, sigma))
plt.plot(K, calls, label='Call Value')
plt.plot(K, puts, label='Put Value')
plt.xlabel('$K_0$')
plt.ylabel(' Value')
plt.legend()
plt.show()