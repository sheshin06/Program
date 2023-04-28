import numpy as np
import matplotlib.pyplot as plt
a = 0.3
def s(k):
    return np.cos(7*k+2)
def n(k):
    length = k.shape[0]
    u, d = 0, 0.05
    noise = np.random.normal(u, d, size=length)
    return noise
k = np.arange(0, 5*np.pi, 0.1)
S = s(k)
D = S + n(k)
F = D +  a
def s(a, axis=0, ddof=0):
    a = np.asanyarray(a)
    m = a.mean(axis)
    sd = a.std(axis=axis, ddof=ddof)
    return np.where(sd == 0, 0, m/sd)
print(s(k))
print(s(F, axis = 0, ddof = 0))
print(s(D, axis = 0, ddof = 0))
plt.plot(k, S, color='green', label="s(k)")
plt.plot(k, D, label='s(k)+n(k)')
plt.plot(k, F, label='s(k)+n(k)+a')
plt.legend(loc='best')
plt.xlabel('k')
plt.ylabel('v')
plt.show()