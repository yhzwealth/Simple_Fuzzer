import hashlib
import pickle
from typing import Dict, Sequence, Any

from schedule.PowerSchedule import PowerSchedule
from utils.Seed import Seed


def get_path_id(coverage: Any) -> str:
    """Returns a unique hash for the covered statements"""
    pickled = pickle.dumps(sorted(coverage))
    return hashlib.md5(pickled).hexdigest()


class PathPowerSchedule(PowerSchedule):

    def __init__(self, exponent: float) -> None:
        self.exponent = exponent
        self.path_frequency: Dict = {}

    def assign_energy(self, population: Sequence[Seed]) -> None:
        """Assign exponential energy inversely proportional to path frequency"""
        for seed in population:
            seed.energy = 1 / (self.path_frequency[get_path_id(seed.coverage)] ** self.exponent)
