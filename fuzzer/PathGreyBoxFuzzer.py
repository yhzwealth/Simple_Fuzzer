import time
from typing import List, Tuple, Any

from fuzzer.GreyBoxFuzzer import GreyBoxFuzzer
from schedule.PathPowerSchedule import PathPowerSchedule, get_path_id
from runner.FunctionCoverageRunner import FunctionCoverageRunner


class PathGreyBoxFuzzer(GreyBoxFuzzer):
    """Count how often individual paths are exercised."""

    def __init__(self, seeds: List[str], schedule: PathPowerSchedule):
        super().__init__(seeds, schedule)
        # TODO

    def reset(self):
        """Reset path frequency"""
        super().reset()
        # TODO

    def print_stats(self):
        def format_seconds(seconds):
            hours = int(seconds) // 3600
            minutes = int(seconds % 3600) // 60
            remaining_seconds = int(seconds) % 60
            return f"{hours:02d}:{minutes:02d}:{remaining_seconds:02d}"

        template = """
        -----------------TIMING-----------------
               Run Time: {runtime}
          Last New Path: {path_time}
        Last Uniq Crash: {crash_time}

        -----------------RESULT-----------------
            Total Execs: {total_exec}
            Total Paths: {total_path}
           Uniq Crashes: {uniq_crash}
          Covered Lines: {covered_line}
        """
        # TODO

        print(template)

    def run(self, runner: FunctionCoverageRunner) -> Tuple[Any, str]:  # type: ignore
        """Inform scheduler about path frequency"""
        result, outcome = super().run(runner)
        # TODO

        return result, outcome
