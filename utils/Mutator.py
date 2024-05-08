import random
from typing import Any


def insert_random_character(s: str) -> str:
    """Returns s with a random character inserted"""
    # TODO


def delete_random_character(s: str) -> str:
    """Returns s with a random character deleted"""
    # TODO


def flip_random_character(s: str) -> str:
    """Returns s with a random bit flipped in a random position"""
    # TODO


def duplicate_random_character(s: str) -> str:
    """Copy a range of characters."""
    # TODO


def set_random_character(s: str) -> str:
    """Set a character to a random value"""
    # TODO


def swap_random_character(s: str) -> str:
    """Swap 2 characters."""
    # TODO


class Mutator:

    def __init__(self) -> None:
        """Constructor"""
        self.mutators = [
            insert_random_character,
            delete_random_character,
            flip_random_character,
            duplicate_random_character,
            set_random_character,
            swap_random_character
        ]

    def mutate(self, inp: Any) -> Any:  # can be str or Seed (see below)
        """Return s with a random mutation applied. Can be overloaded in subclasses."""
        mutator = random.choice(self.mutators)
        return mutator(inp)
