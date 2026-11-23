from __future__ import annotations
from . import state
import math

def mean_fitness(fitness_landscape: state.FitnessLandscape, frequency_state) -> float:
    return sum(
        fitness_landscape.get_fitness(genotype) 
        * frequency_state.get_genotype_frequency(genotype) 
        for genotype in fitness_landscape.fitness
    )

def relative_allele_fitness(allele: state.Allele, fitness_landscape: state.FitnessLandscape,
                            frequency_state, supplied_mean_fitness: float | None = None) -> float:
    """
    Returns the fitness of a certain allele relative to the current population.
    Returns 0 for an absent allele as a convention.
    """
    base = sum(
        fitness_landscape.get_fitness(genotype) 
        * frequency_state.get_genotype_frequency(genotype) 
        for genotype in fitness_landscape.fitness
        if allele in genotype
    ) 
    allele_frequency = frequency_state.get_allele_frequency(allele)
    if allele_frequency == 0:
        return 0
    return base / allele_frequency / (supplied_mean_fitness 
                               if supplied_mean_fitness is not None 
                               else mean_fitness(fitness_landscape, frequency_state))

def relative_genotype_fitness(genotype: state.Genotype, fitness_landscape: state.FitnessLandscape,
                            frequency_state, supplied_mean_fitness: float | None = None) -> float:
    """
    Returns genotype fitness divided by the current population mean fitness.
    """
    return fitness_landscape.get_fitness(genotype) / (supplied_mean_fitness 
                               if supplied_mean_fitness is not None 
                               else mean_fitness(fitness_landscape, frequency_state))

def mwua_update(fitness_landscape: state.FitnessLandscape, 
               frequency_state: state.MWUAFrequencyState) -> state.MWUAFrequencyState:
    """
    Performs one iteration of the MWUA loop (equation 1 of the paper).
    """
    supplied_mean_fitness = mean_fitness(fitness_landscape, frequency_state)
    return state.MWUAFrequencyState({
        allele: (
            frequency_state.get_allele_frequency(allele) 
            * relative_allele_fitness(
                allele, fitness_landscape, frequency_state,
                supplied_mean_fitness
            )
        )
        for allele in frequency_state.allele_frequencies
    })
    
def general_selection_update(fitness_landscape: state.FitnessLandscape, 
               frequency_state: state.GeneralFrequencyState) -> state.GeneralFrequencyState:
    """
    Performs one iteration of a general population genetics loop.
    No linkage equilibrium assumed.
    """
    supplied_mean_fitness = mean_fitness(fitness_landscape, frequency_state)
    return state.GeneralFrequencyState({
        genotype: (
            frequency_state.get_genotype_frequency(genotype) 
            * relative_genotype_fitness(
                genotype, fitness_landscape, frequency_state,
                supplied_mean_fitness
            )
        )
        for genotype in frequency_state.genotype_frequencies
    })

def general_recombination_update(frequency_state: state.GeneralFrequencyState, 
                         recombination_rate: float) -> state.GeneralFrequencyState:
    """
    Performs one round of recombination, expecting the following parameters:
    frequency_state: a post-selection general frequency state
    recombination rate r: a parameter 0 < r <= 1/2.
    Number of loci for each genotype is expected to be 2 as of now.
    
    Example: if parents g = (A3, B1), k = (A2, B3)
    then the mask "00" corresponds to (A3, B1), 
    and the mask "01" corresponds to (A3, B3), and so on.
    """
    new_frequency_state = state.GeneralFrequencyState({
        genotype: 0
        for genotype in frequency_state.genotype_frequencies
    })
    
    offspring = new_frequency_state.genotype_frequencies
    
    for parent_g, frequency_g in frequency_state.genotype_frequencies.items():
        for parent_k, frequency_k in frequency_state.genotype_frequencies.items():
            pair_probability = frequency_g * frequency_k
            
            # Number of loci must be equal to 2, else, raise an error
            if len(parent_g) != 2 or len(parent_k) != 2:
                raise ValueError("Recombination currently supports exactly two loci.")
            
            # Mask "00": both loci taken from parent g
            offspring[(parent_g[0], parent_g[1])] += pair_probability * (1 - recombination_rate) / 2
            
            # Mask "01": first locus taken from parent g, second locus taken from parent k
            offspring[(parent_g[0], parent_k[1])] += pair_probability * recombination_rate / 2
            
            # Mask "10": first locus taken from parent k, seocndl locus taken from parent g
            offspring[(parent_k[0], parent_g[1])] += pair_probability * recombination_rate / 2
            
            # Mask "11": both loci taken from parent k
            offspring[(parent_k[0], parent_k[1])] += pair_probability * (1 - recombination_rate) / 2
    
    return new_frequency_state