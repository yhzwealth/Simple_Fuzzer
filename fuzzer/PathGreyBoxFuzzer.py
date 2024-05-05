from typing import List

from fuzzer.GreyBoxFuzzer import GreyBoxFuzzer
from schedule.PathSchedule import PathSchedule


class PathGreyBoxFuzzer(GreyBoxFuzzer):
    """Count how often individual paths are exercised."""

    def __init__(self, seeds: List[str], schedule: PathSchedule):
        super().__init__(seeds, schedule)
        # TODO

    def reset(self):
        """Reset path frequency"""
        super().reset()
        # TODO

    def run(self, runner: FunctionCoverageRunner) -> Tuple[Any, str]:  # type: ignore
        """Inform scheduler about path frequency"""
        result, outcome = super().run(runner)
        # TODO

        return result, outcome
