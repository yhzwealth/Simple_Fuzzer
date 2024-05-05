from typing import List

from fuzzer.GreyBoxFuzzer import GreyBoxFuzzer
from schedule.PathSchedule import PathSchedule, get_path_id


class PathGreyBoxFuzzer(GreyBoxFuzzer):
    """Count how often individual paths are exercised."""

    def __init__(self, seeds: List[str], schedule: PathSchedule):
        super().__init__(seeds, schedule)
        self.schedule = schedule

    def reset(self):
        """Reset path frequency"""
        super().reset()
        self.schedule.path_frequency = {}

    def run(self, runner: FunctionCoverageRunner) -> Tuple[Any, str]:  # type: ignore
        """Inform scheduler about path frequency"""
        result, outcome = super().run(runner)

        path_id = get_path_id(runner.coverage())
        if path_id not in self.schedule.path_frequency:
            self.schedule.path_frequency[path_id] = 1
        else:
            self.schedule.path_frequency[path_id] += 1

        return result, outcome
