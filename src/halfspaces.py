"""Halfspaces and perceptrons for small course examples."""

from __future__ import division

import itertools


def all_boolean_points(dimension):
    """Return all Boolean vectors of a fixed dimension."""

    if dimension < 0:
        raise ValueError("dimension must be non-negative")
    return list(itertools.product((0, 1), repeat=dimension))


def linear_threshold(weights, bias):
    """Build h(x) = 1[w dot x + b >= 0]."""

    weights = tuple(float(weight) for weight in weights)
    bias = float(bias)

    def classifier(point):
        if len(point) != len(weights):
            raise ValueError("point dimension does not match weights")
        score = sum(weight * value for weight, value in zip(weights, point))
        return 1 if score + bias >= 0.0 else 0

    return classifier


def perceptron_predict(weights, bias, point):
    """Predict with a binary threshold perceptron."""

    classifier = linear_threshold(weights, bias)
    return classifier(point)


def perceptron_train(examples, labels, epochs=10, learning_rate=1.0):
    """Train a simple perceptron on binary labels 0/1.

    Returns (weights, bias, mistakes).
    """

    examples = [tuple(float(value) for value in example) for example in examples]
    labels = [1 if label else 0 for label in labels]
    if not examples:
        raise ValueError("examples must not be empty")
    if len(examples) != len(labels):
        raise ValueError("examples and labels must have the same length")

    dimension = len(examples[0])
    weights = [0.0] * dimension
    bias = 0.0
    mistakes = 0

    for _ in range(epochs):
        for point, label in zip(examples, labels):
            if len(point) != dimension:
                raise ValueError("all examples must have the same dimension")
            prediction = perceptron_predict(weights, bias, point)
            update = learning_rate * (label - prediction)
            if update != 0.0:
                mistakes += 1
                weights = [w + update * x for w, x in zip(weights, point)]
                bias += update

    return tuple(weights), bias, mistakes

