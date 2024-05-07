import time
from typing import List, Tuple, Any

from fuzzer.GreyBoxFuzzer import GreyBoxFuzzer
from schedule.PathPowerSchedule import PathPowerSchedule, get_path_id
from runner.FunctionCoverageRunner import FunctionCoverageRunner


class PathGreyBoxFuzzer(GreyBoxFuzzer):
    """Count how often individual paths are exercised."""

    def __init__(self, seeds: List[str], schedule: PathPowerSchedule):
        super().__init__(seeds, schedule)
        self.schedule = schedule
        self.schedule.path_frequency = {}
        self.last_path_time = self.start_time


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
        template = template.format(runtime=format_seconds(time.time() - self.start_time),
                                   path_time=format_seconds(self.last_path_time - self.start_time),
                                   crash_time=format_seconds(self.last_crash_time - self.start_time),
                                   total_exec=str(self.total_execs),
                                   total_path=len(self.schedule.path_frequency),
                                   uniq_crash=len(set(self.crash_map.values())),
                                   covered_line=len(self.covered_line))
        print(template)

    def run(self, runner: FunctionCoverageRunner) -> Tuple[Any, str]:  # type: ignore
        """Inform scheduler about path frequency"""
        result, outcome = super().run(runner)

        path_id = get_path_id(runner.coverage())
        if path_id not in self.schedule.path_frequency:
            self.schedule.path_frequency[path_id] = 1
            self.last_path_time = time.time()
        else:
            self.schedule.path_frequency[path_id] += 1

        return result, outcome
