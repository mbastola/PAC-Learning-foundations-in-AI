"""PAC and VC-dimension bounds used by the notes.

The functions are intentionally plain in Python: no numeric stack is needed for these definitions.
"""

from __future__ import division

import math


def _check_probability(name, value):
    if value <= 0.0 or value >= 1.0:
        raise ValueError("%s must be strictly between 0 and 1" % name)


def binomial(n, k):
    """Return n choose k without relying on math.comb."""

    if k < 0 or k > n:
        return 0
    k = min(k, n - k)
    result = 1
    for i in range(1, k + 1):
        result = result * (n - k + i) // i
    return result


def finite_class_sample_complexity(num_hypotheses, epsilon, delta):
    """Consistent-learner PAC bound for a finite hypothesis class.

    A standard union-bound proof gives

        m >= (log |H| + log(1/delta)) / epsilon.
    """

    if num_hypotheses < 1:
        raise ValueError("num_hypotheses must be positive")
    _check_probability("epsilon", epsilon)
    _check_probability("delta", delta)
    numerator = math.log(num_hypotheses) + math.log(1.0 / delta)
    return int(math.ceil(numerator / epsilon))


def sauer_growth_bound(vc_dimension, sample_size):
    """Return Sauer's lemma upper bound for a class of VC dimension d."""

    if vc_dimension < 0:
        raise ValueError("vc_dimension must be non-negative")
    if sample_size < 0:
        raise ValueError("sample_size must be non-negative")
    if vc_dimension >= sample_size:
        return 2 ** sample_size
    return sum(binomial(sample_size, i) for i in range(vc_dimension + 1))


def vc_sample_complexity(vc_dimension, epsilon, delta):
    """A simple teaching bound for VC-style sample complexity.

    The archive uses the order

        O((d log(1/epsilon) + log(1/delta)) / epsilon).

    This function keeps that dependence explicit with conservative constants.
    """

    if vc_dimension < 0:
        raise ValueError("vc_dimension must be non-negative")
    _check_probability("epsilon", epsilon)
    _check_probability("delta", delta)
    inside = vc_dimension * math.log(2.0 / epsilon) + math.log(2.0 / delta)
    return int(math.ceil((4.0 / epsilon) * inside))

