import numpy as np
import matplotlib.pyplot as plt
m = 1.0 
k = 1.0  
g = 9.81 
y0 = 10.0 
t_start = 0.0
t_end = 12.0
dt = 0.1
t = np.arange(t_start, t_end, dt)
y = np.zeros_like(t)
v = np.zeros_like(t)
y[0] = y0
def uskor(y):
    return - g - k / m * y
for i in range(1, len(t)):
    v[i] = v[i-1] + uskor(y[i-1]) * dt
    y[i] = y[i-1] + v[i] * dt
    if y[i] < 0:
        y[i] = 0
        v[i] = - v[i-1]
plt.plot(t, y)
plt.xlabel('Время')
plt.ylabel('Координата')
plt.show()
