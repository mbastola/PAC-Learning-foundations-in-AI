"""Brute-force VC-dimension utilities for finite examples."""

from __future__ import division

import itertools


def _as_bit(value):
    return 1 if value else 0


def all_labelings(size):
    """Yield every binary labeling of a set with the given size."""

    return itertools.product((0, 1), repeat=size)


def trace(concept, points):
    """Return the labeling induced by a concept on an ordered point list."""

    return tuple(_as_bit(concept(point)) for point in points)


def realized_labelings(concepts, points):
    """Return the set of labelings realized by concepts on points."""

    return set(trace(concept, points) for concept in concepts)


def is_shattered(concepts, points):
    """Return True when concepts realize every labeling of points."""

    realized = realized_labelings(concepts, points)
    return realized == set(all_labelings(len(points)))


def empirical_vc_dimension(concepts, candidate_points):
    """Compute VC dimension inside a finite candidate universe.

    This is an exhaustive educational helper. It is meant for tiny domains.
    """

    points = list(candidate_points)
    best = 0
    for size in range(len(points) + 1):
        shattered_at_size = False
        for subset in itertools.combinations(points, size):
            if is_shattered(concepts, subset):
                shattered_at_size = True
                best = size
                break
        if not shattered_at_size:
            break
    return best

