import subprocess
import time
from typing import Tuple, List

from runner.Runner import Runner

Outcome = str


class Fuzzer:
    """Base class for fuzzers."""

    def __init__(self) -> None:
        """Constructor"""
        pass

    def fuzz(self) -> str:
        """Return fuzz input"""
        return ""

    def run(self, runner: Runner = Runner()) \
            -> Tuple[subprocess.CompletedProcess, Outcome]:
        """Run `runner` with fuzz input"""
        return runner.run(self.fuzz())

    def runs(self, runner: Runner = Runner(), run_time: int = 60) \
            -> List[Tuple[subprocess.CompletedProcess, Outcome]]:
        """Run `runner` with fuzz input, `trials` times"""
        now = time.time()
        res = list()
        while time.time() - now < run_time:
            res.append(self.run(runner))
        return res
