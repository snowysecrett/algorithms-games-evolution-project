# Simulation results (two-locus example, 22 Nov 2026)

After ten generations from uniform genotype frequencies, comparing MWUA with selection followed by recombination ($r=0.5000$). Interior cells show genotype frequencies; the margins show allele frequencies.
All frequencies are rounded to four decimal places for display.

## MWUA - linkage equilibrium

| | $B_1$ | $B_2$ | $B_3$ | Allele frequency |
|---|---:|---:|---:|---:|
| $A_1$ | $0.1109$ | $0.1311$ | $0.0976$ | $0.3396$ |
| $A_2$ | $0.0938$ | $0.1108$ | $0.0825$ | $0.2871$ |
| $A_3$ | $0.1219$ | $0.1441$ | $0.1073$ | $0.3733$ |
| **Allele frequency** | $0.3266$ | $0.3860$ | $0.2874$ | $1.0000$ |

## Selection + recombination

| | $B_1$ | $B_2$ | $B_3$ | Allele frequency |
|---|---:|---:|---:|---:|
| $A_1$ | $0.1118$ | $0.1312$ | $0.0968$ | $0.3397$ |
| $A_2$ | $0.0942$ | $0.1105$ | $0.0823$ | $0.2870$ |
| $A_3$ | $0.1205$ | $0.1442$ | $0.1085$ | $0.3732$ |
| **Allele frequency** | $0.3265$ | $0.3859$ | $0.2876$ | $1.0000$ |

Run: `python -m experiments.chastain2014`.