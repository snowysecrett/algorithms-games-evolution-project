# Results — two-locus example

Ten generations from uniform genotype frequencies (1/9), using the fitness matrix in `experiments/chastain2014.py`; the general model applies selection followed by recombination with r = 0.5.
The models agree on allele frequencies after one generation (within floating-point precision); the maximum absolute allele-frequency difference after ten generations is 0.00018549.

## Allele frequencies at generation 10

| Allele | MWUA | Selection + recombination | Absolute difference |
|---|---:|---:|---:|
| A1 | 0.33960053 | 0.33970193 | 0.00010140 |
| A2 | 0.28713962 | 0.28704858 | 0.00009104 |
| A3 | 0.37325985 | 0.37324949 | 0.00001036 |
| B1 | 0.32658295 | 0.32649264 | 0.00009031 |
| B2 | 0.38599617 | 0.38590099 | 0.00009518 |
| B3 | 0.28742088 | 0.28760637 | 0.00018549 |

## Genotype frequencies at generation 10

| Genotype | MWUA (product distribution) | Selection + recombination |
|---|---:|---:|
| A1, B1 | 0.11090774 | 0.11178246 |
| A1, B2 | 0.13108451 | 0.13116347 |
| A1, B3 | 0.09760828 | 0.09675601 |
| A2, B1 | 0.09377490 | 0.09418924 |
| A2, B2 | 0.11083479 | 0.11054575 |
| A2, B3 | 0.08252992 | 0.08231358 |
| A3, B1 | 0.12190030 | 0.12052094 |
| A3, B2 | 0.14407687 | 0.14419177 |
| A3, B3 | 0.10728268 | 0.10853678 |

Run: `python -m experiments.chastain2014` · Implementation: `d7b9b81` · Values rounded for display.
