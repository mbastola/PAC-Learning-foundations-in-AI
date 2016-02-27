"""Print a few sample-complexity values from the course bounds."""

from __future__ import print_function

from pac_learning.bounds import finite_class_sample_complexity, vc_sample_complexity


def main():
    epsilon = 0.05
    delta = 0.05
    print("Finite class |H|=128:", finite_class_sample_complexity(128, epsilon, delta))
    print("VC dimension d=10:", vc_sample_complexity(10, epsilon, delta))


if __name__ == "__main__":
    main()

