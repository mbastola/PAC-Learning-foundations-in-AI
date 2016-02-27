"""Boolean decision lists.

A rule is a triple (index, value, label). The first matching rule returns its
label; otherwise the default label is returned.
"""


def evaluate_decision_list(rules, default_label, point):
    """Evaluate a Boolean decision list on one point."""

    for index, value, label in rules:
        if index < 0 or index >= len(point):
            raise ValueError("rule index out of range")
        if int(point[index]) == int(value):
            return 1 if label else 0
    return 1 if default_label else 0


def make_literal_rule(index, value, label):
    """Create a decision-list rule for x_index == value."""

    return (index, 1 if value else 0, 1 if label else 0)

