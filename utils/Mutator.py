import random
from typing import Any


# TODO

def duplicate_random_character(s: str) -> str:
    """Copy a range of characters."""
    pass


def set_random_character(s: str) -> str:
    """Set a character to a random value"""
    pass


def swap_random_character(s: str) -> str:
    """Swap 2 characters."""
    pass


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
