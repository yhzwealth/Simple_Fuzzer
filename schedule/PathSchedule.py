from typing import Dict, Sequence

from schedule.Schedule import Schedule
from utils.Seed import Seed


class PathSchedule(Schedule):

    def __init__(self) -> None:
        super().__init__()
        # TODO

    def assign_energy(self, population: Sequence[Seed]) -> None:
        """Assign exponential energy inversely proportional to path frequency"""
        # TODO
