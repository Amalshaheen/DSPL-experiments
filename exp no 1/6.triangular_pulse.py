import numpy as np
import matplotlib.pyplot as plt

def unit_triangular_pulse(n, N):
    pulse = np.zeros_like(n, dtype=float)
    condition = (n >= -N/2) & (n <= N/2)
    pulse[condition] = 1 - np.abs(n[condition]) / (N/2)
    return pulse

n = np.arange(-10, 11)
N = 10
pulse = unit_triangular_pulse(n, N)

plt.stem(n, pulse)
plt.title("Unit Triangular Pulse Function")
plt.xlabel("n")
plt.ylabel("Pulse")
