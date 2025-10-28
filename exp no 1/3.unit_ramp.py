import numpy as np
import matplotlib.pyplot as plt


def unit_ramp(n):
    ramp = np.zeros_like(n)
    ramp[n >= 0] = n[n >= 0]
    return ramp

n = np.arange(-10, 11)
ramp = unit_ramp(n)

plt.stem(n, ramp)
plt.title("Unit Ramp Function")
plt.xlabel("n")
plt.ylabel("Ramp")
