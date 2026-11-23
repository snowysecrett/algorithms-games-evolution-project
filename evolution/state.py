from __future__ import annotations
from dataclasses import dataclass
from typing import List
import numpy as np
import math

@dataclass(frozen=True)
class Allele:
    id: str
        
Genotype = tuple[Allele, ...] # Any number of alleles

Locus = List[Allele]

class FitnessLandscape:
    """
    Holds the fitness values for each genotype.
    We assume that it doesn't change across generations (for now).
    """
    def __init__(self, fitness: dict[Genotype, float]) -> None:
        self.fitness = fitness.copy()
        self.sum_fitnesses = sum(
            genotype_fitness
            for (_, genotype_fitness) in self.fitness.items()
        )
        self.genotype_count = len(fitness)
    def get_fitness(self, genotype: Genotype) -> float:
        return self.fitness[genotype]
    
class MWUAFrequencyState:
    """
    Holds the genotype and allele frequencies, assuming linkage equilibrium.
    This can represent our MWUA model but cannot represent a general population-genetics model.
    """
    def __init__(self, allele_frequencies: dict[Allele, float]) -> None:
        self.allele_frequencies = allele_frequencies.copy()
    def get_allele_frequency(self, allele: Allele) -> float:
        return self.allele_frequencies[allele]
    def get_genotype_frequency(self, genotype: Genotype) -> float:
        return math.prod(self.allele_frequencies[x] for x in genotype)
    
class GeneralFrequencyState:
    """
    Maintain genotype frequency for a general population-genetics model.
    """
    def __init__(self, genotype_frequencies: dict[Genotype, float]) -> None:
        self.genotype_frequencies = genotype_frequencies.copy()
    def get_allele_frequency(self, allele: Allele) -> float:
        return sum(
            frequency 
            for (genotype, frequency) in self.genotype_frequencies.items()
            if allele in genotype
        )
    def get_genotype_frequency(self, genotype: Genotype) -> float:
        return self.genotype_frequencies[genotype]