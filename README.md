# Algorithms, Games and Evolution

Cambridge Computer Science Part II project (2026–27), by Isaac Chan.

This project studies how natural selection and sexual reproduction relate to the multiplicative-weights update algorithm (MWUA), following Chastain et al. (2014). It aims to reproduce this connection and test how well it holds when assumptions such as weak selection and an infinite population are relaxed.

## Planned work

- Explain the mathematics and assumptions behind the connection.
- Implement population-genetics and MWUA models, including simulations of finite populations.
- Compare how allele frequencies change under different model settings.
- Provide reproducible experiments, plots and code documentation.

## Documents

- [Project proposal](proposal.pdf) — aims, scope and work plan.
- [Literature review](lit-review.pdf) — background and the connection between evolution, games and MWUA.

## Status

The first deterministic two-locus implementation is available: a reduced MWUA model and a full joint-frequency model with selection followed by recombination. The example runs both for ten generations and prints genotype and allele frequencies at generations 0, 1 and 10. Exact agreement with the paper's printed tables remains to be checked.

## Run the example

From the repository root (tested with Python 3.9.1):

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m experiments.chastain2014
```

- `evolution/state.py`: allele, fitness and frequency representations.
- `evolution/update.py`: MWUA, selection and two-locus recombination updates.
- `experiments/chastain2014.py`: example inputs and model trajectories.
- `experiments/formatting.py`: shared console table formatting.

The current functions assume normalized input frequencies, a complete genotype dictionary, unique allele IDs across loci, and positive mean fitness. The experiment uses recombination fraction 0.5. A committed automated test suite and finite-population simulations are still planned.

## Reference

Chastain, E., Livnat, A., Papadimitriou, C. H. and Vazirani, U. V. (2014). *Algorithms, games, and evolution*. PNAS, 111(29), 10620–10623. [Paper](https://doi.org/10.1073/pnas.1406556111).
