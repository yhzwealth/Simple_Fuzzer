import random
from typing import Any


# TODO

class Mutator:

    def __init__(self) -> None:
        """Constructor"""
        self.mutators = [
            # TODO
        ]

    def mutate(self, inp: Any) -> Any:  # can be str or Seed (see below)
        """Return s with a random mutation applied. Can be overloaded in subclasses."""
        mutator = random.choice(self.mutators)
        return mutator(inp)
