import random
from typing import Any


def insert_random_character(s: str) -> str:
    """Returns s with a random character inserted"""
    pos = random.randint(0, len(s))
    random_character = chr(random.randrange(32, 127))
    return s[:pos] + random_character + s[pos:]


def delete_random_character(s: str) -> str:
    """Returns s with a random character deleted"""
    if s == "":
        return insert_random_character(s)

    pos = random.randint(0, len(s) - 1)
    return s[:pos] + s[pos + 1:]


def flip_random_character(s: str) -> str:
    """Returns s with a random bit flipped in a random position"""
    if s == "":
        return insert_random_character(s)

    pos = random.randint(0, len(s) - 1)
    c = s[pos]
    bit = 1 << random.randint(0, 6)
    new_c = chr(ord(c) ^ bit)
    return s[:pos] + new_c + s[pos + 1:]


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
            delete_random_character,
            insert_random_character,
            flip_random_character
        ]

    def mutate(self, inp: Any) -> Any:  # can be str or Seed (see below)
        """Return s with a random mutation applied. Can be overloaded in subclasses."""
        mutator = random.choice(self.mutators)
        return mutator(inp)
