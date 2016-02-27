"""Compute shattering behavior on a tiny Boolean universe."""

from __future__ import print_function

from pac_learning.halfspaces import all_boolean_points, linear_threshold
from pac_learning.vc_dimension import empirical_vc_dimension


def main():
    points = all_boolean_points(2)
    concepts = [
        linear_threshold((1, 0), -0.5),
        linear_threshold((-1, 0), 0.5),
        linear_threshold((0, 1), -0.5),
        linear_threshold((0, -1), 0.5),
        linear_threshold((1, 1), -0.5),
        linear_threshold((-1, -1), 1.5),
    ]
    print("Empirical VC dimension on {0,1}^2:", empirical_vc_dimension(concepts, points))


if __name__ == "__main__":
    main()

