import numpy as np
import matplotlib.pyplot as plt


def unit_pulse(n, N, T):
    pulse = np.zeros_like(n)
    pulse[(n % T >= 0) & (n % T <= N)] = 1
    return pulse


n = np.arange(-10, 11)
N = 3
T = 10
pulse = unit_pulse(n, N, T)

plt.stem(n, pulse)
plt.title("Pulse Train Function")
plt.xlabel("n")
plt.ylabel("Pulse")
