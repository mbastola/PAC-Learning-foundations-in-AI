"""Finite-distribution PAC-semantics helpers."""

from __future__ import division


def _check_distribution(distribution):
    total = sum(probability for _, probability in distribution)
    if abs(total - 1.0) > 1e-9:
        raise ValueError("distribution probabilities must sum to 1")
    for _, probability in distribution:
        if probability < 0.0:
            raise ValueError("distribution probabilities must be non-negative")


def implication_probability(premise, conclusion, distribution):
    """Return Pr[premise(x) => conclusion(x)] for a finite distribution."""

    distribution = list(distribution)
    _check_distribution(distribution)
    probability = 0.0
    for point, mass in distribution:
        if (not premise(point)) or conclusion(point):
            probability += mass
    return probability


def pac_entails(premise, conclusion, distribution, epsilon):
    """Return True when implication holds with probability at least 1-epsilon."""

    if epsilon < 0.0 or epsilon > 1.0:
        raise ValueError("epsilon must be between 0 and 1")
    return implication_probability(premise, conclusion, distribution) >= 1.0 - epsilon

