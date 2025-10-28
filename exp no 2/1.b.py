import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    step = np.zeros_like(n)
    step[n >= 0] = 1
    return step
n = np.arange(-5, 6)

fn = unit_step(n) - unit_step(n-3)

plt.stem(n, fn)
plt.title("Unit Step Function")
plt.xlabel("n")
plt.ylabel("u[n] - u[n-3]")