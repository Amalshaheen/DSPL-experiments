import numpy as np
import matplotlib.pyplot as plt
def unit_pulse(n, N):
    pulse = np.zeros_like(n)
    pulse[(n >= 0) & (n <= N)] = 1
    return pulse

n = np.arange(-10, 11)
N = 3
pulse = unit_pulse(n, N)

plt.stem(n, pulse)
plt.title("Unit Pulse Function")
plt.xlabel("n")
plt.ylabel("Pulse")
