import numpy as np
import matplotlib.pyplot as plt
def unit_impulse(n):
    impulse = np.zeros_like(n)
    impulse[n == 0] = 1
    return impulse

n = np.arange(-5, 6)
impulse = unit_impulse(n) + unit_impulse(n-2) + unit_impulse(n+2)

plt.stem(n, impulse)
plt.title("Unit Impulse Function")
plt.xlabel("n")
plt.ylabel("δ[n] + δ[n-2] + δ[n+2]")
