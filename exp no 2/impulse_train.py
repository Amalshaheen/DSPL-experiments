import numpy as np
import matplotlib.pyplot as plt

def impulse_train(n,T):
    impulse = np.zeros_like(n)
    impulse[n % T == 0] = 1
    return impulse

n = np.arange(-10, 11)
T = 3
impulse = impulse_train(n,T)

plt.stem(n, impulse)
plt.title("Impulse Train Function")
plt.xlabel("n")
plt.ylabel("Impulse")
