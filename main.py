import os

from fuzzer.PathGreyBoxFuzzer import PathGreyBoxFuzzer
from runner.FunctionCoverageRunner import FunctionCoverageRunner
from schedule.PathPowerSchedule import PathPowerSchedule
from examples.Examples import example1, example2, example3, example4
from utils.ObjectUtils import dump_object, load_object


class Result:
    def __init__(self, coverage, crashes):
        self.covered_line = coverage
        self.crashes = crashes

    def __str__(self):
        return "Covered Lines: " + str(self.covered_line) + ", Crashes Num: " + str(self.crashes)


if __name__ == "__main__":
    f_runner = FunctionCoverageRunner(example4)
    corpus_path = "corpus"

    seeds = []
    for i in os.listdir(corpus_path):
        fname = os.path.join(corpus_path, i)
        if os.path.isfile(fname):
            with open(fname, 'r') as f:
                seeds.append(f.read())

    grey_fuzzer = PathGreyBoxFuzzer(seeds=seeds, schedule=PathPowerSchedule(5))
    grey_fuzzer.runs(f_runner, run_time=5)
    res = Result(grey_fuzzer.covered_line, set(grey_fuzzer.crash_map.values()))
    dump_object("_result" + os.sep + "res.pkl", res)
    print(load_object("_result" + os.sep + "res.pkl"))
