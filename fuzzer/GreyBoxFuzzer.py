from typing import List, Any, Tuple

import random

from fuzzer.Fuzzer import Fuzzer
from runner.Runner import Runner
from utils.Mutator import Mutator
from runner.FunctionCoverageRunner import FunctionCoverageRunner
from schedule.Schedule import Schedule

from utils.Seed import Seed


class GreyBoxFuzzer(Fuzzer):

    def __init__(self, seeds: List[str], schedule: Schedule) -> None:
        """Constructor.
        `seeds` - a list of (input) strings to mutate.
        `mutator` - the mutator to apply.
        `schedule` - the power schedule to apply.
        """
        super().__init__()
        self.population = None
        self.coverages_seen = None
        self.seed_index = None
        self.crash_map = None
        self.seeds = seeds
        self.mutator = Mutator()
        self.schedule = schedule
        self.reset()

    def reset(self):
        """Reset the initial population, seed index, coverage information"""
        self.seed_index = 0
        self.coverages_seen = set()
        self.crash_map = dict()
        self.population = []  # population is filled during greybox fuzzing

    def create_candidate(self) -> str:
        """Returns an input generated by fuzzing a seed in the population"""
        seed = self.schedule.choose(self.population)

        # Stacking: Apply multiple mutations to generate the candidate
        candidate = seed.data
        trials = min(len(candidate), 1 << random.randint(1, 5))
        for i in range(trials):
            candidate = self.mutator.mutate(candidate)
        return candidate

    def fuzz(self) -> str:
        """Returns first each seed once and then generates new inputs"""
        if self.seed_index < len(self.seeds):
            # Still seeding
            self.inp = self.seeds[self.seed_index]
            self.seed_index += 1
        else:
            # Mutating
            self.inp = self.create_candidate()

        return self.inp

    def run(self, runner: FunctionCoverageRunner) -> Tuple[Any, str]:  # type: ignore
        """Run function(inp) while tracking coverage.
           If we reach new coverage,
           add inp to population and its coverage to population_coverage
        """
        result, outcome = super().run(runner)
        new_coverage = frozenset(runner.coverage())
        if new_coverage not in self.coverages_seen:
            # We have new coverage
            seed = Seed(self.inp, runner.coverage())
            self.coverages_seen.add(new_coverage)
            self.population.append(seed)
        if outcome == Runner.FAIL:
            self.crash_map[self.inp] = result

        return result, outcome
