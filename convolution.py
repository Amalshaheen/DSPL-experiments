import numpy as np


def convolve(x, h):
    len_x = len(x)
    len_h = len(h)
    len_y = len_x + len_h - 1
    y = np.zeros(len_y)

    for n in range(len_y):
        for k in range(len_h):
            if 0 <= n - k < len_x:
                y[n] += x[n - k] * h[k]
    return y

# Example usage
x = np.array([1, 2, 3, 4])
h = np.array([1,1,1,1,1,1,1,1])
y = convolve(x, h)
n2 = np.arange(0, len(y))
print("Input Signal x[n]:", x)
print("Impulse Response h[n]:", h)
print("Output Signal y[n]:", y)