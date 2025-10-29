import numpy as np  
import matplotlib.pyplot as plt

def triangular_pulse_train(n, N, T):
    pulse  = np.zeros_like(n, dtype=float)
    x = n - T * np.round(n / T) # Distance to nearest pulse center
    condition = np.abs(x) <= N/2
    pulse[condition] = 1 - np.abs(x[condition]) / (N/2)

    return pulse

n = np.arange(-30, 31)
N = 5
T = 10
pulse = triangular_pulse_train(n, N, T)
plt.stem(n, pulse)
plt.title("Triangular Pulse Train")
plt.xlabel("n")
plt.ylabel("Amplitude")



# second way:

# Using a different approach with a loop


import numpy as np  
import matplotlib.pyplot as plt

def triangular_pulse_train(n, N, T):
    pulse = np.zeros_like(n, dtype=float)

    num_shifts = int((n[-1] - n[0]) / T)
    print(num_shifts)
    
    for k in range(-num_shifts, num_shifts+1):
        x = n - k * T
        condition = np.abs(x) <= N / 2
        pulse[condition] += 1 - np.abs(x[condition]) / (N / 2)

    return pulse

n = np.arange(-100, 101)
N = 5
T = 10
pulse = triangular_pulse_train(n, N, T)
plt.stem(n, pulse)
plt.title("Triangular Pulse Train (N={}, T={})".format(N, T))
plt.xlabel("n")
plt.ylabel("Amplitude")
