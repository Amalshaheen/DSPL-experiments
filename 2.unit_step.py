import numpy as np
import matplotlib.pyplot as plt

def unit_step(n):
    step = np.zeros_like(n)
    step[n >= 0] = 1
    return step

n = np.arange(-10, 11)
step = unit_step(n)

plt.stem(n, step)
plt.title("Unit Step Function")
plt.xlabel("n")
plt.ylabel("Step")