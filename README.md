# PAC Learning Foundations in Logical AI

This repository reevaluates my Master's CSE 513 theory-of-AI/ML course at WashU as a
small, executable study project in Python.

PAC learning, short for Probably Approximately Correct learning, is a
mathematical model of learning from examples. A learner receives samples from an
unknown distribution and should, with high probability, return a hypothesis
whose true error is small. In notation, for accuracy `epsilon` and confidence
`delta`, the learner should output a hypothesis `h` such that
`error(h) <= epsilon` with probability at least `1 - delta`.

PAC learning is important for foundational AI/ML because it separates the core
question of learning from implementation details: how many examples are needed,
what kinds of concept classes are learnable, and how model complexity affects
generalization. This is the thread connecting the repo's finite-class bounds,
VC dimension, halfspaces, perceptrons, decision lists, PAC semantics, and neural
network VC-dimension material. As a final intuition, the `epsilon`/`delta`
language echoes calculus: `epsilon` measures how close the learned hypothesis
must be to correct, while `delta` measures how rarely the learning process is
allowed to fail.

Here we rewrite the course ideas in Python:

- PAC learning definitions and finite-class bounds.
- VC dimension, shattering, growth functions, and Sauer-style bounds.
- Halfspaces, perceptrons, and decision lists.
- PAC semantics, classical entailment, and a small resolution example.
- The final-project thread on VC dimension of neural networks.

## Run

Run examples:

```bash
PYTHONPATH=src python3 examples/sample_complexity_demo.py
PYTHONPATH=src python3 examples/vc_dimension_demo.py
```

Build notes if a LaTeX distribution is installed:

```bash
make notes
```