# Algorithms, Games and Evolution

A University of Cambridge Computer Science Part II project (2026–27) by Isaac Chan, Churchill College.

This project studies the connection between population genetics, game theory and the multiplicative-weights update algorithm (MWUA). Building on Chastain et al. (2014), it asks how an idealised model of natural selection and sexual reproduction can be understood as a repeated coordination game between genes, and how accurately this algorithmic description captures evolutionary dynamics.

## Scope

The core work is to reconstruct the mathematical connection and its assumptions, demonstrate it computationally, and evaluate its accuracy when assumptions such as weak selection and an infinite population are relaxed.

Planned implementation and evaluation include:

- Deterministic population-genetics simulations and a corresponding MWUA model.
- Stochastic simulations of finite populations, including the effects of genetic drift.
- Reproducible experiments comparing allele-frequency trajectories as selection strength and other model parameters vary.
- Visualisations and documentation explaining the models, experiments and results.

The initial focus is on reproducing and evaluating the original connection. Broader extensions will be explored as the project develops.

## Documents

- [Project proposal](proposal.pdf) — aims, scope, evaluation and work plan.
- [Literature review](lit-review.pdf) — population-genetics background and the connection to games and MWUA.

## Current status

Implementation is beginning. This repository currently contains the proposal and literature review; simulation code, experiment scripts, results and usage instructions will be added as they are developed.

## Main reference

Erick Chastain, Adi Livnat, Christos H. Papadimitriou and Umesh V. Vazirani. *Algorithms, games, and evolution*. Proceedings of the National Academy of Sciences, 111(29), 10620–10623, 2014. [doi:10.1073/pnas.1406556111](https://doi.org/10.1073/pnas.1406556111).
