import numpy as np
import matplotlib.pyplot as plt


def dtft(x, n):
    omega = np.linspace(-np.pi, np.pi, 1000)
    X = np.zeros_like(omega, dtype=complex)
    for k, w in enumerate(omega):
        X[k] = np.sum(x * np.exp(-1j * w * n))
    return omega, X


n = np.arange(-10, 10)
x = np.sinc(n) # Example signal: sinc function

omega, X = dtft(x, n)

plt.plot(omega, np.abs(X))
plt.title("DTFT Magnitude")
plt.xlabel("Frequency")
plt.ylabel("|X(w)|")

plt.figure()

plt.plot(omega, np.angle(X))
plt.title("DTFT Phase")
plt.xlabel("Frequency")
plt.ylabel("angle(X(w))")

