from __future__ import annotations
from evolution import state, update
from experiments.formatting import print_frequency_table

"""
Completion date: 2026-11-22
We reproduce the worked example by Chastain et al. (2014), shown on Fig. 1 & Fig. 2
of their paper. In the example shown, a haploid organism with two genetic loci A and
B has three allele variants in each of its two loci named A1, A2, A3, and B1, B2, B3
respectively, totalling nine genotypes.
"""

"""
We first run our independent MWUA implementation on the paper's example to check for 
consistent results.
"""


# 2 loci, 3 allele variants each.
loci: list[state.Locus] = [
    [state.Allele("A1"), state.Allele("A2"), state.Allele("A3")],
    [state.Allele("B1"), state.Allele("B2"), state.Allele("B3")],
]

# Fig. 1, Table A: Fitness values.
fitness_landscape = state.FitnessLandscape({
    (state.Allele("A1"), state.Allele("B1")): 1.02,
    (state.Allele("A1"), state.Allele("B2")): 1.03,
    (state.Allele("A1"), state.Allele("B3")): 0.99,
    (state.Allele("A2"), state.Allele("B1")): 1.00,
    (state.Allele("A2"), state.Allele("B2")): 1.01,
    (state.Allele("A2"), state.Allele("B3")): 0.98,
    (state.Allele("A3"), state.Allele("B1")): 1.01,
    (state.Allele("A3"), state.Allele("B2")): 1.04,
    (state.Allele("A3"), state.Allele("B3")): 1.02
})

mwua_initial_state = state.MWUAFrequencyState({
    state.Allele("A1"): 1 / 3,
    state.Allele("A2"): 1 / 3,
    state.Allele("A3"): 1 / 3,
    state.Allele("B1"): 1 / 3,
    state.Allele("B2"): 1 / 3,
    state.Allele("B3"): 1 / 3
})

mwua_iterative_states = [mwua_initial_state]

for i in range(0, 10):
    mwua_iterative_states.append(
        update.mwua_update(fitness_landscape, 
                           mwua_iterative_states[i]
        )
    )

for generation in (0, 1, 10):
    print_frequency_table(
        mwua_iterative_states[generation],
        loci,
        title=f"Generation {generation} — MWUA (linkage equilibrium)",
    )

"""
Next, we implement a selection-recombination model with recombination rate = 1/2
without assuming linkage equilibrium. Check its outputs against MWUA.
"""

general_initial_state = state.GeneralFrequencyState({
    genotype: mwua_initial_state.get_genotype_frequency(genotype)
    for genotype in fitness_landscape.fitness
})

general_iterative_states = [general_initial_state]
recombination_rate = 1 / 2
for i in range(0, 10):
    general_iterative_states.append(
        update.general_recombination_update(
            update.general_selection_update(fitness_landscape, 
                           general_iterative_states[i]
            ),
            recombination_rate
        )
    )

for generation in (0, 1, 10):
    print_frequency_table(
        general_iterative_states[generation],
        loci,
        title=f"Generation {generation} — Selection + recombination",
    )