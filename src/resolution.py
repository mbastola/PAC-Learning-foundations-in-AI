"""Tiny propositional resolution helper.

Literals are signed integers: 2 means x_2, and -2 means not x_2.
Clauses are frozensets of literals.
"""


def complement(literal):
    return -literal


def is_tautology(clause):
    """Return True if a clause contains a literal and its complement."""

    clause = set(clause)
    return any(complement(literal) in clause for literal in clause)


def resolve_on(left, right, variable):
    """Resolve two clauses on a positive variable number."""

    if variable <= 0:
        raise ValueError("variable must be positive")
    left = frozenset(left)
    right = frozenset(right)
    if variable in left and -variable in right:
        return frozenset((left | right) - set((variable, -variable)))
    if -variable in left and variable in right:
        return frozenset((left | right) - set((variable, -variable)))
    raise ValueError("clauses do not contain complementary literals")


def derives_empty_clause(left, right, variable):
    """Return True if resolving two clauses on variable gives contradiction."""

    return len(resolve_on(left, right, variable)) == 0

