import numpy as np
import matplotlib.pyplot as plt

def bipolar_pulse(n, N):
    pulse = np.zeros_like(n)
    pulse[(n >= 0) & (n <= N/2)] = 1
    pulse[(n > N/2) & (n <= N)] = -1
    return pulse

n = np.arange(-10, 11)
N = 3
pulse = bipolar_pulse(n, N)

plt.stem(n, pulse)
plt.title("Bipolar Pulse Function")
plt.xlabel("n")
plt.ylabel("Pulse")
