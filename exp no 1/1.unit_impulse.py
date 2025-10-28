import numpy as np
import matplotlib.pyplot as plt

def unit_impulse(n):
    impulse = np.zeros_like(n)
    impulse[n == 0] = 1
    return impulse

n = np.arange(-10, 11)
impulse = unit_impulse(n)

plt.stem(n, impulse)
plt.title("Unit Impulse Function")
plt.xlabel("n")
plt.ylabel("Impulse")
