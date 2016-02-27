"""Small executable pieces for Theory of AI/ML course."""

from .bounds import (
    binomial,
    finite_class_sample_complexity,
    sauer_growth_bound,
    vc_sample_complexity,
)
from .decision_lists import evaluate_decision_list
from .halfspaces import all_boolean_points, linear_threshold, perceptron_train
from .pac_semantics import implication_probability, pac_entails
from .vc_dimension import empirical_vc_dimension, is_shattered, realized_labelings

__all__ = [
    "all_boolean_points",
    "binomial",
    "empirical_vc_dimension",
    "evaluate_decision_list",
    "finite_class_sample_complexity",
    "implication_probability",
    "is_shattered",
    "linear_threshold",
    "pac_entails",
    "perceptron_train",
    "realized_labelings",
    "sauer_growth_bound",
    "vc_sample_complexity",
]

