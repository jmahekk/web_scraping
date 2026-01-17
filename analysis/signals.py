import numpy as np

def generate_composite_signal(tfidf_matrix):
    signal = tfidf_matrix.sum(axis=1).A1

    mean = signal.mean()
    std = signal.std()

    ci_low = mean - 1.96 * std
    ci_high = mean + 1.96 * std

    return signal, ci_low, ci_high
