import matplotlib.pyplot as plt
import numpy as np

def plot_signal(signal, low_ci, high_ci):
    x = np.arange(len(signal))

    plt.figure(figsize=(10, 4))
    plt.plot(x, signal, label="Market Signal")
    plt.axhline(low_ci, linestyle="--", label="Lower CI")
    plt.axhline(high_ci, linestyle="--", label="Upper CI")

    plt.title("Indian Stock Market Twitter Signal")
    plt.xlabel("Tweet Index")
    plt.ylabel("Signal Strength")
    plt.legend()
    plt.tight_layout()
    plt.show()
